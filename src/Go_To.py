import json
import sys
import webbrowser
from Input_Parser import parse_string
from Speak import speak

def go_to(key_str):
    name_to_url_dict = {}
    with open('name_to_url.json', 'r') as json_file:
        name_to_url_dict = json.load(json_file)
    url = name_to_url_dict[key_str]
    webbrowser.open(url, new=2)
    speak('Pulling up now')
    return True


def run_go_to(input):
    if input.find('go to') != -1:
        query = parse_string(input, 'to')
        
        if query.find('google') != -1:
            go_to('google')
        if query.find('netflix') != -1:
            go_to('netflix')
        if query.find('youtube') != -1:
            go_to('youtube')
        if query.find('disney') != -1:
            go_to('disney plus')
        if query.find('td') != -1:
            go_to('td ameritrade')
        if query.find('ameritrade') != -1:
            go_to('td ameritrade')
        if query.find('brokerage') != -1:
            go_to('td ameritrade')
        if query.find('email') != -1:
            go_to('email')
        if query.find('canvas') != -1:
            go_to('canvas')
        if query.find('uw') != -1:
            go_to('my uw')
        if query.find('good reads') != -1:
            go_to('goodreads')