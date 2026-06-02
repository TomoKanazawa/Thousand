import type { Metadata } from "next";
import { SiteNav } from "../components/site-nav";
import { SiteFooter } from "../components/site-footer";

export const metadata: Metadata = {
  title: "Terms of Use",
  description: "The terms governing your use of the Thousand Health website.",
};

const LAST_UPDATED = "June 2, 2026";

export default function TermsPage() {
  return (
    <div className="flex min-h-screen flex-col">
      <SiteNav />
      <main className="flex-1">
        <div className="mx-auto max-w-3xl px-6 py-20">
          <h1 className="text-4xl font-semibold tracking-tight">
            Terms of Use
          </h1>
          <p className="mt-3 text-sm text-muted">Last updated: {LAST_UPDATED}</p>

          <div className="prose-legal mt-10">
            <p>
              These Terms of Use (&ldquo;Terms&rdquo;) govern your access to and
              use of the website located at thousandhealth.com (the
              &ldquo;Site&rdquo;), operated by Thousand Health, Inc.
              (&ldquo;Thousand Health,&rdquo; &ldquo;we,&rdquo; &ldquo;us,&rdquo;
              or &ldquo;our&rdquo;). By accessing or using the Site, you agree to
              be bound by these Terms. If you do not agree, do not use the Site.
            </p>

            <h2>1. Informational purpose only</h2>
            <p>
              The Site provides general information about Thousand Health and its
              products and services. Nothing on the Site constitutes medical
              advice, diagnosis, or treatment, and the Site is not a substitute
              for the judgment of a qualified healthcare professional. Thousand
              Health&rsquo;s products are intended as clinical decision support
              and do not replace the independent judgment of licensed clinicians,
              who remain solely responsible for all diagnostic and treatment
              decisions. Never disregard professional medical advice or delay
              seeking it because of content you read on the Site.
            </p>

            <h2>2. No reliance for clinical decisions</h2>
            <p>
              Information on the Site is provided for general informational
              purposes and may be updated or changed at any time without notice.
              You should not rely on the Site as the basis for any clinical,
              business, or other decision without independent verification.
            </p>

            <h2>3. Acceptable use</h2>
            <p>You agree not to:</p>
            <ul>
              <li>
                Use the Site in any way that violates any applicable law or
                regulation;
              </li>
              <li>
                Attempt to gain unauthorized access to the Site, its servers, or
                any associated systems or networks;
              </li>
              <li>
                Interfere with or disrupt the integrity or performance of the
                Site;
              </li>
              <li>
                Use any automated means to access the Site or collect information
                from it without our prior written permission; or
              </li>
              <li>
                Submit any personal health information of any individual through
                the Site&rsquo;s contact channels unless specifically requested
                and through a secure, agreed-upon method.
              </li>
            </ul>

            <h2>4. Intellectual property</h2>
            <p>
              The Site and its contents — including text, graphics, logos, and
              software — are owned by or licensed to Thousand Health and are
              protected by intellectual property laws. The &ldquo;Thousand
              Health&rdquo; name and logo are trademarks of Thousand Health, Inc.
              You may not use, reproduce, or distribute any content from the Site
              without our prior written consent.
            </p>

            <h2>5. Third-party links</h2>
            <p>
              The Site may contain links to third-party websites or resources. We
              provide these links for convenience only and are not responsible
              for the content, products, or services on or available from those
              websites.
            </p>

            <h2>6. Disclaimer of warranties</h2>
            <p>
              The Site is provided on an &ldquo;as is&rdquo; and &ldquo;as
              available&rdquo; basis. To the fullest extent permitted by law,
              Thousand Health disclaims all warranties, express or implied,
              including warranties of merchantability, fitness for a particular
              purpose, and non-infringement. We do not warrant that the Site will
              be uninterrupted, secure, or error-free.
            </p>

            <h2>7. Limitation of liability</h2>
            <p>
              To the fullest extent permitted by law, Thousand Health and its
              officers, directors, employees, and agents will not be liable for
              any indirect, incidental, special, consequential, or punitive
              damages arising out of or relating to your use of, or inability to
              use, the Site.
            </p>

            <h2>8. Changes to these Terms</h2>
            <p>
              We may revise these Terms from time to time. The most current
              version will always be posted on this page with the &ldquo;Last
              updated&rdquo; date. Your continued use of the Site after changes
              take effect constitutes your acceptance of the revised Terms.
            </p>

            <h2>9. Governing law</h2>
            <p>
              These Terms are governed by the laws of the State of Delaware,
              without regard to its conflict-of-laws principles.
            </p>

            <h2>10. Contact</h2>
            <p>
              If you have questions about these Terms, contact us at{" "}
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
