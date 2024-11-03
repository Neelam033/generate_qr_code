import phonenumbers
from phonenumbers import geocoder, carrier
from geopy.geocoders import Nominatim

# Function to get phone number details
def get_phone_number_details(phone_number):
    # Parse phone number
    parsed_number = phonenumbers.parse(phone_number)

    # Get country
    country = geocoder.country_name_for_number(parsed_number, "en")

    # Get location description
    location = geocoder.description_for_number(parsed_number, "en")

    # Get carrier
    phone_carrier = carrier.name_for_number(parsed_number, "en")

    return country, location, phone_carrier

# Function to get coordinates for a given location
def get_coordinates(location):
    geolocator = Nominatim(user_agent="phone-location-tracker")
    location = geolocator.geocode(location)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Example phone number
phone_number = "+918887084034"

# Get phone number details
country, location, phone_carrier = get_phone_number_details(phone_number)
print(f"Country: {country}")
print(f"Location: {location}")
print(f"Carrier: {phone_carrier}")

# Get coordinates for the location
if location:
    latitude, longitude = get_coordinates(location)
    if latitude and longitude:
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
    else:
        print("Location not found.")
else:
    print("Location not found.")
