# Data sources, validation and limitations

## Included files
| File | Purpose | Status |
|---|---|---|
| `athletes_events_demo.csv` | Athlete-event rows, country, sport, year, season and medal outcome | Synthetic demo |
| `medal_results_demo.csv` | Aggregate medal entries by year/country/sport/medal | Derived from synthetic demo |
| `sports_investment_demo.csv` | Country/year/season investment field for efficiency analysis | Synthetic fictional amounts |

## Official data replacement plan
Before making claims about real Olympic performance, obtain a dataset from an authoritative or appropriately licensed source, for example:
- The International Olympic Committee's official results and reports.
- The Olympic Studies Centre / Olympic World Library resources.
- A well-documented public historical athlete-event dataset, after checking its license, coverage, and known limitations.
- Government or sports agency reports for actual investment amounts, with clear currency, fiscal year and scope.

Do not assume athlete-event datasets contain a row for every athlete in every event. Do not assume 2026 has Summer Games: Milano Cortina 2026 is a Winter edition; the next Summer Games are scheduled for 2028. Validate the exact event coverage of the source you choose.

## Data quality checks to document
1. Missing year, country, sport, season or medal status.
2. Duplicate event/athlete rows.
3. Country-code changes and historical delegations.
4. Medal values outside Gold, Silver, Bronze and No Medal.
5. Whether team medals count once per team or once per athlete.
6. Whether totals refer to medals, medal-winning events, or athlete medal entries.
7. Missing investment values and currency/inflation adjustments.
8. Comparability between Summer and Winter Games.

## Important interpretation warning
A high medal-to-investment ratio does not prove that funding caused success. Medal opportunities, population, qualification, sport mix, host effects, historical development, and data coverage are confounders. Present this metric as exploratory and avoid causal language.
