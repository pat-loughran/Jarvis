import speech_recognition as sr

def listen_to_user(recognizer, microphone):
    audio = ''
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 500
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=1000)
    audio_str = recognizer.recognize_google(audio)
    return audio_str


def main():
    r = sr.Recognizer()
    mic = sr.Microphone()
    done = ''
    while done != 'exit':
        print('speak')
        done = listen_to_user(r, mic)
        print(done)

if __name__=="__main__":
    main()