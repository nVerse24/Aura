import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say anything\n - ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(str(text))
    except:
        print("ME NO UNDERSTAND")
        
