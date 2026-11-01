# Tableau workbook build guide

This folder describes the workbook to build in Tableau Desktop or Tableau Public. A Tableau workbook file is not auto-generated because Tableau must create and validate its own workbook format in the Tableau application.

## Connect data
1. Open Tableau.
2. Connect to Text File and choose `data/processed/athletes_events.csv`.
3. Add `data/processed/sports_investment.csv` as a second data source.
4. For cross-source comparisons, relate on year, country_code, country, region and season where applicable. Check join cardinality to avoid duplicated medal totals.
5. Keep a note on the data source page that the included data is synthetic demo data until replaced.

## Calculated fields
**Won Medal**
```tableau
[medal] = "Gold" OR [medal] = "Silver" OR [medal] = "Bronze"
```
**Medal Entry**
```tableau
IF [Won Medal] THEN 1 ELSE 0 END
```
**Medal Efficiency %**
```tableau
SUM([Medal Entry]) / COUNT([athlete_id]) * 100
```
**Investment Efficiency**
```tableau
SUM([total_medals]) / SUM([sports_investment_usd_millions])
```
If your Tableau data model does not contain a country/year aggregate `total_medals`, create an aggregate table first and relate it carefully. Avoid joining raw athlete rows directly to a repeated country/year investment value because that inflates investment totals.

## Dashboard 1 — Olympic Performance Overview
- KPI tiles: athlete-event entries, countries, sports, medal entries.
- Line chart: year vs medal entries, color by season.
- Horizontal bars: medal entries by country.
- Horizontal bars: medal entries by sport.
- Filters: year, season, country, region.
- Add a note defining medal entries and explaining that team medals may be represented differently by source.

## Dashboard 2 — Investment and Regional Efficiency
- Scatter/bubble plot: investment on X, medal entries on Y, country as detail, region as color.
- Bar chart: medal efficiency by region.
- Table: country, year, season, investment, medals, efficiency.
- Add an explicit note: correlation does not establish causation.

## Dashboard 3 — Olympic Story
Suggested story points:
1. Overall medal trend.
2. Country-level comparisons.
3. Sport category differences.
4. Regional distribution.
5. Investment-efficiency caveats and conclusions.
Use story captions to state what each chart shows and its limitations.

## Publish and embed
- Save the workbook.
- Publish to Tableau Public only if the data is safe and permitted to be public.
- Copy the official embed snippet from Tableau's Share/Embed options.
- Add it to `templates/tableau.html` inside the embed panel.
- For a private Tableau Server/Cloud deployment, follow the institution's authentication policy.
