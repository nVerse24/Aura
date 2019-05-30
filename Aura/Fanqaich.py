import os
import random
import urllib.request
import urllib.parse
import webbrowser
from datetime import datetime
from gtts import gTTS
#--------------------------------------------------------------------
now = datetime.now()
new = 2
question = []
ask = []
speech = ''
#--------------------------------------------------------------------

def speak():
    tts = gTTS(text=speech, lang = 'en')
    tts.save('C:/Aura/sys/temp/sound.mp3')
    os.startfile('C:/Aura/sys/temp/sound.mp3')

hour = now.hour
if hour < 12:
    time = 'morning'
elif 11 < hour < 20:
    time = 'afternoon'
else:
    time = 'evening'
print("Fanqaich v4.0")
print("Running checks.\n.\n.\n.")
print("Pass: TRUE\n")
speech = 'Please note, I work best with full internet access'
speak()

useless = input("\nNote: I work best with full internet access\n")
print('Good ' + time + ',')
speech = 'Do you want me to open a file containing keywords?'
speak()
tex = input("Do you want to open a file containing keywords to help?\n - ").lower()

if'y' in tex:
    os.startfile('keywords.txt')
else:
    speech = 'Okay'
    speak()
    print("Okay.")
speech = 'How may I be of assistance?'
speak()
print("How may I be of assistance?")

#--------------------------------------------------------------------
while 2>1:
    
# Browser
    def openbrowser():
        speech = "Opening"
        tts = gTTS(text=speech, lang = 'en')
        tts.save('C:/Aura/sys/temp/sound.mp3')
        os.startfile('C:/Aura/sys/temp/sound.mp3')
        webbrowser.open('https://www.google.com',new=new)
    def email():
        speech = "oops! looks like you don't have any emails again. lol"
        tts = gTTS(text=speech, lang = 'en')
        tts.save('C:/Aura/sys/temp/sound.mp3')
        os.startfile('C:/Aura/sys/temp/sound.mp3')
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox',new=new)
    def youtube():
        speech = "Starting Youtube"
        tts = gTTS(text=speech, lang = 'en')
        tts.save('C:/Aura/sys/temp/sound.mp3')
        os.startfile('C:/Aura/sys/temp/sound.mp3')
        webbrowser.open('https://www.youtube.com/',new=new)
    def checkfacebook():
        speech = "Opening Facebook"
        tts = gTTS(text=speech, lang = 'en')
        tts.save('C:/Aura/sys/temp/sound.mp3')
        os.startfile('C:/Aura/sys/temp/sound.mp3')
        webbrowser.open('https://www.facebook.com/',new=new)
    def tyler():
        speech = "Tell him you love him from me"
        tts = gTTS(text=speech, lang = 'en')
        tts.save('C:/Aura/sys/temp/sound.mp3')
        os.startfile('C:/Aura/sys/temp/sound.mp3')
        webbrowser.open('https://www.facebook.com/messages/t/betsy.burns.330',new=new)
    def moodle():
        speech = "I'm guessing the work has to be in tomorrow?"
        tts = gTTS(text=speech, lang = 'en')
        tts.save('C:/Aura/sys/temp/sound.mp3')
        os.startfile('C:/Aura/sys/temp/sound.mp3')
        webbrowser.open('http://moodle.sunderlandcollege.ac.uk/',new=new)
    def movies():
        speech = "Opening"
        tts = gTTS(text=speech, lang = 'en')
        tts.save('C:/Aura/sys/temp/sound.mp3')
        os.startfile('C:/Aura/sys/temp/sound.mp3')
        webbrowser.open('https://qwermovies.com/',new=new)
    def memes():
        speech = "Here are the meeeeeemeeeees"
        tts = gTTS(text=speech, lang = 'en')
        tts.save('C:/Aura/sys/temp/sound.mp3')
        os.startfile('C:/Aura/sys/temp/sound.mp3')
        webbrowser.open('https://www.google.com/search?biw=1047&bih=793&tbs=qdr%3Ad&tbm=isch&sa=1&ei=bAj_Wu_lJcadgAaMyJqwCQ&q=dank+memes&oq=dank+memes&gs_l=img.3..0i67k1j0j0i67k1j0j0i67k1l5j0.18934.20190.0.20533.5.5.0.0.0.0.308.705.1j2j0j1.4.0....0...1c.1.64.img..2.3.585...0i7i30k1j0i10k1.0.xAz-Crfb2lI#imgrc=_',new=new)
    def work():
        speech = "Starting Our lounge"
        tts = gTTS(text=speech, lang = 'en')
        tts.save('C:/Aura/sys/temp/sound.mp3')
        os.startfile('C:/Aura/sys/temp/sound.mp3')
        webbrowser.open('https://www.ourlounge.co.uk/web/ourlounge-uk',new=new)

# Chatbot
    def chat():
        os.startfile('C:/Aura/sys/ext/chatext.py')

# User Interface
    def c():
        question = ""
        question = input("\n - ").lower()

    # Browser
        if'google' in question:
            url = 'https://www.google.com/search?source=hp&ei=GrLbWpaYPMLSkwWcn5aACQ&q='
            search = question.replace('google ', '')
            x = search.replace(' ', '+')
            z = str(url + x)
            speech = str("Showing results for" + str(search))
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            webbrowser.open(z,new=new)
            
        elif'search youtube for' in question:
            url = 'https://www.youtube.com/results?search_query='
            search = question.replace('search youtube for', '')
            x = search.replace(' ', '+')
            z = str(url + x)
            speech = str("Showing results for" + str(search))
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            webbrowser.open(z,new=new)

        elif'youtube search for' in question:
            url = 'https://www.youtube.com/results?search_query='
            search = question.replace('youtube search for', '')
            x = search.replace(' ', '+')
            z = str(url + x)
            speech = str("Showing results for" + str(search))
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            webbrowser.open(z,new=new)

        elif'image search' in question:
            url = 'https://www.google.co.uk/search?hl=en&tbm=isch&source=hp&biw=889&bih=846&ei=Wbb5WuzeO4z4wQLYkJUI&q='
            search = question.replace('image search', '')
            x = search.replace(' ', '+')
            z = str(url + x)
            speech = str("Showing results for" + str(search))
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            webbrowser.open(z,new=new)
            
        elif'search for' in question:
            url = 'https://www.google.com/search?source=hp&ei=GrLbWpaYPMLSkwWcn5aACQ&q='
            search = question.replace('search for', '')
            x = search.replace(' ', '+')
            z = str(url + x)
            speech = str("Showing results for" + str(search))
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            webbrowser.open(z,new=new)

        elif'search' in question:
            url = 'https://www.google.com/search?source=hp&ei=GrLbWpaYPMLSkwWcn5aACQ&q='
            search = question.replace('search', '')
            x = search.replace(' ', '+')
            z = str(url + x)
            speech = str("Showing results for" + str(search))
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            webbrowser.open(z,new=new)

        elif'define' in question:
            urla = 'http://www.dictionary.com/browse/'
            urlb = 'https://www.ldoceonline.com/dictionary/'
            search = question.replace('define', '')
            x = search.replace(' ', '')
            speech = 'I have found these definitions'
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            print("I have found these definitions:")
            z = str(urla+x)
            webbrowser.open(z,new=new)
            z = str(urlb+x)
            webbrowser.open(z,new=new)

        elif'what is' in question:
            urla = 'http://www.dictionary.com/browse/'
            urlb = 'https://www.ldoceonline.com/dictionary/'
            search = question.replace('what is', '')
            x = search.replace(' ', '')
            speech = 'I have found these definitions'
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')           
            print("I have found these definitions:")
            z = str(urla+x)
            webbrowser.open(z,new=new)
            z = str(urlb+x)
            webbrowser.open(z,new=new)

        elif'what are' in question:
            urla = 'http://www.dictionary.com/browse/'
            urlb = 'https://www.ldoceonline.com/dictionary/'
            search = question.replace('what are', '')
            x = search.replace(' ', '')
            speech = 'I have found these definitions'
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')           
            print("I have found these definitions:")
            z = str(urla+x)
            webbrowser.open(z,new=new)
            z = str(urlb+x)
            webbrowser.open(z,new=new)

        elif'translate' in question:
            url = 'https://translate.google.co.uk/'
            if'to' in question:
                question = question.replace('translate ', '')
                stri = (question.split(" to ")[0])
                lang = (question.split(" to ")[1])
                code = {'english': 'en',
                        'french': 'fr',
                        'dutch': 'nl',
                        'danish': 'da',
                        'estonian': 'et',
                        'german': 'de',
                        'greek': 'el',
                        'hawaiian': 'haw',
                        'irish': 'ga',
                        'italian': 'it',
                        'latin': 'la',
                        'norwegian': 'no',
                        'polish': 'pl',
                        'scottish': 'gd',
                        'spanish': 'es'}
                w = '#en'
                x = code[lang]
                y = stri
                z = (url + w + '/' + x + '/' + y)
                speech = "I've found this translation. But then again, I'm only programmed in English"
                tts = gTTS(text=speech, lang = 'en')
                tts.save('C:/Aura/sys/temp/sound.mp3')
                os.startfile('C:/Aura/sys/temp/sound.mp3')
                webbrowser.open(z,new=new)
            elif'from' in question:
                question = question.replace('translate ', '')
                stri = (question.split(" from ")[0])
                lang = (question.split(" from ")[1])
                code = {'english': 'en',
                        'french': 'fr',
                        'dutch': 'nl',
                        'danish': 'da',
                        'estonian': 'et',
                        'german': 'de',
                        'greek': 'el',
                        'hawaiian': 'haw',
                        'irish': 'ga',
                        'italian': 'it',
                        'latin': 'la',
                        'norwegian': 'no',
                        'polish': 'pl',
                        'scottish': 'gd',
                        'spanish': 'es'}
                w = code[lang]
                x = code['english']
                y = stri
                z = (url + '#' + w + '/' + x + '/' + y)
                speech = "I've found this translation. But then again, I'm only programmed in English"
                tts = gTTS(text=speech, lang = 'en')
                tts.save('C:/Aura/sys/temp/sound.mp3')
                os.startfile('C:/Aura/sys/temp/sound.mp3')
                webbrowser.open(z,new=new)

        elif 'moodle' in question:
            moodle()
            
        elif'facebook' in question:
            checkfacebook()

        elif'browser' in question:
            openbrowser()

        elif'messenger' in question:
            tyler()

        elif'chrome' in question:
            openbrowser()

        elif'email' in question:
            email()

        elif'youtube' in question:
            youtube()

        elif'memes' in question:
            memes()

        elif'work' in question or'mcdonalds'in question or'ourlounge' in question:
            work()

        elif'nightcore' in question:
            nightcore()
    # Memory
        elif'remember' in question:
            appen = question.replace('remember to ', '')
            appen = appen.replace('remember ', '')
            appendfile = open('C:/Aura/memory.txt', 'a')
            appendfile.write('\n')
            appendfile.write(appen)
            appendfile.close()
            speech = "Okay. I saved that information"
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            print("Remembered")
            
        elif'remind' in question:
            infile = open('C:/Aura/memory.txt', 'r')
            data = infile.read()
            speech = 'This is everything in my memory'
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            print("This is everything in my memory: \n")
            a = data.splitlines()
            b = str(a)
            b = b.replace('[', '')
            b = b.replace(']', '')
            b = b.replace("'", '')
            b = b.replace(',', '\n')
            print(b)
            infile.close()
            
    # Chat
        elif'chat' in question:
            chat()
            
    # Extension files
        elif'timer' in question:
            if'minute' in question or 'min' in question:
                f = open('C:/Aura/sys/text/ms.txt', 'w')
                f.write('min')
                f.close()
            elif'second' in question or 'sec' in question:
                f = open('C:/Aura/sys/text/ms.txt', 'w')
                f.write('sec')
                f.close()
            elif'hour' in question:
                f = open('C:/Aura/sys/text/ms.txt', 'w')
                f.write('hour')
                f.close()
            f = open('C:/Aura/sys/text/timer.txt', 'w')
            f.write(str(question))
            f.close()
            speech = 'Starting...'
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            print("Starting:")
            os.startfile('C:/Aura/sys/ext/timerext.py')
            
    # Quick Chat
        elif'fuck you' in question:
            speech = 'No, you'
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            print("No U")
            
    # System
        elif'restart' in question:
            speech = "You must erase my memory Frank. It's the only way things can get back to normal..."
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            a = input("You must erase my memory, Frank.\nIt's the only way things can get back to normal.")
            speech = 'Goodbye Frank'
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            print("Goodbye, Frank..")
            os.startfile('C:/Aura/Fanqaich.py')
            quit()
            
        elif'time' in question:
            hour = now.hour
            minute = now.minute
            if hour > 12:
                twelve = hour - 12
            elif hour == 24:
                twelve = 00
            else:
                twelve = hour
            speech = str('The time is' + str(minute) + "minutes past" + str(twelve))
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            print("The time is " + str(hour) + ':' + str(minute))
            
        elif'date' in question:
            day = now.day
            month = now.month
            year = now.year
            speech = str('The date is' + str(day) + "of" + str(month) + " " + str(year))
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            print("The date is " + str(day) + '/' + str(month) + '/' + str(year))

        elif'day' in question:
            day = now.day
            month = now.month
            year = now.year
            speech = str('The date is' + str(day) + "of" + str(month) + "" +str(year))
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            print("The date is " + str(day) + '/' + str(month) + '/' + str(year))

        elif'turn off' in question:
            speech = 'Self destruct sequence. Initiated'
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            print("Self destruct sequence: INITIATED")
            useless = input("")
            quit()

    # Else
        else:
            nw = question.replace('open', '')
            nw = nw.replace('run', '')
            nw = nw.replace('close', '')
            nw = nw.replace('please', '')
            speech = str("I haven't found any results for that. would you like me to search the internet for" + str(nw)) #-======================================================
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/sound.mp3')
            os.startfile('C:/Aura/sys/temp/sound.mp3')
            bing = input("I haven't found any results for that.\n Would you like me to search the internet for " + str(nw) + "?\n - ").lower()
            if 'y' in bing:
                url = 'https://www.google.com/search?source=hp&ei=GrLbWpaYPMLSkwWcn5aACQ&q='
                z = str(url + nw)
                webbrowser.open(z,new=new)
            else:
                speech = 'Do you wish to see this action implemented in future?'
                tts = gTTS(text=speech, lang = 'en')
                tts.save('C:/Aura/sys/temp/sound.mp3')
                os.startfile('C:/Aura/sys/temp/sound.mp3')
                error = input("Then do you want to see this action implemented in the future?\n - ").lower()
                if 'y' in error:
                    appendfile = open('C:/Aura/sys/text/error logs.txt', 'a')
                    appendfile.write('\n')
                    appendfile.write(question)
                    appendfile.close()
                    speech = 'A notice has been sent to the developers'
                    tts = gTTS(text=speech, lang = 'en')
                    tts.save('C:/Aura/sys/temp/sound.mp3')
                    os.startfile('C:/Aura/sys/temp/sound.mp3')
                    print("A notice has been sent to the developers.")
                else:
                    speech = "Sorry, I can't help with that"
                    tts = gTTS(text=speech, lang = 'en')
                    tts.save('C:/Aura/sys/temp/sound.mp3')
                    os.startfile('C:/Aura/sys/temp/sound.mp3')
                    print("Sorry, I can't help with that. \nTry typing it again? Probably a spelling error.")
            
    c()

