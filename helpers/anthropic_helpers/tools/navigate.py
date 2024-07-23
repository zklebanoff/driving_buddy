import googlemaps
from datetime import datetime
from dotenv import load_dotenv
import os, re

load_dotenv()


navigate = {
  "name": "navigate",
  "description": "Takes an array of two or more locations (cities, towns, etc.) and provides step-by-step directions for traveling from the first location to each subsequent location, ultimately reaching the final destination. The directions include detailed instructions on routes, distances, and estimated travel times between each location.",
  "input_schema": {
    "type": "object",
    "properties": {
      "locations": {
        "type": "array",
        "items": {
          "type": "string",
          "description": "A list of locations (cities, towns, etc.)"
        },
        "minItems": 2,
        "description": "An array of two or more locations."
      }
    },
    "required": ["locations"]
  }
}

# locations = [
#     "New York, NY",
#     "Philadelphia, PA",
#     "Baltimore, MD",
#     "Washington, DC"
# ]
def get_directions(locations):
    gmaps = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_KEY'))

    # Ensure there are at least two locations
    if len(locations) < 2:
        raise ValueError("At least two locations are required to get directions.")

    # Request directions
    directions_result = gmaps.directions(
        origin=locations[0],
        destination=locations[-1],
        waypoints=locations[1:-1],
        mode="driving",
        departure_time=datetime.now()
    )

    return directions_result

def extract_instructions(directions):
    instructions = ""
    for leg in directions[0]['legs']:
        for step in leg['steps']:
            # Remove HTML tags using regex
            clean_text = re.sub('<[^<]+?>', '', step['html_instructions'])
            instructions += f"{clean_text}\n"

    return instructions

def navigate_tool(locations):
  directions = get_directions(locations)
  instructions = extract_instructions(directions)
  return instructions