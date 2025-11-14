import requests

def get_lat_long(place_name):
    """Uses OpenStreetMap’s free API
        Finds latitude and longitude for multiple places
        Demonstrates API usage, JSON handling, and looping in Python"""

    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": place_name,
        "format": "json",
        "limit": 1
    }

    headers = {"User-Agent": "location-finder-app"}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200 and response.json():
        data = response.json()[0]
        lat = data["lat"]
        lon = data["lon"]
        print(f" {place_name}")
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}\n")
    else:
        print(f"Could not find coordinates for {place_name}")

# Example areas in Bangalore
places = [
    "Koramangala, Bengaluru",
    "Whitefield, Bengaluru",
    "Jayanagar, Bengaluru",
    "Indiranagar, Bengaluru",
    "Malleshwaram, Bengaluru"
]

for place in places:
    get_lat_long(place)
