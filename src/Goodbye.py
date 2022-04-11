from Speak import speak


def check_if_finished(input):
    if input.find('goodbye') != -1:
        speak("goodbye")
        return True
    if input.find("that's all") != -1:
        speak("goodbye")
        return True
    if input.find("that is all") != -1:
        speak("goodbye")
        return True
    if input.find("that's enough") != -1:
        speak("goodbye")
        return True
    if input.find("that is enough") != -1:
        speak("goodbye")
        return True
    if input.find("turn off") != -1:
        speak("goodbye")
        return True
    return False