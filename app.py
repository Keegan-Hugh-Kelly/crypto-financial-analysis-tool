# app.py
from flask import Flask, render_template, request, jsonify
import requests
from urllib.parse import quote
from config import API_KEY

app = Flask(__name__)

def fetch_data(chart_name, timespan, rolling_average, format="json"):
    api_url = f"https://api.blockchain.info/charts/{quote(chart_name)}"
    params = {
        "timespan": quote(timespan),
        "rollingAverage": quote(rolling_average),
        "format": format
    }

    headers = {"Content-Type": "application/json", "Accept": "application/json", "X-API-Key": API_KEY}

    try:
        response = requests.get(api_url, params=params, headers=headers)
        response.raise_for_status()

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        chart_name = request.form["chart_name"].lower()
        timespan = request.form["timespan"]
        rolling_average = request.form["rolling_average"]

        fetched_data = fetch_data(chart_name, timespan, rolling_average)

        if fetched_data is not None:
            return jsonify(fetched_data)
        else:
            return jsonify({"error": "Failed to fetch data."})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
