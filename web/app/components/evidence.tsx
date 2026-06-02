type Stat = {
  value: string;
  label: string;
  source: string;
};

const HEALTH_IMPACT: Stat[] = [
  {
    value: "1 in 4",
    label:
      "hospitalized adults who died or were transferred to the ICU had a diagnostic error (23.0%); errors contributed to harm or death in nearly 1 in 5.",
    source: "Auerbach et al., JAMA Internal Medicine, 2024",
  },
  {
    value: "7.2%",
    label:
      "of general-medicine inpatients experience a harmful diagnostic error — roughly 1 in 14 patients on the ward.",
    source: "Dalal et al., BMJ Quality & Safety, 2025",
  },
  {
    value: "2.4×",
    label:
      "higher in-hospital mortality when the discharge diagnosis differs from admission (8.6% vs 3.8%), alongside ~3.4 additional days of stay.",
    source: "Hautz et al., Scand J Trauma Resusc Emerg Med, 2019",
  },
  {
    value: "~795,000",
    label:
      "Americans suffer death or permanent disability from diagnostic error every year.",
    source: "Newman-Toker et al., BMJ Quality & Safety, 2024",
  },
];

const FINANCIAL_IMPACT: Stat[] = [
  {
    value: "$33,000",
    label:
      "in added cost per sepsis case when it is not recognized on admission ($51,022 vs $18,023).",
    source: "Paoli et al., Critical Care Medicine, 2018",
  },
  {
    value: "$1,795",
    label:
      "in excess cost per hospitalization for acute kidney injury after risk adjustment, plus longer length of stay.",
    source: "Silver et al., Journal of Hospital Medicine, 2017",
  },
  {
    value: "68%",
    label:
      "of acute kidney injury goes undetected in hospitalized patients — a condition the labs already point to.",
    source: "Esposito et al., Clinical Kidney Journal, 2024",
  },
  {
    value: "$54.6B",
    label:
      "nearly half of US Medicare inpatient spending rides on the highest-severity flag — capture that often hinges on documentation.",
    source: "HHS Office of Inspector General, 2021",
  },
];

function StatGrid({ stats }: { stats: Stat[] }) {
  return (
    <div className="mt-8 grid gap-px overflow-hidden rounded-2xl border border-border bg-border sm:grid-cols-2">
      {stats.map((stat) => (
        <div key={stat.source} className="flex flex-col bg-background p-7">
          <p className="text-4xl font-semibold tracking-tight text-accent-strong">
            {stat.value}
          </p>
          <p className="mt-3 flex-1 leading-relaxed text-foreground">
            {stat.label}
          </p>
          <p className="mt-4 text-xs leading-snug text-muted">{stat.source}</p>
        </div>
      ))}
    </div>
  );
}

export function Evidence() {
  return (
    <section id="evidence" className="border-t border-border">
      <div className="mx-auto max-w-6xl px-6 py-24">
        <div className="max-w-2xl">
          <p className="mb-3 text-sm font-medium tracking-wide text-accent uppercase">
            For hospitalists
          </p>
          <h2 className="text-3xl font-semibold tracking-tight sm:text-4xl">
            The evidence is clear, and it is in the record.
          </h2>
          <p className="mt-4 text-lg leading-relaxed text-muted">
            Diagnostic error is one of the most consequential and most
            underaddressed problems in inpatient medicine — for patients and for
            the bottom line. Every figure below is drawn from peer-reviewed
            literature and government data.
          </p>
        </div>

        <div className="mt-14">
          <h3 className="text-sm font-semibold tracking-wide text-foreground uppercase">
            Health impact
          </h3>
          <StatGrid stats={HEALTH_IMPACT} />
        </div>

        <div className="mt-16">
          <h3 className="text-sm font-semibold tracking-wide text-foreground uppercase">
            Financial impact
          </h3>
          <StatGrid stats={FINANCIAL_IMPACT} />
        </div>

        <p className="mt-10 max-w-3xl text-sm leading-relaxed text-muted">
          Citations, in order: Auerbach AD, et al. <em>JAMA Intern Med</em>.
          2024;184(2):164–173. · Dalal AK, et al. <em>BMJ Qual Saf</em>.
          2025;34(6):377–388. · Hautz WE, et al. <em>Scand J Trauma Resusc Emerg
          Med</em>. 2019;27:54. · Newman-Toker DE, et al. <em>BMJ Qual Saf</em>.
          2024;33(2):109–120. · Paoli CJ, et al. <em>Crit Care Med</em>.
          2018;46:1889–1897. · Silver SA, et al. <em>J Hosp Med</em>.
          2017;12:70–76. · Esposito P, et al. <em>Clin Kidney J</em>.
          2024;17(8):sfae231. · HHS OIG. Data Brief OEI-02-18-00380, 2021.
        </p>
      </div>
    </section>
  );
}
