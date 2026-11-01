import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from analytics import medal_trend, country_medals, sport_efficiency, region_efficiency, kpis

def sample():
    return pd.DataFrame([
        {"athlete_id":1,"year":2020,"season":"Summer","country_code":"AAA","country":"Alpha","region":"Asia","sport":"Rowing","medal":"Gold"},
        {"athlete_id":2,"year":2020,"season":"Summer","country_code":"AAA","country":"Alpha","region":"Asia","sport":"Rowing","medal":"No Medal"},
        {"athlete_id":3,"year":2022,"season":"Winter","country_code":"BBB","country":"Beta","region":"Europe","sport":"Biathlon","medal":"Bronze"},
    ])

def test_medal_trend_counts_medal_entries():
    out = medal_trend(sample())
    assert out["medal_awards"].sum() == 2

def test_country_medals_filter():
    out = country_medals(sample(), year=2020)
    assert len(out) == 1
    assert out.iloc[0]["country"] == "Alpha"

def test_sport_efficiency_has_metric():
    out = sport_efficiency(sample())
    assert "medals_per_athlete_entry" in out.columns
    assert out["medals_per_athlete_entry"].between(0,1).all()

def test_region_efficiency_percentage():
    out = region_efficiency(sample())
    assert out["medal_efficiency_pct"].between(0,100).all()

def test_kpis():
    out = kpis(sample())
    assert out["countries"] == 2
    assert out["sports"] == 2
