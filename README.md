## 01 .lon_ltd_city_wise
#   Overview
  ## Location Finder — Python Project

- This project is a simple Python-based location finder that helps you get:
-  Your current location (using your IP address)
- The latitude and longitude of any area, city, or country you enter

## How It Works
- The program first checks your current location using your IP address (ipinfo.io).
- Then it asks you to enter a destination area, such as Jayanagar, Bangalore or Andheri, Mumbai.
- It connects to the OpenStreetMap Nominatim API to find the latitude and longitude of that place.
- The results are displayed clearly in the console.

## Technologies and Libraries Used
   # 1. requests

   - Purpose: To send and receive data from APIs (like ipinfo.io and nominatim.openstreetmap.org).

###  Why Used:

- Very simple to make web requests.
- Converts responses to JSON easily.
- Reliable and widely used for Python API communication.

# 2. geopy (optional method)

- Purpose: Used for geocoding (finding coordinates for a location name).

### Why Used:

- Works directly with OpenStreetMap (Nominatim).
- Doesn’t require an API key (free to use).
- Provides clean and readable results.

# 3. geopy.geocoders.Nominatim
- Purpose: Converts a city or area name (e.g., “Bangalore, India”) into latitude and longitude.

### Why Used:
- It’s free and open-source.
- Gives accurate global results.
- Perfect for small projects and demos.

## Libraries
   - requests
   - geocoder


## 02 .open_street_map_bglr_area

## Overview

- This Python program finds the latitude and longitude of specific areas in Bengaluru (Bangalore) using OpenStreetMap’s Nominatim API.
- It’s a quick and easy tool for geolocation lookup — you just provide area names, and the program fetches their coordinates automatically.
