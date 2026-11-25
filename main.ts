/**
 * Spotlight @crisxai5: AI & Crypto Expert on X.
 *
 * Writes the published X post URL to /output/POST.json for the make.fun
 * bounty "Spotlight @crisxai5: AI & Crypto Expert on X".
 * The post was published from @CUNGYIOOOO introducing @crisxai5 as a
 * must-follow voice in AI and crypto.
 */

import { mkdirSync, writeFileSync } from "node:fs";

// The published X post introducing @crisxai5, posted from @CUNGYIOOOO.
const PUBLISHED_POST_URL =
  "https://x.com/CUNGYIOOOO/status/2125565342395081096";

function buildPayload(): { url: string } {
  return { url: PUBLISHED_POST_URL };
}

function main(): void {
  const payload = buildPayload();
  mkdirSync("/output", { recursive: true });
  const text = `{"url": "${payload.url}"}\n`;
  writeFileSync("/output/POST.json", text, "utf-8");
  console.log(`Wrote /output/POST.json: ${JSON.stringify(payload)}`);
}

main();
