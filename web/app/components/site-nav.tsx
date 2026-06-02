import Link from "next/link";

export function SiteNav() {
  return (
    <header className="sticky top-0 z-50 border-b border-border bg-background/80 backdrop-blur">
      <div className="mx-auto flex h-16 max-w-6xl items-center justify-between px-6">
        <Link href="/" className="flex items-center gap-2.5">
          <span className="flex h-7 w-7 items-center justify-center rounded-md bg-accent text-sm font-bold text-white">
            T
          </span>
          <span className="text-base font-semibold tracking-tight">
            Thousand Health
          </span>
        </Link>
        <nav className="flex items-center gap-6 text-sm font-medium text-muted">
          <Link href="/#how" className="hidden hover:text-foreground sm:block">
            How it works
          </Link>
          <Link href="/#evidence" className="hidden hover:text-foreground sm:block">
            Evidence
          </Link>
          <Link href="/#approach" className="hidden hover:text-foreground sm:block">
            Approach
          </Link>
          <a
            href="mailto:tomo@thousandhealth.com"
            className="rounded-full bg-accent px-4 py-2 text-white transition-colors hover:bg-accent-strong"
          >
            Contact
          </a>
        </nav>
      </div>
    </header>
  );
}
