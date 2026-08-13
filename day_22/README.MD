# Day 22 - Weather App using API 🌦️

## 📌 Description

Today I created a simple Weather App using Python.

The program asks the user to enter a city name and gets the current weather information using a Weather API.

It displays:
- 🌡️ Temperature
- ☁️ Weather condition
- 💧 Humidity

I also learned how to handle errors using `try` and `except`.

## 🛠️ Concepts Learned

- Python `input()`
- Variables
- f-strings
- `import requests`
- APIs
- `requests.get()`
- JSON data
- Dictionaries and keys
- Lists and indexing `[0]`
- `try` and `except`
- Error handling

## 💻 Code

```python
import requests

city = input("Enter your city : ")

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url).json()

    current = response["current_condition"][0]
    temperature = current["temp_C"]
    weather = current["weatherDesc"][0]["value"]
    humidity = current["humidity"]

    print("Temperature:", temperature, "°C")
    print("Weather:", weather)
    print("Humidity:", humidity, "%")

except:
    print("Unable to get weather information.")