from geopy.geocoders import Nominatim


def get_direccion_luiscore(lat: str, lon: str):
    geolocator = Nominatim(user_agent="luis")
    location = geolocator.reverse(f"{lat}, {lon}")
    return location.address
