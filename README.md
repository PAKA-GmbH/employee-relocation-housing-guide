# PAKA GmbH — Employee Relocation Housing Guide

A research-backed resource hub for PAKA GmbH to support international employees relocating to German cities.

---

## Available Guides

| City | Budget | Language | Last Updated | Status |
|------|--------|----------|--------------|--------|
| [Stuttgart](./stuttgart/) | €300–500/month | EN | March 2026 | ✅ Complete |
| [Nürnberg](./nuremberg/) | €600 (1 room) / €1,000 (2 rooms) | EN | March 2026 | ✅ Complete |

---

## What's in Each Guide

Each city guide contains:

- **Market Reality Check** — what budget actually buys in that city
- **Short-term strategy** — how to find housing fast (< 4 weeks)
- **Wohnheime & residences** — youth/worker dormitories with contacts and prices
- **Social organizations** — free support services, migration counseling
- **Mid-term strategy** — building SCHUFA, application documents, WG tips
- **Long-term strategy** — cooperatives, social housing, permanent solutions
- **Online portals** — all relevant platforms with direct links
- **Best neighborhoods** for budget renters
- **Community-specific section** — e.g. Moroccan/North African community in Stuttgart
- **Documents checklist** — Bewerbungsmappe, SCHUFA, Mietschuldenfreiheitsbescheinigung
- **PAKA GmbH action sequence** — step-by-step SOP for HR onboarding

---

## How to Use

### For a candidate arriving in Stuttgart:
1. Share the PDF: [`stuttgart/Stuttgart_Housing_Guide_PAKA_GmbH.pdf`](./stuttgart/Stuttgart_Housing_Guide_PAKA_GmbH.pdf)
2. Follow the **PAKA GmbH Action Sequence** (Section 15 of the guide)
3. Prepare the employer confirmation letter (template in `/templates/`)

### For a candidate arriving in Nürnberg:
1. Share the PDF: [`nuremberg/Nuernberg_Housing_Guide.pdf`](./nuremberg/Nuernberg_Housing_Guide.pdf)
2. Guide includes employer letter template the candidate can give directly to their employer (Section 9)
3. Key immediate actions: apply for WBS, join a cooperative, set up IS24 alerts

### For a new city:
1. Copy [`templates/city-housing-guide-template.md`](./templates/city-housing-guide-template.md)
2. Fill in city-specific research (use the Stuttgart guide as the benchmark for depth)
3. Generate PDF using [`templates/generate_pdf.py`](./templates/generate_pdf.py)
4. Add entry to the table above

---

## For Candidates

Key advice for any international worker relocating to a German city:

1. **Book bridge housing before you arrive** — don't arrive without an address
2. **Complete Anmeldung within 14 days** — mandatory address registration
3. **Open a German bank account on Day 1** — N26 works online, no local address needed
4. **Build SCHUFA patiently** — it takes 2–3 months; substitute with an employer confirmation letter (Arbeitgeberbescheinigung) from your direct employer
5. **Apply to Jugendwohnheime first** (Stuttgart) — most affordable; designed for international youth
6. **Join a cooperative early** — waiting lists run in parallel with your search; lifetime tenancy and below-market rents

---

## Repository Structure

```
employee-relocation-housing-guide/
├── README.md                          ← this file
├── stuttgart/
│   ├── stuttgart-housing-guide.md                ← full research in markdown
│   ├── Stuttgart_Housing_Guide_PAKA_GmbH.pdf     ← formatted PDF report
│   └── Stuttgart_Housing_Guide_PAKA_GmbH.html    ← HTML source for PDF
├── nuremberg/
│   ├── nuremberg-housing-guide.md                ← full research in markdown
│   ├── Nuernberg_Housing_Guide.pdf               ← formatted PDF report
│   └── Nuernberg_Housing_Guide.html              ← HTML source for PDF
└── templates/
    ├── city-housing-guide-template.md ← blank template for new cities
    ├── employer-confirmation-letter.md← PAKA GmbH letter for candidates
    ├── bewerbungsmappe-checklist.md   ← application folder checklist
    ├── pdf-style.css                  ← PDF styling
    └── generate_pdf.py                ← PDF generator script
```

---

*Maintained by PAKA GmbH — HR & Relocation Team*
*Research: March 2026 | Next review: March 2027*
