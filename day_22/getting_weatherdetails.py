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
    print("Weather",weather)
    print("Humidity",humidity,"%")
    
except:
    print("Unable to get weather information.")




