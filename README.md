# Simple Weather App using Python, Streamlit and OpenWeatherMap API

This is a simple weather app created using Python, Streamlit, and the OpenWeatherMap API. The app allows users to input a city name and retrieve the current weather information for that city.

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installing Dependencies

Install the required libraries using the following command:

```python
pip install streamlit requests
```

### Obtaining an API Key

You need to obtain an API key from OpenWeatherMap. Visit [OpenWeatherMap API](https://openweathermap.org/api) to sign up and get your free API key.

### Creating application
1. Importing necessary libraries

```python
import streamlit as st
import requests
```
2. Storing API key into `API_KEY` variable

3. Creating a function to fetch weather data from API based on city input
```python
def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"} 
    response = requests.get(base_url, params=params)
    data = response.json()
    return data
```

4.  Creating a streamlit app window
Create a streamlit app with an input field to enter the city name, button that calls `get_weather()` function, on click that will display the weather information.
```python
if st.button("Get Weather"):
    weather_data = get_weather(city_name)

    if weather_data["cod"] == "404":
        st.error("City not found. Please enter a valid city name.")
    else:
        st.subheader(f"Weather in {city_name}")
        st.write(f"Temperature: {weather_data['main']['temp']}°C")
        st.write(f"Description: {weather_data['weather'][0]['description']}")
        st.write(f"Humidity: {weather_data['main']['humidity']}%")
        st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
```
Run the Streamlit app:

```bash
streamlit run weather_app.py
```

## Usage

1. Enter the desired city name in the input field.
2. Click the "Get Weather" button to retrieve and display the current weather information for the specified city.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [OpenWeatherMap API](https://openweathermap.org/api)

Happy coding!
```

Make sure to replace `"your-username"` in the clone URL with your actual GitHub username. Additionally, include a license file (`LICENSE`) if desired and adjust the README file as needed for your project.
