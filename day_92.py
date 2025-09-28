import requests, json
timezone = "CST"
latitude = 25.961378
longitude = -108.896939

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")
jsonResult = result.json()
todayOvercast = jsonResult["daily"]

weatherCode = todayOvercast["weathercode"][0]
maxTemperature = todayOvercast["temperature_2m_max"][0]
minTemperature = todayOvercast["temperature_2m_min"][0]

if weatherCode == 0:
  print("Clear sky")
elif weatherCode == 1 or weatherCode == 2 or weatherCode == 3:
  print("Mainly clear, party cloudy, and overcast")
else:
  print("Otro pronostico wachín")

print(f"🥵: {maxTemperature}°C   🥶: {minTemperature}°C")