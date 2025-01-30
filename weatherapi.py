import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime

API_KEY = "c95691fdbbcc27da28f483e46216c074"
CITY = "Chennai"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def fetch_weather_data(city, api_key):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def visualize_weather_data(data):
    if not data:
        return

    
    forecasts = data["list"]
    timestamps = [datetime.fromtimestamp(entry["dt"]) for entry in forecasts]
    temperatures = [entry["main"]["temp"] for entry in forecasts]
    humidity = [entry["main"]["humidity"] for entry in forecasts]

    
    df = pd.DataFrame({
        "Timestamp": timestamps,
        "Temperature (°C)": temperatures,
        "Humidity (%)": humidity
    })

    sns.set(style="darkgrid")
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 1, 1)
    sns.lineplot(x="Timestamp", y="Temperature (°C)", data=df, marker="o", color="r")
    plt.title(f"Temperature Forecast for {CITY}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")

    plt.subplot(2, 1, 2)
    sns.lineplot(x="Timestamp", y="Humidity (%)", data=df, marker="o", color="b")
    plt.title(f"Humidity Forecast for {CITY}")
    plt.xlabel("Time")
    plt.ylabel("Humidity (%)")

    plt.tight_layout()
    plt.show()


def main():
    data = fetch_weather_data(CITY, API_KEY)
    if data:
        visualize_weather_data(data)

if __name__ == "__main__":
    main()