import requests
import matplotlib.pyplot as plt
from urllib.parse import quote
from config import API_KEY

def fetch_data(chart_name, timespan, rolling_average, format="json"):
    api_key = API_KEY
    api_url = f"https://api.blockchain.info/charts/{quote(chart_name)}"

    params = {
        "timespan": quote(timespan),
        "rollingAverage": quote(rolling_average),
        "format": format
    }

    try:
        response = requests.get(api_url, params=params, headers={"Content-Type": "application/json", "Accept": "application/json"})
        response.raise_for_status()

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def plot_data(data):
    x_values = [entry["x"] for entry in data["values"]]
    y_values = [entry["y"] for entry in data["values"]]

    plt.plot(x_values, y_values)
    plt.title(data["name"])
    plt.xlabel("Timestamp")
    plt.ylabel(data["unit"])
    plt.show()

if __name__ == "__main__":
    # Manually define a list of valid chart names
    valid_chart_names = ["transactions-per-second", "trade-volume", "market-price"]

    print("Valid Chart Names:")
    for chart_name in valid_chart_names:
        print(chart_name)

    # Choose a chart name from the valid ones
    chart_name = input("\nEnter the chart name from the list above: ").lower()

    # Get user input for timespan and rolling average
    timespan = input("Enter the timespan (e.g., 5weeks): ")
    rolling_average = input("Enter the rolling average (e.g., 8hours): ")

    fetched_data = fetch_data(chart_name, timespan, rolling_average)

    if fetched_data is not None:
        print(f"Data fetched successfully:\n{fetched_data}")
        plot_data(fetched_data)
    else:
        print("Failed to fetch data.")
