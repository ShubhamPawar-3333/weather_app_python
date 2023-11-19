import streamlit as st
import requests

# OpenWeatherMap API key
api_key = "INSERT_YOUR_API_KEY"

# Function to get weather data based on city name
def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"} 
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

# Streamlit app
st.title("Simple Weather App")

# User input for city name
city_name = st.text_input("Enter city name:", "London")

# Get weather data when the user clicks the button
if st.button("Get Weather"):
    weather_data = get_weather(city_name)

    # Display weather information
    if weather_data["cod"] == "404":
        st.error("City not found. Please enter a valid city name.")
    else:
        st.subheader(f"Weather in {city_name}")
        st.write(f"Temperature: {weather_data['main']['temp']}°C")
        st.write(f"Description: {weather_data['weather'][0]['description']}")
        st.write(f"Humidity: {weather_data['main']['humidity']}%")
        st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
