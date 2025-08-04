import requests  # For making HTTP API requests

# Your OpenWeatherMap API key
api_key = "KEY"

# Format the weather data into a user-friendly string
def format_weather(city: str, data: dict) -> str:
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    return (
        f"The weather in {city} is {weather} "
        f"with a temperature of {temperature} Celcius."
    )

# Get latitude and longitude for a given city using OpenWeatherMap Geocoding API
def get_lat_lon(city):
    url = (
        f"http://api.openweathermap.org/geo/1.0/direct?"
        f"q={city}&limit=1&appid={api_key}"
    )

    print(f"Retrieving latitude and longitude for {city}.")
    response = requests.get(url)
    data = response.json()

    # If successful and response contains data, return lat/lon
    if response.status_code == 200 and data:
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        return lat, lon
    else:
        print("Failed to retrieve latitude and longitude.", data)
        return None, None

# Get weather data using coordinates
def get_weather(city):
    # First get coordinates of the city
    lat, lon = get_lat_lon(city)
    
    # If coordinates couldn't be retrieved, return failure
    if lat is None or lon is None:
        return False, f"Failed to retrieve weather information for {city}."

    print(f"Got Lat Lon for {city}: {lat}, {lon}")
    
    # Build the weather API request URL
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"units=metric&lat={lat}&lon={lon}&appid={api_key}"
    )

    # Request weather data
    response = requests.get(url)
    data = response.json()

    # If successful, return formatted weather string
    if response.status_code == 200:
        print(f"Retrieved weather information for {city}.", data)
        return True, format_weather(city, data)
    else:
        print("Failed to retrieve weather information.", data)
        return False, "Failed to retrieve weather information."

# Run the module as a standalone script for testing
if __name__ == "__main__":
    city = "Munich"
    print(get_weather(city))
