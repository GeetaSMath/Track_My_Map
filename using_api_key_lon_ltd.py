import requests

API_KEY = 'AIzaSyCY5BmvPdwm6T4eEQUe4v3ZbjcsUMz9FhU'   # Replace with your API key
address = 'bangalore BDA complex'  # Replace with your current or destination address

url = 'https://maps.googleapis.com/maps/api/geocode/json'
params = {'address': address, 'key': API_KEY}

response = requests.get(url, params=params)
result = response.json()

if result['status'] == 'OK':
    geometry = result['results'][0]['geometry']['location']
    latitude = geometry['lat']
    longitude = geometry['lng']
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print('Geocoding request failed.')
