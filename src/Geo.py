from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="name")

def get_coordinates(city):
    coordinates = {}
    location = geolocator.geocode(city)
    if (location == None):
        return -1
    coordinates['latitude'] = round(location.latitude, 4)
    coordinates['longitude'] = round(location.longitude, 4)
    return coordinates

def main():
    city = 'Madison'
    coordinates = get_coordinates(city)
    print('latitude = {}'.format(coordinates['latitude']))
    print('longitude = {}'.format(coordinates['longitude']))

if __name__=="__main__":
    main()
    

