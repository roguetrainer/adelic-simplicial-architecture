#!/usr/bin/env python3
"""
csv_to_papers_json.py
=====================
Generate _data/papers.json from _data/papers.csv.

Usage:
    python scripts/csv_to_papers_json.py

The CSV is the master record. Edit papers.csv in Excel/Numbers,
then run this script to regenerate papers.json for the website.

CSV columns:
    number      — integer paper number (e.g. 318)
    title       — full paper title
    doi         — e.g. 10.5281/zenodo.20346650 (blank if draft)
    zenodo_id   — numeric part of DOI (auto-derived if blank)
    slug        — URL slug e.g. 10.5281-zenodo.20346650 (auto-derived if blank)
    portfolios  — pipe-separated e.g. A|B
    tags        — pipe-separated e.g. fano|g2|octonions
    explainer   — True or False
    status      — published / draft
    notes       — free text, ignored by website
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
CSV_PATH  = ROOT / "_data" / "papers.csv"
JSON_PATH = ROOT / "_data" / "papers.json"


def csv_to_json():
    papers = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            doi = row["doi"].strip()
            zenodo_id = row["zenodo_id"].strip() or (doi.replace("10.5281/zenodo.", "") if doi else "")
            slug = row["slug"].strip() or (f"10.5281-zenodo.{zenodo_id}" if zenodo_id else "")

            paper = {
                "number":     int(row["number"]),
                "title":      row["title"].strip(),
                "doi":        doi,
                "slug":       slug,
                "portfolios": [p.strip() for p in row["portfolios"].split("|") if p.strip()],
                "tags":       [t.strip() for t in row["tags"].split("|") if t.strip()],
                "explainer":  row["explainer"].strip().lower() in ("true", "1", "yes"),
            }
            papers.append(paper)

    papers.sort(key=lambda p: p["number"])

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(papers, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Written {len(papers)} papers to {JSON_PATH}")


if __name__ == "__main__":
    csv_to_json()
