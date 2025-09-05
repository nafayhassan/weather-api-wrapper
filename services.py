import httpx
import logging

logging.basicConfig(level=logging.INFO)


async def fetch_weather(city: str):
    try:
        # Step 1: Get coordinates
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        async with httpx.AsyncClient(timeout=10.0) as client:
            geo_response = await client.get(geo_url)
            geo_response.raise_for_status()  # raise if status != 200
            geo_data = geo_response.json()

        if "results" not in geo_data or len(geo_data["results"]) == 0:
            logging.error(f"No results found for {city}")
            return None

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        # Step 2: Get weather
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current_weather=true"
        )
        async with httpx.AsyncClient(timeout=10.0) as client:
            weather_response = await client.get(weather_url)
            weather_response.raise_for_status()
            weather_data = weather_response.json()

        current = weather_data.get("current_weather", {})
        if not current:
            logging.error("No current weather data in response")
            return None

        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            51: "Light rain",
            61: "Rain showers",
        }

        return {
            "temperature": current.get("temperature"),
            "description": weather_codes.get(current.get("weathercode"), "Unknown"),
        }

    except httpx.HTTPError as e:
        logging.error(f"HTTP error fetching weather: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None


# GET WEATHER BY C0 ORDINATES
async def fetch_weather_by_coordinates(lat: float, lon: float):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()

            current = data.get("current_weather", {})
            if not current:
                return None

            weather_codes = {
                0: "Clear sky", 1: "Mainly clear", 2: "Partly cloud", 3: "Overcast",
                45: "Fog", 51: "Light rain", 61: "Rain showers",
            }

            return {
                "temperature": current.get("temperature"),
                "description": weather_codes.get(current.get("weathercode"), "unknown"),
            }
    except Exception:
        return None


# FETCH FORECAST
async def fetch_forecast(city: str, days: int = 5):
    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        async with httpx.AsyncClient(timeout=10.0) as client:
            geo = await client.get(geo_url)
            geo.raise_for_status()
            geo_data = geo.json()

        if "results" not in geo_data or not geo_data["results"]:
            return None

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        forecast_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min&forecast_days={days}&timezone=auto"
        )
        async with httpx.AsyncClient(timeout=10.0) as client:
            forecast = await client.get(forecast_url)
            forecast.raise_for_status()
            return forecast.json()
    except Exception:
        return None
