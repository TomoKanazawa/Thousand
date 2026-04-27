"""Fetch 10 MTSamples cases across mixed ambulatory specialties.

Auto-discovers real sample URLs from each specialty's browse page,
then fetches the chosen cases. Idempotent — skips files already on disk.

MTSamples requires a Referer header on every request, so we maintain
a session and pass referers explicitly.
"""

from __future__ import annotations

import re
import time
from pathlib import Path
from urllib.parse import unquote, urljoin

import requests
from bs4 import BeautifulSoup

BASE = "https://www.mtsamples.com"

# (browse-type-param, label, how-many-cases-to-take)
# Skew toward specialties with diagnostic-puzzle visits (consults, ER) and
# away from chronic-disease followups (Endo is heavy on followups).
# Take more than we need per specialty — prepare_cases.py drops thin charts
# and we want 30 valid cases at the end. Total budget here ≈ 50 raw cases.
SPECIALTIES: list[tuple[str, str, int]] = [
    ("98-General+Medicine", "GenMed", 200),
    ("6-Cardiovascular+%2F+Pulmonary", "Cardio", 200),
    ("24-Gastroenterology", "GI", 200),
    ("42-Neurology", "Neuro", 200),
    ("93-Emergency+Room+Reports", "ER", 75),
    ("97-Consult+%2D+History+and+Phy%2E", "Consult", 200),
    ("3-Allergy+%2F+Immunology", "Allergy", 8),
    ("41-Nephrology", "Nephro", 81),
    ("87-Office+Notes", "Office", 53),
    ("91-SOAP+%2F+Chart+%2F+Progress+Notes", "SOAP", 167),
    ("100-ENT+%2D+Otolaryngology", "ENT", 100),
    ("96-Hematology+%2D+Oncology", "HemOnc", 91),
    ("105-Pain+Management", "PainMgmt", 63),
    ("78-Sleep+Medicine", "Sleep", 20),
    ("77-Rheumatology", "Rheum", 10),
    ("18-Dermatology", "Derm", 30),
    ("21-Endocrinology", "Endo", 20),
    ("45-Obstetrics+%2F+Gynecology", "OBGYN", 100),
    ("72-Psychiatry+%2F+Psychology", "Psych", 53),
    ("82-Urology", "Uro", 100),
]

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
COMMON_HEADERS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

# PREFER: titles that name a SYMPTOM/CHIEF COMPLAINT — the diagnosis is hidden
# and the model has to reason it out from the chart. These are real DDx puzzles.
PREFER_TITLE_PATTERNS = re.compile(
    r"\b(pain|ache|dyspnea|shortness of breath|sob|cough|fatigue|"
    r"weight loss|nausea|vomit|diarrhea|constipation|"
    r"headache|dizziness|syncope|weakness|numbness|"
    r"fever|rash|edema|bleeding|hematuria|hematemesis|"
    r"palpitation|dysphagia|jaundice)\b",
    re.IGNORECASE,
)

# Hard-skip — none of these are DDx puzzles:
SKIP_TITLE_PATTERNS = re.compile(
    # Procedures / imaging / labs (no diagnostic reasoning)
    r"\b(doppler|echocardiogram|ekg|ecg|x-?ray|mri|ct\b|ultrasound|"
    r"i&d|fusion|exploration|resection|repair|excision|biopsy|"
    r"endoscopy|colonoscopy|catheterization|angiogram|"
    r"letter|discharge summary|chiropract|cosmetic|operative|"
    r"surgery|procedure|imaging|laceration|"
    # Diagnosis-in-title — model can read it off the chart
    r"diabetes|hypothyroid|hyperthyroid|hypertension|"
    r"atrial fibrillation|copd|asthma|"
    r"pulmonary edema|heart failure|chf|"
    r"hemorrhoid|cancer|cva|stroke|tia|sepsis|"
    r"pneumonia|copd|emphysema|cirrhosis|"
    r"q[\s-]?fever|"
    # Any word ending in a disease-suffix is almost certainly a diagnosis name
    r"\w+itis|\w+osis|\w+emia|\w+pathy|\w+oma\b|"
    # Followups — diagnosis already established, not new DDx
    r"follow[\s-]?up|f/u|soap|return visit|"
    # Pediatric/neonatal — different DDx criteria, off-target for ambulatory adult
    r"pediatric|neonatal|newborn|infant|child|"
    r"\d+[\s-]?(month|year|day)[\s-]?old|"
    r"juvenile|teen|teenager|adolescent|"
    # Procedural/management consults masquerading as DDx
    r"bariatric|gastric bypass|roux[\s-]?en[\s-]?y|lap band|"
    r"weight loss evaluation|weight loss surgery|weight loss consult|"
    r"urinary retention|foley|catheter placement|"
    # Trauma — fast surgical reasoning, not medical DDx
    r"fight|fighting|gunshot|stab|fall(?:en)?|mva|motor vehicle|trauma|"
    # Toxic ingestion — diagnosis is a known event, not clinical reasoning
    r"ingestion|overdose|poisoning|intoxication|"
    # Inpatient admission notes (we want ambulatory)
    r"admission)\b",
    re.IGNORECASE,
)


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return s[:40]


def discover_samples(session: requests.Session, type_param: str) -> list[tuple[str, str]]:
    """Return [(title, full_sample_url), ...] for one specialty."""
    browse_url = f"{BASE}/site/pages/browse.asp?type={type_param}"
    resp = session.get(browse_url, headers={"Referer": BASE + "/"}, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    pairs: list[tuple[str, str]] = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "sample.asp?" not in href:
            continue
        title = a.get_text(strip=True)
        if not title or len(title) < 4:
            continue
        if SKIP_TITLE_PATTERNS.search(title):
            continue
        full = urljoin(BASE, href)
        pairs.append((title, full))

    # Dedupe while preserving order.
    seen: set[str] = set()
    unique: list[tuple[str, str]] = []
    for t, u in pairs:
        if u in seen:
            continue
        seen.add(u)
        unique.append((t, u))

    # Prefer symptom-titled cases up front; let others fill remaining slots.
    # SKIP_TITLE_PATTERNS already excludes the worst (procedures, diagnosis-titled).
    preferred = [p for p in unique if PREFER_TITLE_PATTERNS.search(p[0])]
    others = [p for p in unique if not PREFER_TITLE_PATTERNS.search(p[0])]
    return preferred + others


def extract_note_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find("div", id="sampletext") or soup.find("div", class_="hilightBold")
    if main:
        text = main.get_text("\n", strip=True)
    else:
        text = soup.get_text("\n", strip=True)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def main() -> None:
    out_dir = Path(__file__).parent / "cases"
    out_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update(COMMON_HEADERS)

    counter = 1
    seen_urls: set[str] = set()
    seen_titles: set[str] = set()  # MTSamples lists the same note under multiple specialties
    symptom_counts: dict[str, int] = {}  # cap diversity per primary symptom
    SYMPTOM_CAP = 100  # effectively no cap during harvest
    for type_param, label, take in SPECIALTIES:
        print(f"\n[{label}] discovering samples for type={type_param}")
        try:
            samples = discover_samples(session, type_param)
        except Exception as e:
            print(f"  ERROR discovering {label}: {e}")
            continue
        print(f"  found {len(samples)} candidates")

        browse_url = f"{BASE}/site/pages/browse.asp?type={type_param}"
        taken = 0
        for title, url in samples:
            if taken >= take:
                break
            if url in seen_urls:
                continue
            seen_urls.add(url)
            # MTSamples cross-lists the same note under multiple specialties.
            # Match by normalized title to catch these duplicates.
            title_key = re.sub(r"\s+", " ", title.lower().strip())
            if title_key in seen_titles:
                print(f"  [dup ] {title[:60]} (already seen)")
                continue
            seen_titles.add(title_key)

            # Cap how many cases share the same primary symptom keyword.
            sym_match = PREFER_TITLE_PATTERNS.search(title)
            sym_key = sym_match.group(0).lower() if sym_match else "_other"
            if symptom_counts.get(sym_key, 0) >= SYMPTOM_CAP:
                print(f"  [cap ] {title[:60]} (symptom '{sym_key}' already at cap)")
                continue
            symptom_counts[sym_key] = symptom_counts.get(sym_key, 0) + 1

            slug = slugify(title)
            idx = f"{counter:02d}"
            out_path = out_dir / f"{idx}_{slug}.txt"
            if out_path.exists():
                print(f"  [skip] {out_path.name}")
                counter += 1
                taken += 1
                continue

            try:
                resp = session.get(url, headers={"Referer": browse_url}, timeout=30)
                resp.raise_for_status()
            except Exception as e:
                print(f"  [fail] {title[:50]}: {e}")
                continue

            text = extract_note_text(resp.text)
            if len(text) < 400:
                print(f"  [thin] {title[:50]} ({len(text)} chars) — skipping")
                continue

            out_path.write_text(text, encoding="utf-8")
            print(f"  [ok]   {idx} {title[:60]}")
            counter += 1
            taken += 1
            time.sleep(1.5)

    print(f"\nDone. {counter - 1} cases in {out_dir}")


if __name__ == "__main__":
    main()
