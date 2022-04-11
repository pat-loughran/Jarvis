import sys
import webbrowser
from Input_Parser import parse_string
from Speak import speak

def search(query, base_url):
    split = query.split()
    delimiter = '+'
    final_query = delimiter.join(split)
    final_url = base_url + final_query
    print('final url = {}'.format(final_url))
    webbrowser.open(final_url, new=2)

def search_helper(input, last_word, base_url):
    query = parse_string(input, last_word)
    search(query, base_url)
    speak('pulling that up for you now')
    return True

def run_search(input):
    dd_go_base_url = 'https://duckduckgo.com/?t=ffab&q='
    youtube_base_url = 'https://www.youtube.com/results?search_query='

    if input.find("search for the") != -1:
        return search_helper(input, 'the', dd_go_base_url)
    if input.find("search online for the") != -1:
        return search_helper(input, 'the', dd_go_base_url)
    if input.find("search online for") != -1:
        return search_helper(input, 'for', dd_go_base_url)
    if input.find("search the web for the") != -1:
        return search_helper(input, 'the', dd_go_base_url)
    if input.find("search the web for") != -1:
        return search_helper(input, 'for', dd_go_base_url)
    if input.find("search for videos on") != -1:
        return search_helper(input, 'on', youtube_base_url)
    if input.find("search for") != -1:
        return search_helper(input, 'for', dd_go_base_url)
    if input.find("pull up videos on") != -1:
        return search_helper(input, 'on', youtube_base_url)
    if input.find("pull up a video on") != -1:
        return search_helper(input, 'on', youtube_base_url)
    if input.find("pull up an") != -1:
        return search_helper(input, 'an', dd_go_base_url)
    if input.find("pull up") != -1:
        return search_helper(input, 'up', dd_go_base_url)
    if input.find("search youtube for videos on") != -1:
        return search_helper(input, 'on', youtube_base_url)
    if input.find("search youtube for videos with") != -1:
        return search_helper(input, 'with', youtube_base_url)
    if input.find("youtube for") != -1:
        return search_helper(input, 'for', youtube_base_url)
    if input.find("youtube") != -1:
        return search_helper(input, 'youtube', youtube_base_url)
    if input.find("search") != -1:
        return search_helper(input, 'search', dd_go_base_url)