import tkinter as tk
from tkinter import messagebox
import requests


API_KEY = 'e2bfa8d1ec60bc2501cd3d8e3cc7f4ba'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # or 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        weather_data = response.json()

        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        weather_result = (
            f"City: {city}\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )

        result_label.config(text=weather_result)

    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", f"City '{city}' not found!")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Network Error: {e}")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

# Heading
heading_label = tk.Label(root, text="Weather App", font=("Arial", 18, "bold"))
heading_label.pack(pady=10)

# City Entry
city_entry = tk.Entry(root, font=("Arial", 14), width=25)
city_entry.pack(pady=10)

# Get Weather Button
get_weather_button = tk.Button(root, text="Get Weather", font=("Arial", 14), command=get_weather)
get_weather_button.pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Run the App
root.mainloop()
