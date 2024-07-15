import math
from camera_bird_detection import lat_long_output

# Define the coordinates of wind turbines and the radius
# this will eventually be passed from a database of turbine info
WIND_TURBINES = [
    {"id": "WT1", "latitude": 34.0522, "longitude": -118.2437},
    {"id": "WT2", "latitude": 34.0525, "longitude": -118.2440},
    # Add more turbines as needed
]
RADIUS_MILES = 1.0

# Function to calculate distance between two geographic coordinates using Haversine formula
def haversine_distance(lat1, lon1, lat2, lon2):
    ''' Used to calculate the great-circle distance between 
    two points on the Earth's surface, given their 
    latitude and longitude.
    '''
    R = 3958.8  # Earth radius in miles
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# Function to send message to wind turbines
def send_message(turbine_id):
    print(f"Message sent to Wind Turbine {turbine_id}: Bird detected within {RADIUS_MILES} mile radius.")

# Main function to check proximity and send messages
def check_bird_proximity():
    bird_location = lat_long_output()
    for turbine in WIND_TURBINES:
        distance = haversine_distance(
            bird_location["latitude"],
            bird_location["longitude"],
            turbine["latitude"],
            turbine["longitude"],
        )
        if distance <= RADIUS_MILES:
            send_message(turbine["id"])

# Run the program
if __name__ == "__main__":
    check_bird_proximity()
