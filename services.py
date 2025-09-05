import httpx


async def fetch_weather(city: str):
    # using Open-Meteo free api
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    async with httpx.AsyncClient as client:
        geo_response = await client.get(url)
        geo_data = geo_response.json()

    if "results" not in geo_data:
        return None
    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    async with httpx.AsyncClient as client:
        weather_response = await client.get(weather_url)
        weather_data = weather_response.json()

    current = weather_data.get("current_weather", {})
    return {
        "temperature": current.get("temperature"),
        "description": "clear sky" if current.get("weathercode") == 0 else "cloudy",
    }
