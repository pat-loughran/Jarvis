from Speak import speak

def run_intro(input):
    if input.find('bring yourself online') != -1:
        speak("Hello Patrick, ready at your command")
        return True
    if input.find('spring yourself online') != -1:
        speak("Hello Patrick, ready at your command")
        return True
    if input.find('who are you') != -1:
        speak("I am Jarvis, " + 
        "I am a virtual assistant that Patrick created to run his systems, " +
        "I was born on January fifth, two thousand and twenty two.")
        return True
        
    