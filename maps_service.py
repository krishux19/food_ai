import requests
import os

MAPS_API_KEY = os.getenv("MAPS_API_KEY")

def get_nearby_food(lat=28.6139, lon=77.2090):  # default Delhi
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    params = {
        "location": f"{lat},{lon}",
        "radius": 1500,
        "type": "restaurant",
        "key": MAPS_API_KEY
    }

    response = requests.get(url, params=params).json()

    results = []
    for place in response.get("results", [])[:3]:
        results.append({
            "name": place["name"],
            "rating": place.get("rating", "N/A")
        })

    return results