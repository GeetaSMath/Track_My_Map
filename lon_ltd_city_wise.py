from geopy.geocoders import Nominatim

"""The script connects to OpenStreetMap’s Nominatim service.

It searches for the place name you entered.

It returns latitude and longitude if the location is found."""

geolocator = Nominatim(user_agent="geoapi")
location_name = "bangalore, India"
location = geolocator.geocode(location_name)

if location:
    print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
else:
    print("Location not found")

