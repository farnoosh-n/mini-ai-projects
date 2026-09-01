import requests
import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import create_agent

load_dotenv()

def get_weather_description(code):
    """Convert weather code to a weather description."""
    if code == 0:
        return "Sunny"

    elif code in [1, 2]:
        return "Partly cloudy"

    elif code == 3:
        return "Cloudy"

    elif code in [51, 53, 55, 56, 57]:
        return "Drizzle"

    elif code in [61, 63, 65, 66, 67, 80, 81, 82]:
        return "Rainy"

    elif code in [71, 73, 75, 77, 85, 86]:
        return "Snowy"

    elif code in [95, 96, 99]:
        return "Thunderstorm"

    else:
        return "Unknown"
# -------------------------
#  Find city coordinates
# -------------------------
@tool
def get_weather(city):
    """Get the current weather of a city."""
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params)

    data = response.json()

    if "results" not in data:
         return None
    
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]




# -------------------------
#  Get weather
# -------------------------

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params={
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code"
    }

    weather_response=requests.get(
        weather_url,
        params=weather_params
    )

    weather_data=weather_response.json()


    temperature = weather_data["current"]["temperature_2m"]



    weather_code = weather_data["current"]["weather_code"]
    weather = get_weather_description(weather_code)
    return f"{city}: {temperature}°C, {weather}"


@tool
def get_dollar_price():
    """
    Get the current US dollar price in toman.
    """
    token = os.getenv("TINDEX_TOKEN")

    url = "https://tindex.app/api/public/currency-rates"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    data = response.json()["data"]

    for item in data:
        if item["key"] == "usd-exchange-rate":
            return item["rate"]

#---------------LLM----------------
llm = ChatOllama(
    model="qwen2.5:3b"
)

#---------------Agents----------------
agent= create_agent(
    model=llm,
    tools=[get_weather,get_dollar_price]
)
response = agent.invoke({
    "messages":[
        {"role":"user",
        "content": "What's the weather in Berlin? and what is the current US dollar price in toman "}
    ]
})

print(response["messages"][-1].content)