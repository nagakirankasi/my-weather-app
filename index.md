# 🌦 Real-Time Weather App

A Python-based app that fetches real-time weather data using the OpenWeatherMap API.

## 🚀 Features
- Fetches live weather data for any city
- Displays temperature, humidity, and weather conditions
- Provides a **5-day weather forecast**
- Includes **graphical weather trends**
- Simple **CLI-based** and **Streamlit Web UI**

---

## 📦 Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/nagakirankasi/Weather-App.git
cd Weather-App
```

### **2️⃣ Install Dependencies**
Ensure Python 3.8+ is installed, then run:
```bash
pip install -r requirements.txt
```
**Example `requirements.txt`**:
```
requests
streamlit
flask
matplotlib
```

---

## 🔑 API Setup
Sign up at [OpenWeatherMap](https://openweathermap.org/) and get a **free API key**.
Replace `your_api_key` in `weather.py` with your actual API key:
```python
API_KEY = "your_api_key"
```

---

## 🌐 Usage
### **1️⃣ CLI Mode**
Run the script in command line mode:
```bash
python weather.py
```
Enter the city name when prompted, and the weather details will be displayed.

### **2️⃣ Web UI (Streamlit)**
Launch the web interface:
```bash
streamlit run app.py
```
Use the input field to enter a city name and fetch weather data.

---

## 🌤 5-Day Weather Forecast
The app now fetches and displays a **5-day weather forecast**, including:
- Daily temperature trends
- Humidity levels
- Weather conditions

### **Example API Call for Forecast Data**
```python
BASE_FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"
def get_5day_forecast(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_FORECAST_URL, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": "City not found!"}
```

---

## 📈 Graphical Weather Trends
The app now includes **visual graphs** to display:
- **Temperature trends over 5 days**
- **Humidity variations**

### **Example Graph Using Matplotlib**
```python
import matplotlib.pyplot as plt
def plot_weather_trends(forecast_data):
    dates = [item['dt_txt'] for item in forecast_data['list'][:5]]
    temps = [item['main']['temp'] for item in forecast_data['list'][:5]]
    plt.plot(dates, temps, marker='o', linestyle='-', color='b')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('5-Day Temperature Trend')
    plt.xticks(rotation=45)
    plt.show()
```

---

## 🧪 Running Tests
To ensure the weather API integration works correctly, run:
```bash
python -m unittest discover tests
```

---

## 📢 Contributing
Feel free to fork this repository and submit **pull requests** to improve the project!

### 🔥 Future Enhancements
- Support for **multiple weather APIs**
- Implement **real-time weather alerts**

---

This project is designed to provide accurate and up-to-date weather information in a simple format. 🌍🌤 Let us know if you have suggestions for improvements! 🚀

