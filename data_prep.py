"""Validate and prepare the included demonstration datasets."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"

def prepare():
    OUT.mkdir(parents=True, exist_ok=True)
    athletes = pd.read_csv(RAW / "athletes_events_demo.csv")
    medals = pd.read_csv(RAW / "medal_results_demo.csv")
    investment = pd.read_csv(RAW / "sports_investment_demo.csv")

    required = {"year", "season", "country", "sport", "medal"}
    missing = required - set(athletes.columns)
    if missing:
        raise ValueError(f"Missing athlete dataset columns: {sorted(missing)}")

    athletes = athletes.drop_duplicates()
    athletes["year"] = pd.to_numeric(athletes["year"], errors="coerce").astype("Int64")
    athletes["medal"] = athletes["medal"].fillna("No Medal").str.strip().str.title()
    athletes = athletes.dropna(subset=["year", "country", "sport"])
    athletes.to_csv(OUT / "athletes_events.csv", index=False)

    medals = medals.drop_duplicates()
    medals["year"] = pd.to_numeric(medals["year"], errors="coerce").astype("Int64")
    medals.to_csv(OUT / "medal_results.csv", index=False)

    investment = investment.drop_duplicates()
    investment["sports_investment_usd_millions"] = pd.to_numeric(
        investment["sports_investment_usd_millions"], errors="coerce"
    )
    investment.to_csv(OUT / "sports_investment.csv", index=False)

    print("Prepared files:")
    for path in sorted(OUT.glob("*.csv")):
        print(f" - {path.name}: {sum(1 for _ in open(path, encoding='utf-8'))-1:,} rows")
    print("\\nIMPORTANT: included data is synthetic demonstration data, not official Olympic records.")

if __name__ == "__main__":
    prepare()
