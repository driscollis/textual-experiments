import pgeocode
import requests

wmo_codes = {0: "Clear sky",
             1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
             45: "Fog", 48: "Fog with depositing rime",
             51: "Light Drizzle", 53: "Moderate Drizzle", 55: "Dense Drizzle",
             56: "Light Freezing Drizzle", 57: "Denze Freezing Drizzle",
             61: "Light Rain", 63: "Moderate Rain", 65: "Heavy Rain",
             66: "Light Freezing Fain", 67: "Heavy Freezing Rain",
             71: "Light Snow", 73: "Moderate Snow", 75: "Geavy Snow",
             77: "Flurries",
             80: "Light Rain", 81: "Moderate Rain", 82: "Violent Rain",
             85: "Slight Snow Showers", 86: "Heavy Snow Showers",
             95: "Thunderstorms",
             96: "Thunderstorms w/ Light Hail",
             99: "Thunderstorms w/ Heavy Hail",}

smo_to_emoji = {
    0: "sun",
    1: "sun_with_face",
    2: "partly_sunny", 3: "cloudy",
    51: "cloud_with_rain", 52: "cloud_with_rain", 55: "cloud_with_rain",
    45: "fog", 48: "foggy",
    56: "ice", 57: "ice",
    61: "cloud_with_rain", 63: "cloud_with_rain", 65: "cloud_with_rain",
    66: "ice", 67: "ice",
    71: "snowflake", 73: "snowflake", 75: "snowflake",
    85: "snowflake", 86: "snowflake",
    95: "thunder_cloud_and_rain", 95: "cloud_with_lightning_and_rain",
    99: "cloud_with_lightning_and_rain",}


# Get location lag/lon from zip
nomi = pgeocode.Nominatim("us")
location = nomi.query_postal_code("50035")
lat = location["latitude"]
lon = location["longitude"]
town =  location["place_name"]
state_code = location["state_code"]

# Get weather info

url =  f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
print(url)

# https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,precipitation,rain&daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=America%2FChicago
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=41.7017&longitude=-93.4527&current=temperature_2m,precipitation,rain&hourly=temperature_2m")
result = response.json()
temp = result["current"]["temperature_2m"]
temp_f = (temp * 9 / 5) + 32
print(f"Current temperature for {town} {state_code} is {temp}C / {temp_f} F")

#import openmeteo_requests
#from openmeteo_sdk.Variable import Variable
#params = {
    #"latitude": location["latitude"],
    #"longitude": location["longitude"],
    #"hourly": ["temperature_2m", "precipitation", "wind_speed_10m"],
    #"current": ["temperature_2m", "relative_humidity_2m"]
#}

#responses = om.weather_api("https://api.open-meteo.com/v1/forecast", params=params)

#current = responses[0].Current()
#current_variables = list(map(lambda i: current.Variables(i), range(0, current.VariablesLength())))
#current_temperature_2m = next(filter(lambda x: x.Variable() == Variable.temperature and x.Altitude() == 2, current_variables))
#current_relative_humidity_2m = next(filter(lambda x: x.Variable() == Variable.relative_humidity and x.Altitude() == 2, current_variables))

#temp =  current_temperature_2m.Value()
#temp_f = (temp * 9 / 5) + 32
#print(f"Current temperature_2m {temp}C / {temp_f} F")
#print(f"Current relative_humidity_2m {current_relative_humidity_2m.Value()}")
