import sys
from Search import run_search
from Go_To import run_go_to
from Speak import speak
from Weather import run_weather
from Stocks import run_stocks
from Speech_To_Text import listen_to_user
from Goodbye import check_if_finished
from Intro import run_intro
from Date import run_date
import speech_recognition as sr

def main():
    #Speech_Recognizer
    r = sr.Recognizer()
    mic = sr.Microphone()

    #input
    is_done = False
    
    while is_done == False:
        print('listening')
        input = listen_to_user(r, mic)
        input = input.strip()
        input = input.lower()
        is_done = check_if_finished(input)
        if is_done:
            sys.exit(0)
        print('audio = {}'.format(input))
        done = False
        #intro
        done = run_intro(input)
        if done:
            continue
        #Search
        done = run_search(input)
        if done:
            continue
        #Go-To
        done = run_go_to(input)
        if done:
            continue
        #Weather
        done = run_weather(input)
        if done:
            continue
        #Stocks
        done = run_stocks(input)
        if done:
            continue
        #Date and Time
        done = run_date(input)
        if done:
            continue
        
        if done == False:
            speak("sorry I didn't catch that")
        
main()

