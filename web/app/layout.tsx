import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  metadataBase: new URL("https://thousandhealth.com"),
  title: {
    default: "Thousand Health — AI diagnostic copilot",
    template: "%s — Thousand Health",
  },
  description:
    "Thousand Health reads the full clinical record to surface diagnoses that are supported by the data but never formally made — so clinicians and health systems catch what was missed.",
  keywords: [
    "AI diagnosis",
    "diagnostic copilot",
    "clinical decision support",
    "missed diagnoses",
    "health system AI",
  ],
  openGraph: {
    title: "Thousand Health — AI diagnostic copilot",
    description:
      "Surface diagnoses that are supported by the data but never formally made.",
    url: "https://thousandhealth.com",
    siteName: "Thousand Health",
    type: "website",
  },
  icons: {
    icon: [
      { url: "/favicon.ico", sizes: "any" },
      { url: "/favicon-32x32.png", type: "image/png", sizes: "32x32" },
      { url: "/favicon-16x16.png", type: "image/png", sizes: "16x16" },
      { url: "/icon-192.png", type: "image/png", sizes: "192x192" },
      { url: "/icon-512.png", type: "image/png", sizes: "512x512" },
    ],
    apple: "/apple-touch-icon.png",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
