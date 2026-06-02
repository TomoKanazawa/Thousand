import type { NextConfig } from "next";
import path from "node:path";

const nextConfig: NextConfig = {
  // Pin the workspace root so Next doesn't infer a stray parent lockfile.
  turbopack: {
    root: path.join(__dirname),
  },
};

export default nextConfig;

// Enable Cloudflare bindings (KV, R2, D1, env, etc.) during `next dev`,
// so server code can use getCloudflareContext() locally just like in production.
import { initOpenNextCloudflareForDev } from "@opennextjs/cloudflare";
initOpenNextCloudflareForDev();
