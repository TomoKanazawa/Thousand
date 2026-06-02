import { SiteNav } from "./components/site-nav";
import { SiteFooter } from "./components/site-footer";
import { Evidence } from "./components/evidence";

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col">
      <SiteNav />

      <main className="flex-1">
        {/* Hero */}
        <section className="relative overflow-hidden">
          <div className="pointer-events-none absolute inset-0 bg-[radial-gradient(60%_60%_at_50%_0%,rgba(14,124,134,0.10),transparent)]" />
          <div className="mx-auto max-w-6xl px-6 py-24 sm:py-32">
            <div className="mx-auto max-w-3xl text-center">
              <p className="mb-5 inline-flex items-center rounded-full border border-border bg-surface px-3 py-1 text-xs font-medium tracking-wide text-accent-strong uppercase">
                AI diagnostic copilot
              </p>
              <h1 className="text-balance text-4xl font-semibold leading-tight tracking-tight sm:text-6xl">
                Catch the diagnoses that were missed.
              </h1>
              <p className="mx-auto mt-6 max-w-2xl text-balance text-lg leading-relaxed text-muted sm:text-xl">
                Thousand Health reads the full clinical record and surfaces
                conditions that are supported by the data but never formally
                diagnosed — putting the evidence in front of the clinician who
                decides.
              </p>
              <div className="mt-9 flex flex-col items-center justify-center gap-3 sm:flex-row">
                <a
                  href="mailto:tomo@thousandhealth.com"
                  className="flex h-12 w-full items-center justify-center rounded-full bg-accent px-7 text-base font-medium text-white transition-colors hover:bg-accent-strong sm:w-auto"
                >
                  Request a demo
                </a>
                <a
                  href="#how"
                  className="flex h-12 w-full items-center justify-center rounded-full border border-border px-7 text-base font-medium text-foreground transition-colors hover:bg-surface sm:w-auto"
                >
                  See how it works
                </a>
              </div>
            </div>
          </div>
        </section>

        {/* Problem */}
        <section className="border-y border-border bg-surface">
          <div className="mx-auto grid max-w-6xl gap-10 px-6 py-16 sm:grid-cols-3">
            {[
              {
                stat: "Every record",
                label:
                  "The signals of a missed diagnosis are usually already in the chart — in labs, trends, and notes.",
              },
              {
                stat: "Not acted on",
                label:
                  "Conditions that are clinically supported often go unrecorded, so they are never treated or coded.",
              },
              {
                stat: "Clinician-led",
                label:
                  "Thousand Health flags what deserves a second look. The clinician always makes the call.",
              },
            ].map((item) => (
              <div key={item.stat}>
                <p className="text-xl font-semibold tracking-tight text-accent-strong">
                  {item.stat}
                </p>
                <p className="mt-2 leading-relaxed text-muted">{item.label}</p>
              </div>
            ))}
          </div>
        </section>

        {/* How it works */}
        <section id="how" className="mx-auto max-w-6xl px-6 py-24">
          <div className="max-w-2xl">
            <h2 className="text-3xl font-semibold tracking-tight sm:text-4xl">
              How it works
            </h2>
            <p className="mt-4 text-lg leading-relaxed text-muted">
              A focused pipeline that reads what is already there and reasons
              about what it means.
            </p>
          </div>
          <div className="mt-14 grid gap-8 md:grid-cols-3">
            {[
              {
                step: "01",
                title: "Read the record",
                body: "Ingests structured and unstructured EHR data — labs, vitals, medications, and clinical notes — at the moment a decision is being made.",
              },
              {
                step: "02",
                title: "Reason over the evidence",
                body: "Identifies conditions that the data supports against established clinical criteria, including ones that were never written down.",
              },
              {
                step: "03",
                title: "Surface for review",
                body: "Presents each candidate with the evidence behind it, so the care team can confirm, act, or dismiss in seconds.",
              },
            ].map((item) => (
              <div
                key={item.step}
                className="rounded-2xl border border-border bg-background p-7"
              >
                <span className="font-mono text-sm font-medium text-accent">
                  {item.step}
                </span>
                <h3 className="mt-3 text-xl font-semibold tracking-tight">
                  {item.title}
                </h3>
                <p className="mt-3 leading-relaxed text-muted">{item.body}</p>
              </div>
            ))}
          </div>
        </section>

        {/* Evidence */}
        <Evidence />

        {/* Approach */}
        <section id="approach" className="border-t border-border bg-surface">
          <div className="mx-auto max-w-6xl px-6 py-24">
            <div className="max-w-2xl">
              <h2 className="text-3xl font-semibold tracking-tight sm:text-4xl">
                Built for clinical trust
              </h2>
              <p className="mt-4 text-lg leading-relaxed text-muted">
                A diagnostic tool only earns adoption if clinicians can trust
                it. That principle shapes every decision we make.
              </p>
            </div>
            <div className="mt-14 grid gap-px overflow-hidden rounded-2xl border border-border bg-border sm:grid-cols-2">
              {[
                {
                  title: "Evidence-grounded",
                  body: "Every flag is traceable to the data and criteria behind it. No black-box conclusions — clinicians see why.",
                },
                {
                  title: "Decision support, not a decision",
                  body: "Thousand Health surfaces possibilities. The clinician remains the diagnostician and the final authority.",
                },
                {
                  title: "Privacy by design",
                  body: "Protected health information is handled under strict access controls and used only to serve the patient's care.",
                },
                {
                  title: "Fits the workflow",
                  body: "Designed to meet care teams where they already work, rather than adding another system to check.",
                },
              ].map((item) => (
                <div key={item.title} className="bg-background p-8">
                  <h3 className="text-lg font-semibold tracking-tight">
                    {item.title}
                  </h3>
                  <p className="mt-2 leading-relaxed text-muted">{item.body}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* CTA */}
        <section className="mx-auto max-w-6xl px-6 py-24">
          <div className="rounded-3xl bg-foreground px-8 py-16 text-center sm:px-16">
            <h2 className="text-balance text-3xl font-semibold tracking-tight text-white sm:text-4xl">
              See it on your data.
            </h2>
            <p className="mx-auto mt-4 max-w-xl text-balance leading-relaxed text-white/70">
              We work with clinicians, health systems, and payers to find the
              diagnoses hiding in their records. Reach out for a conversation.
            </p>
            <div className="mt-8">
              <a
                href="mailto:tomo@thousandhealth.com"
                className="inline-flex h-12 items-center justify-center rounded-full bg-white px-7 text-base font-medium text-foreground transition-colors hover:bg-white/90"
              >
                tomo@thousandhealth.com
              </a>
            </div>
          </div>
        </section>
      </main>

      <SiteFooter />
    </div>
  );
}
