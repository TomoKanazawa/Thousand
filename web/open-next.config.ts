import { defineCloudflareConfig } from "@opennextjs/cloudflare";

// Default Cloudflare Workers config. When we add features that need caching
// (ISR, fetch cache) or other bindings, configure them here — e.g. an R2/KV
// incremental cache. Empty config is the supported baseline.
export default defineCloudflareConfig();
