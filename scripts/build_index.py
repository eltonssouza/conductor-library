#!/usr/bin/env python3
"""Generate the library catalog so Conductor can always see what's available.

Single source of truth: the YAML frontmatter of every content `.md` file
(`software_dev` tier, plus `stack`/`version` for stack books). This script scans
the numbered topic folders and emits two artifacts, both deterministic (no
timestamps, stable sort) so re-runs produce clean git diffs:

  - LIBRARY_INDEX.json  — machine-readable manifest the Conductor app consumes
                          (per-category files + a stacks/versions map for
                          `stack@major` edition selection).
  - README.md           — the human navigable index, regenerated between the
                          AUTO-INDEX markers (the intro above them is manual).

Usage:
    python scripts/build_index.py            # write artifacts
    python scripts/build_index.py --check     # verify they are up to date (CI)

Run from anywhere; paths are resolved relative to the repo root.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Display titles for each numbered topic folder, keyed by the NN prefix.
CATEGORY_TITLES = {
    "00": "Academic Curriculum (reading lists)",
    "01": "Programming Languages",
    "02": "Algorithms & Data Structures",
    "03": "Software Design & Architecture",
    "04": "Software Engineering & Practices",
    "05": "Databases & Data",
    "06": "Web & Frontend",
    "07": "DevOps, SRE & Operations",
    "08": "Distributed Systems & Microservices",
    "09": "Security & Privacy",
    "10": "AI & LLM",
    "11": "Management, Product & Process",
    "12": "Design & UX",
    "13": "Automation & Integration",
    "14": "Frameworks",
}

FOLDER_RE = re.compile(r"^(\d{2})_")
START_MARKER = "<!-- AUTO-INDEX:START -->"
END_MARKER = "<!-- AUTO-INDEX:END -->"


def parse_frontmatter(text: str) -> dict[str, str]:
    """Return the leading YAML frontmatter as a flat dict of scalar values."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip()
    return data


def url_path(rel_path: str) -> str:
    """Encode a repo-relative path the way the README links do: space and # only."""
    return rel_path.replace("%", "%25").replace(" ", "%20").replace("#", "%23")


def collect() -> list[dict]:
    """Walk the numbered topic folders and return one record per content file."""
    categories: list[dict] = []
    for folder in sorted(p for p in REPO_ROOT.iterdir() if p.is_dir() and FOLDER_RE.match(p.name)):
        nn = folder.name[:2]
        files = []
        for md in sorted(folder.glob("*.md"), key=lambda p: p.name):
            fm = parse_frontmatter(md.read_text(encoding="utf-8"))
            rel = f"{folder.name}/{md.name}"
            record = {
                "path": rel,
                "title": md.stem,
                "tier": fm.get("software_dev"),
            }
            if fm.get("stack"):
                record["stack"] = fm["stack"]
            if fm.get("version"):
                try:
                    record["version"] = int(fm["version"])
                except ValueError:
                    record["version"] = fm["version"]
            files.append(record)
        if files:
            categories.append(
                {
                    "id": folder.name,
                    "number": nn,
                    "title": CATEGORY_TITLES.get(nn, folder.name),
                    "files": files,
                }
            )
    return categories


def build_stacks(categories: list[dict]) -> dict:
    """Group stack books by id, exposing the versions available for selection."""
    stacks: dict[str, dict] = {}
    for cat in categories:
        for f in cat["files"]:
            sid = f.get("stack")
            if not sid:
                continue
            entry = stacks.setdefault(sid, {"versions": [], "editions": []})
            edition = {"path": f["path"], "title": f["title"]}
            if "version" in f:
                edition["version"] = f["version"]
                if f["version"] not in entry["versions"]:
                    entry["versions"].append(f["version"])
            entry["editions"].append(edition)
    for entry in stacks.values():
        entry["versions"].sort(key=lambda v: (isinstance(v, str), v))
        entry["editions"].sort(key=lambda e: (e.get("version", 0), e["title"]))
    return dict(sorted(stacks.items()))


def build_manifest(categories: list[dict], stacks: dict) -> dict:
    total = sum(len(c["files"]) for c in categories)
    return {
        "schema": "conductor-library-index/v1",
        "totals": {
            "files": total,
            "categories": len(categories),
            "stacks": len(stacks),
        },
        "categories": categories,
        "stacks": stacks,
    }


def render_readme_index(categories: list[dict]) -> str:
    """Render the markdown catalog placed between the AUTO-INDEX markers."""
    lines: list[str] = []
    lines.append("> **Generated by `scripts/build_index.py` — do not edit by hand.** "
                 "It mirrors [LIBRARY_INDEX.json](LIBRARY_INDEX.json), the machine-readable "
                 "catalog Conductor consumes.")
    lines.append("")
    for cat in categories:
        lines.append(f"## {cat['number']} · {cat['title']}")
        lines.append("")
        for f in cat["files"]:
            lines.append(f"- [{f['title']}]({url_path(f['path'])})")
        lines.append("")
    total = sum(len(c["files"]) for c in categories)
    lines.append("---")
    lines.append("")
    lines.append(f"**Total: {total} book/reading-list files**")
    return "\n".join(lines)


def update_readme(readme_text: str, index_md: str) -> str:
    block = f"{START_MARKER}\n\n{index_md}\n\n{END_MARKER}"
    if START_MARKER in readme_text and END_MARKER in readme_text:
        pre = readme_text[: readme_text.index(START_MARKER)]
        post = readme_text[readme_text.index(END_MARKER) + len(END_MARKER):]
        return f"{pre}{block}{post}"
    # Bootstrap: replace from the first generated heading onward, keep the intro.
    anchor = readme_text.find("## 00 ")
    pre = readme_text[:anchor] if anchor != -1 else readme_text.rstrip() + "\n\n"
    return f"{pre}{block}\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if artifacts are stale (for CI)")
    args = ap.parse_args()

    categories = collect()
    stacks = build_stacks(categories)
    manifest = build_manifest(categories, stacks)

    json_path = REPO_ROOT / "LIBRARY_INDEX.json"
    readme_path = REPO_ROOT / "README.md"

    new_json = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    new_readme = update_readme(readme_path.read_text(encoding="utf-8"),
                               render_readme_index(categories))

    if args.check:
        stale = []
        if json_path.read_text(encoding="utf-8") != new_json:
            stale.append("LIBRARY_INDEX.json")
        if readme_path.read_text(encoding="utf-8") != new_readme:
            stale.append("README.md")
        if stale:
            print("STALE: " + ", ".join(stale) + " — run: python scripts/build_index.py")
            return 1
        print("Index up to date.")
        return 0

    json_path.write_text(new_json, encoding="utf-8")
    readme_path.write_text(new_readme, encoding="utf-8")
    print(f"Wrote LIBRARY_INDEX.json and README.md "
          f"({manifest['totals']['files']} files, "
          f"{manifest['totals']['categories']} categories, "
          f"{manifest['totals']['stacks']} stacks).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
