"""Reusable analytics functions for the Olympic performance project."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"

MEDAL_NAMES = {"Gold", "Silver", "Bronze"}

def load_data():
    athlete_file = DATA / "athletes_events.csv"
    investment_file = DATA / "sports_investment.csv"
    if not athlete_file.exists():
        from data_prep import prepare
        prepare()
    athletes = pd.read_csv(athlete_file)
    investment = pd.read_csv(investment_file)
    return athletes, investment

def medal_trend(athletes):
    return (athletes[athletes["medal"].isin(MEDAL_NAMES)]
            .groupby(["year", "season"], as_index=False)
            .size().rename(columns={"size": "medal_awards"})
            .sort_values("year"))

def country_medals(athletes, year=None, season=None):
    df = athletes[athletes["medal"].isin(MEDAL_NAMES)].copy()
    if year is not None:
        df = df[df["year"] == int(year)]
    if season and season != "All":
        df = df[df["season"] == season]
    return (df.groupby(["country_code", "country", "region"], as_index=False)
            .size().rename(columns={"size": "total_medals"})
            .sort_values("total_medals", ascending=False))

def sport_efficiency(athletes):
    df = athletes.copy()
    df["won_medal"] = df["medal"].isin(MEDAL_NAMES)
    result = (df.groupby("sport", as_index=False)
              .agg(athlete_event_entries=("athlete_id", "count"),
                   medal_entries=("won_medal", "sum")))
    result["medals_per_athlete_entry"] = (
        result["medal_entries"] / result["athlete_event_entries"]
    ).round(4)
    return result.sort_values("medals_per_athlete_entry", ascending=False)

def region_efficiency(athletes):
    df = athletes.copy()
    df["won_medal"] = df["medal"].isin(MEDAL_NAMES)
    return (df.groupby("region", as_index=False)
            .agg(athlete_event_entries=("athlete_id", "count"),
                 medal_entries=("won_medal", "sum"))
            .assign(medal_efficiency_pct=lambda x:
                    (100*x["medal_entries"]/x["athlete_event_entries"]).round(2))
            .sort_values("medal_efficiency_pct", ascending=False))

def investment_efficiency(athletes, investment):
    medals = (athletes[athletes["medal"].isin(MEDAL_NAMES)]
              .groupby(["year", "country_code", "country", "region", "season"],
                       as_index=False).size().rename(columns={"size":"total_medals"}))
    merged = investment.merge(
        medals, on=["year","country_code","country","region","season"], how="left"
    )
    merged["total_medals"] = merged["total_medals"].fillna(0)
    merged["medals_per_usd_million"] = (
        merged["total_medals"] / merged["sports_investment_usd_millions"].replace(0, pd.NA)
    ).round(3)
    return merged.sort_values("medals_per_usd_million", ascending=False)

def kpis(athletes):
    medal_rows = athletes[athletes["medal"].isin(MEDAL_NAMES)]
    return {
        "athlete_event_entries": int(len(athletes)),
        "countries": int(athletes["country"].nunique()),
        "sports": int(athletes["sport"].nunique()),
        "medal_entries": int(len(medal_rows)),
        "years": f'{int(athletes["year"].min())}–{int(athletes["year"].max())}',
    }
