from flask import Flask, render_template, request, jsonify
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from data_prep import prepare
from analytics import (load_data, medal_trend, country_medals, sport_efficiency,
                       region_efficiency, investment_efficiency, kpis)

app = Flask(__name__)
if not (ROOT / "data" / "processed" / "athletes_events.csv").exists():
    prepare()

def get_frames():
    return load_data()

@app.route("/")
def index():
    athletes, investment = get_frames()
    summary = kpis(athletes)
    trend = medal_trend(athletes)
    country = country_medals(athletes).head(10)
    sport = sport_efficiency(athletes).head(10)
    region = region_efficiency(athletes)
    investment_table = investment_efficiency(athletes, investment).head(10)
    return render_template(
        "index.html", summary=summary,
        trend_labels=trend["year"].astype(str).tolist(),
        trend_values=trend["medal_awards"].astype(int).tolist(),
        country_labels=country["country"].tolist(),
        country_values=country["total_medals"].astype(int).tolist(),
        sport_labels=sport["sport"].tolist(),
        sport_values=(sport["medals_per_athlete_entry"]*100).round(2).tolist(),
        region_labels=region["region"].tolist(),
        region_values=region["medal_efficiency_pct"].tolist(),
        investment_rows=investment_table.to_dict(orient="records"),
    )

@app.route("/api/medal-trend")
def api_medal_trend():
    athletes, _ = get_frames()
    season = request.args.get("season", "All")
    trend = medal_trend(athletes)
    if season != "All":
        trend = trend[trend["season"] == season]
    return jsonify(trend.to_dict(orient="records"))

@app.route("/tableau")
def tableau():
    # Replace the URL in templates/tableau.html with a published Tableau view URL.
    return render_template("tableau.html")

@app.route("/health")
def health():
    return jsonify({"status":"ok", "project":"Global Olympic Sports Performance Analytics"})

if __name__ == "__main__":
    app.run(debug=True)
