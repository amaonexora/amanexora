#!/usr/bin/env python3
"""Validate the committed AMA.NexOra source package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parent
WEBSITE = ROOT / "website"
errors: list[str] = []

required = [
    ROOT / "COMPLETE_MANIFEST.txt",
    ROOT / "README_START_HERE.txt",
    WEBSITE / "index.html",
    WEBSITE / "styles.css",
    WEBSITE / "script.js",
    WEBSITE / "manifest.webmanifest",
    WEBSITE / "robots.txt",
    WEBSITE / "assets/04_AMA.NexOra_Horizontal_Dark.svg",
    WEBSITE / "assets/06_AMA.NexOra_Icon_Only.svg",
    WEBSITE / "assets/08_AMA.NexOra_Favicon.svg",
]

for path in required:
    if not path.is_file():
        errors.append(f"Missing required file: {path.relative_to(ROOT)}")

for path in ROOT.rglob("*.svg"):
    try:
        ElementTree.parse(path)
    except ElementTree.ParseError as exc:
        errors.append(f"Invalid SVG {path.relative_to(ROOT)}: {exc}")

manifest_path = WEBSITE / "manifest.webmanifest"
manifest: dict = {}
if manifest_path.is_file():
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid web manifest: {exc}")

icons = manifest.get("icons", [])
if not icons:
    errors.append("Web manifest must declare at least one icon.")
for icon in icons:
    source = icon.get("src")
    if not source:
        errors.append("Web manifest icon is missing src.")
    elif not (WEBSITE / source).is_file():
        errors.append(f"Missing web manifest icon: {source}")

index_path = WEBSITE / "index.html"
if index_path.is_file():
    html = index_path.read_text(encoding="utf-8")
    references = re.findall(r'(?:src|href)="([^"]+)"', html)
    for reference in references:
        if reference.startswith(("#", "http://", "https://", "mailto:", "tel:", "data:")):
            continue
        target = (WEBSITE / reference.split("#", 1)[0].split("?", 1)[0]).resolve()
        if not target.is_file():
            errors.append(f"Broken local HTML reference: {reference}")

    if 'rel="icon"' not in html:
        errors.append("index.html does not declare a favicon.")

dark_logo = WEBSITE / "assets/04_AMA.NexOra_Horizontal_Dark.svg"
if dark_logo.is_file() and 'fill="#fff"' not in dark_logo.read_text(encoding="utf-8"):
    errors.append("Dark-background logo does not contain a white foreground treatment.")

if errors:
    print("AMA.NexOra brand package validation failed:")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)

svg_count = sum(1 for _ in ROOT.rglob("*.svg"))
print(f"AMA.NexOra brand package validation passed ({svg_count} SVG files checked).")
