from geopy.geocoders import Nominatim

def get_direccion_mikecore(lat: str, lon: str):
    geolocator = Nominatim(user_agent="mike")
    location = geolocator.reverse(f"{lat}, {lon}")
    return location.address


