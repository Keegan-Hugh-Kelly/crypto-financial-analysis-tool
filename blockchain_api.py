import requests
from config import API_KEY  # Make sure to replace this with your actual API key

def fetch_data():
    # Use the API key from the config file
    api_key = API_KEY

    # Specify the chart endpoint
    chart_name = "transactions-per-second"
    api_url = f"https://api.blockchain.info/charts/{chart_name}"

    # Parameters for the API request (you can customize these based on the documentation)
    params = {
        "timespan": "5weeks",  # Duration of the chart
        "rollingAverage": "8hours",  # Duration over which the data should be averaged
        "format": "json"  # Data format (JSON or CSV)
    }

    try:
        response = requests.get(api_url, params=params, headers={"Content-Type": "application/json", "Accept": "application/json"})
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    fetched_data = fetch_data()

    if fetched_data is not None:
        print(f"Data fetched successfully:\n{fetched_data}")
    else:
        print("Failed to fetch data.")
