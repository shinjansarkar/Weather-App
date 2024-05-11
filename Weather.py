import requests
import json

city = input("Enter the city name=")

url = f"http://api.weatherapi.com/v1/current.json?key=e4bc7b299c7c4803bf0151806241404&q={city}"

r = requests.get(url)

wdic = json.loads(r.text)
print("Temperature in celcius=",wdic ["current"]["temp_c"])
print("Humidity =",wdic["current"]["humidity"])
print("Wind speed(mph) =",wdic ["current"]["wind_mph"])
print("Feels like =",wdic["current"]["feelslike_c"])

