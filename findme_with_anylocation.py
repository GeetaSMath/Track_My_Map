"""Function → *Takes an address*
    Output: *Lat, Long*


**2)** Function → *Gives Lat–Long of current location from laptop is being used.*

---

**3)** Get BridgeLabz BLR Lat–Long & save this in a DB.

  **a)** Get the Lat–Long of your login when you are in office.
      → Compare the same with office Lat–Long data.

  **c)** Go to your PG, log in and check."""


import requests
import csv
import os

CSV_FILE = "visited_locations.csv"
THRESHOLD = 0.01  # degrees for variance

def get_current_location():
    """Get approximate latitude and longitude of current location using IP."""
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        if "loc" in data:
            lat, lon = map(float, data["loc"].split(","))
            return lat, lon
    except:
        pass
    return None, None

def save_location(place_name, lat, lon):
    """Save a location in CSV."""
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Place", "Latitude", "Longitude"])
        writer.writerow([place_name, lat, lon])
    print(f"Saved new location: {place_name} -> Lat:{lat}, Lon:{lon}")

def check_variance(lat, lon):
    """Check if current location is near any saved location."""
    if not os.path.isfile(CSV_FILE):
        return None
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            saved_lat = float(row['Latitude'])
            saved_lon = float(row['Longitude'])
            if abs(lat - saved_lat) <= THRESHOLD and abs(lon - saved_lon) <= THRESHOLD:
                return row['Place']
    return None

# --- Main Program ---
place_name = input("Enter place name for this location: ")
current_lat, current_lon = get_current_location()

if current_lat and current_lon:
    print("Current Location -> Lat:", current_lat, "Lon:", current_lon)
    nearby_place = check_variance(current_lat, current_lon)
    if nearby_place:
        print(f"You are near previously saved location: {nearby_place}")
    else:
        save_location(place_name, current_lat, current_lon)
else:
    print("Could not determine current location.")
