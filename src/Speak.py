import pyttsx3

def speak(input):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    print(input)
    engine.say(input)
    engine.runAndWait()

def main():
    speak('hello')
if __name__=="__main__":
    main()