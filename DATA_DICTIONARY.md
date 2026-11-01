# Data dictionary

## athletes_events_demo.csv
- `athlete_id`: unique generated row/athlete-event identifier in demo data.
- `athlete_name`: generated placeholder name, not a real person.
- `year`, `host_city`, `season`: Games edition metadata.
- `country_code`, `country`, `region`: generated delegation labels.
- `sport`, `event`: sport and generated event label.
- `medal`: Gold, Silver, Bronze or No Medal.
- `data_status`: SYNTHETIC_DEMO.

## medal_results_demo.csv
Aggregate counts from the demo athlete-event file; medal counts represent athlete-event medal entries, not necessarily official medal-table totals.

## sports_investment_demo.csv
Generated fictional investment values in USD millions. These must never be described as real country sports budgets.
