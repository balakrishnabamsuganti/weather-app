# Weather Application

A simple Python GUI application to fetch and display real-time weather data using the OpenWeatherMap API.

## Project Overview
This application allows users to input a city name and retrieve current weather details like temperature, humidity, and wind speed in a user-friendly graphical interface built with Tkinter.

## Features
- GUI-based user input using Tkinter
- Real-time weather fetching from OpenWeatherMap API
- Displays temperature, humidity, and wind speed
- Handles errors such as invalid city names or network issues

## Technologies Used
- Python 3.x
- Tkinter (for GUI)
- Requests (for API calls)
- OpenWeatherMap API

## Prerequisites
- Python 3.x installed
- OpenWeatherMap API Key

Install required libraries:
```bash
pip install requests
```

## Setup and Running the Application
1. Clone or download the repository.
2. Replace `API_KEY` in the script with your OpenWeatherMap API key.
3. Run the application:
```bash
python weather_app.py
```

## Project Structure
```
weather_app/
│
├── weather_app.py   # Main Python file
└── README.md        # Project documentation
```

## Future Improvements
- Add weather icons based on conditions
- Search by coordinates (latitude and longitude)
- Store search history in a local database
- Dark/light mode support

## Author
- **Balakrishna Bamsuganti**
- Python Developer | Virtunexa Intern | Aspiring Backend Developer

---

Feel free to contribute, suggest improvements, or fork this project!
