import type { Metadata } from "next";
import { SiteNav } from "../components/site-nav";
import { SiteFooter } from "../components/site-footer";

export const metadata: Metadata = {
  title: "Privacy Policy",
  description:
    "How Thousand Health collects, uses, and protects information through its website.",
};

const LAST_UPDATED = "June 2, 2026";

export default function PrivacyPage() {
  return (
    <div className="flex min-h-screen flex-col">
      <SiteNav />
      <main className="flex-1">
        <div className="mx-auto max-w-3xl px-6 py-20">
          <h1 className="text-4xl font-semibold tracking-tight">
            Privacy Policy
          </h1>
          <p className="mt-3 text-sm text-muted">Last updated: {LAST_UPDATED}</p>

          <div className="prose-legal mt-10">
            <p>
              This Privacy Policy explains how Thousand Health, Inc.
              (&ldquo;Thousand Health,&rdquo; &ldquo;we,&rdquo; &ldquo;us,&rdquo;
              or &ldquo;our&rdquo;) collects, uses, and protects information in
              connection with the website at thousandhealth.com (the
              &ldquo;Site&rdquo;). This policy applies to the Site only. Our
              handling of protected health information on behalf of healthcare
              customers is governed by separate agreements, described in Section
              5 below.
            </p>

            <h2>1. Information we collect</h2>
            <p>We may collect the following through the Site:</p>
            <ul>
              <li>
                <strong>Information you provide.</strong> If you email us or fill
                out a contact form, we collect the information you choose to
                share, such as your name, email address, organization, and the
                contents of your message.
              </li>
              <li>
                <strong>Usage information.</strong> We may automatically collect
                limited technical information such as your browser type, device,
                referring pages, and general interaction with the Site.
              </li>
            </ul>

            <h2>2. How we use information</h2>
            <p>We use the information we collect to:</p>
            <ul>
              <li>Respond to your inquiries and communicate with you;</li>
              <li>Operate, maintain, and improve the Site;</li>
              <li>
                Understand how visitors use the Site so we can improve it; and
              </li>
              <li>Comply with legal obligations and protect our rights.</li>
            </ul>

            <h2>3. Cookies and analytics</h2>
            <p>
              The Site may use cookies or similar technologies and privacy-
              conscious analytics to understand aggregate usage. You can control
              cookies through your browser settings. Disabling cookies may affect
              certain features of the Site.
            </p>

            <h2>4. How we share information</h2>
            <p>
              We do not sell your personal information. We may share information
              with service providers who help us operate the Site (such as
              hosting and analytics providers) under appropriate confidentiality
              obligations, and where required by law or to protect our legal
              rights.
            </p>

            <h2>5. Protected health information (PHI)</h2>
            <p>
              The Site is not intended for the submission of patient health
              information. Please do not send protected health information
              through the Site&rsquo;s contact channels. When Thousand Health
              processes protected health information on behalf of a covered
              entity or business associate as part of delivering its products, it
              does so under a Business Associate Agreement and applicable law,
              including HIPAA. That processing is governed by those agreements,
              not by this Site Privacy Policy.
            </p>

            <h2>6. Data security</h2>
            <p>
              We use reasonable administrative, technical, and physical
              safeguards designed to protect information we hold. No method of
              transmission or storage is completely secure, however, and we
              cannot guarantee absolute security.
            </p>

            <h2>7. Your choices</h2>
            <p>
              You may opt out of receiving non-essential communications from us
              at any time by contacting us. Depending on your location, you may
              have rights to access, correct, or delete personal information we
              hold about you; to exercise these rights, contact us using the
              details below.
            </p>

            <h2>8. Children&rsquo;s privacy</h2>
            <p>
              The Site is not directed to children under 13, and we do not
              knowingly collect personal information from children under 13.
            </p>

            <h2>9. Changes to this policy</h2>
            <p>
              We may update this Privacy Policy from time to time. The most
              current version will be posted on this page with the &ldquo;Last
              updated&rdquo; date.
            </p>

            <h2>10. Contact</h2>
            <p>
              If you have questions about this Privacy Policy, contact us at{" "}
              <a href="mailto:tomo@thousandhealth.com">
                tomo@thousandhealth.com
              </a>
              .
            </p>
          </div>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
