import streamlit as st
import requests
import matplotlib.pyplot as plt

API_KEY = "30a8d5cc1ec2b87f6104ddc7819fbb4e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
BASE_FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city):
    """Fetch real-time weather data for a given city."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        return weather_info
    else:
        return {"error": "City not found!"}

def get_5day_forecast(city):
    """Fetch 5-day weather forecast for a given city."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_FORECAST_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    return {"error": "City not found!"}

def plot_weather_trends(forecast_data):
    """Plot temperature trends over 5 days."""
    dates = [item['dt_txt'] for item in forecast_data['list'][:5]]
    temps = [item['main']['temp'] for item in forecast_data['list'][:5]]
    
    plt.figure(figsize=(8,4))
    plt.plot(dates, temps, marker='o', linestyle='-', color='b')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('5-Day Temperature Trend')
    plt.xticks(rotation=45)
    plt.grid()
    return plt

st.title("🌦 Real-Time Weather App")

city = st.text_input("Enter City Name", "")

if st.button("Get Weather"):
    if city:
        weather = get_weather(city)
        if "error" in weather:
            st.error(weather["error"])
        else:
            st.success(f"Weather in {weather['city']}")
            st.write(f"🌡 Temperature: {weather['temperature']}°C")
            st.write(f"💧 Humidity: {weather['humidity']}%")
            st.write(f"☁ Description: {weather['description'].capitalize()}")
            
            # Fetch and plot the 5-day forecast
            forecast = get_5day_forecast(city)
            if "error" not in forecast:
                st.subheader("📊 5-Day Weather Forecast")
                fig = plot_weather_trends(forecast)
                st.pyplot(fig)
            else:
                st.error("Could not retrieve 5-day forecast.")
    else:
        st.warning("Please enter a city name.")