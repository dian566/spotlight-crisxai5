#!/usr/bin/env python3
"""Spotlight @crisxai5: AI & Crypto Expert on X.

Writes the published X post URL to /output/POST.json for the make.fun
bounty "Spotlight @crisxai5: AI & Crypto Expert on X".
The post was published from @CUNGYIOOOO introducing @crisxai5 as a
must-follow voice in AI and crypto.
"""

import json
import os

# The published X post introducing @crisxai5, posted from @CUNGYIOOOO.
PUBLISHED_POST_URL = "https://x.com/CUNGYIOOOO/status/2125565342395081096"


def build_payload() -> dict:
    return {"url": PUBLISHED_POST_URL}


def main() -> None:
    payload = build_payload()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "POST.json")
    with open(target, "w", encoding="utf-8") as handle:
        json.dump(payload, handle)
        handle.write("\n")
    print(f"Wrote {target}: {payload}")


if __name__ == "__main__":
    main()
