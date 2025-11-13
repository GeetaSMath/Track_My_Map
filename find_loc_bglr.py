import requests

def get_current_location():
    """Get current location based on IP."""
    try:
        response = requests.get("https://ipinfo.io/json")
        if response.status_code == 200:
            data = response.json()
            loc = data.get("loc", "").split(",")
            latitude = loc[0] if len(loc) > 0 else None
            longitude = loc[1] if len(loc) > 1 else None
            print("\n Current Location Details:")
            print(f"City: {data.get('city')}")
            print(f"Region: {data.get('region')}")
            print(f"Country: {data.get('country')}")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
            return latitude, longitude
        else:
            print(" Failed to get current location. Status code:", response.status_code)
            return None, None
    except Exception as e:
        print(" Error getting current location:", e)
        return None, None


def get_bangalore_area_coordinates(area):
    """Find latitude & longitude of any area in Bangalore using Nominatim."""
    try:
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": f"{area}, Bangalore, India",
            "format": "json",
            "limit": 1
        }
        headers = {"User-Agent": "bangalore-area-locator-python"}

        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200 and response.json():
            data = response.json()[0]
            latitude = data["lat"]
            longitude = data["lon"]
            print("\n Destination Details:")
            print(f"Area: {area}, Bangalore, India")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
            return latitude, longitude
        else:
            print("Could not find location for:", area)
            return None, None
    except Exception as e:
        print("Error finding destination:", e)
        return None, None


print(" Bangalore Area Location Finder")
get_current_location()
area = input("\nEnter the area/locality in Bangalore: ").strip()
get_bangalore_area_coordinates(area)


