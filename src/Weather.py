import sys
import requests
from bs4 import BeautifulSoup as bs
from Geo import get_coordinates
from Input_Parser import parse_string
from Speak import speak
from num2words import num2words

def run_weather(input):
    if input.find('weather') != -1:
        city = 'madison'
        query = parse_string(input, 'weather')
        if query.find('in') != -1:
            city = parse_string(query, 'in')
        return get_weather(city)


def get_weather(city):
    url = 'https://darksky.net/forecast/'
    coordinates = get_coordinates(city)

    if (coordinates == -1):
        print('Error: city unable to be found')
        sys.exit(1)

    latitude = str(coordinates['latitude'])
    longitude = str(coordinates['longitude'])
    url = url + latitude + ',' + longitude + '/us12/en'

    response = requests.get(url)

    if response.status_code != 200:
        print('Error, webpage status code returned {}'.format(response.status_code))
        print(response.text)
        print(response)
        sys.exit(1)

    html_text = response.text
    soup = bs(html_text, 'lxml')
    weather = soup.find('span', class_ = 'summary swap')
    speak_str = weather.text
    degree_index = speak_str.find('˚')
    if degree_index != -1:
        speak_str = speak_str.replace('˚', '')
    split = speak_str.split()
    print(split[0])
    word = num2words(split[0])
    split[0] = ''
    space = ' '
    descriptor = space.join(split)
    
    speak_str = 'the weather in ' + city + ' is ' + word + ' and it is ' + descriptor
    speak(speak_str)
    return True
    

