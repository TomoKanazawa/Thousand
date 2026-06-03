import Link from "next/link";

export function SiteFooter() {
  return (
    <footer className="border-t border-border bg-surface">
      <div className="mx-auto flex max-w-6xl flex-col gap-6 px-6 py-10 sm:flex-row sm:items-center sm:justify-between">
        <div className="flex items-center gap-2.5">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src="/logo-1000.svg" alt="1000" className="h-6 w-6" />
          <span className="text-sm font-semibold">Thousand Health</span>
        </div>
        <nav className="flex flex-wrap items-center gap-x-6 gap-y-2 text-sm text-muted">
          <Link href="/terms" className="hover:text-foreground">
            Terms of Use
          </Link>
          <Link href="/privacy" className="hover:text-foreground">
            Privacy Policy
          </Link>
          <a
            href="mailto:tomo@thousandhealth.com"
            className="hover:text-foreground"
          >
            Contact
          </a>
        </nav>
        <p className="text-xs text-muted">
          © {new Date().getFullYear()} Thousand Health, Inc.
        </p>
      </div>
    </footer>
  );
}
