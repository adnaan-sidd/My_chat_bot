import requests
import pandas as pd
from datetime import datetime, timedelta

# Configuration
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"  # Example API URL, update with actual API if different
ASSETS = ['EURUSD', 'GBPUSD', 'JPYUSD', 'XAUUSD']

def fetch_data():
    data = {}
    for asset in ASSETS:
        # Fetch data from the API
        response = requests.get(f"{API_URL}/{asset}")  # Update to use your data source correctly
        if response.status_code == 200:
            data[asset] = response.json()  # Store the data in a dictionary
        else:
            print(f"Error fetching {asset}: {response.status_code}")
    return data

if __name__ == "__main__":
    data = fetch_data()
    print(data)  # Print the collected data for verification
