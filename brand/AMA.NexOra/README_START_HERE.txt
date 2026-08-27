AMA.NexOra — BRAND SOURCE PACKAGE
====================================

START HERE

This directory contains the editable AMA.NexOra identity sources and a static landing-page concept.

FOLDERS
- svg/       Master vector logos for design, web, print, and scalable export.
- website/   Responsive landing page with self-contained website assets.
- social/    Editable SVG templates sized for major social platforms.
- print/     Editable A4 letterhead source.

WEBSITE QUICK START
1. Open website/index.html in a modern browser.
2. For local development, serve the website directory with a static server.
3. Before production deployment, confirm the contact address, domain, legal pages,
   analytics, and deployment headers for the target environment.

QUALITY CHECK
Run this command from the repository root:

python brand/AMA.NexOra/validate_brand_package.py

The check validates:
- SVG and web-manifest syntax
- Required website files
- Local HTML asset references
- Favicon and PWA icon configuration
- Presence of a dark-background horizontal logo

BRAND COLORS
Deep Navy     #0A1F44
Electric Blue #009DFF
Violet        #7B4DFF
Silver        #C8CCD6

EXPORTS
This Git repository is the editable source package. Raster and document exports
(PNG, PDF, EPS, JPG, ICO, guidelines, and rendered mockups) must be produced and
published separately as a versioned release.

AMA.NexOra
Premium Technology · AI · Cybersecurity · Intelligent Systems · Digital Innovation
