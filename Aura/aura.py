#-------------------------------------------------------------imports
import os
import random
import urllib.request
import urllib.parse
import webbrowser
import time
import requests
import pyautogui
from bs4 import BeautifulSoup
from datetime import datetime
from gtts import gTTS
#---------------------------------------------------------definitions
now = datetime.now()
new = 2
question = []
ask = []
speech = []
results = ''
#-----------------------------------------------------welcome message
hour = now.hour
if hour < 12:
    ToD = 'morning'
elif 11 < hour < 20:
    ToD = 'afternoon'
else:
    ToD = 'evening'
weekday = datetime.today().weekday()
print("Aura v5.0")
speech = str('good' + ToD)
tts = gTTS(text=speech, lang = 'en')
tts.save('C:/Aura/sys/temp/voice.mp3')
os.startfile('C:/Aura/sys/temp/voice.mp3')
print('Good ' + str(ToD))
time.sleep(2.4)
print('Please note: I work best with full internet access')
if weekday == 0:
    os.startfile('C:/Aura/sys/temp/updatesche.mp3')
    pause = input('Do you want to update your work schedule for this week?\n - ').lower()
    if 'y' in pause:
        os.startfile('C:/Aura/sys/temp/work.mp3')
        time.sleep(3)
        webbrowser.open('https://www.peoplestuffuk.com/WFMMCDPRD/Login.jsp',new=new)
        mon = input("Any hours on monday?\n - ")
        tue = input("Any hours on tuesday?\n - ")
        wed = input("Any hours on wednesday?\n - ")
        thu = input("Any hours on thursday?\n - ")
        fri = input("Any hours on friday?\n - ")
        sat = input("Any hours on saturday?\n - ")
        sun = input("Any hours on sunday?\n - ")
        sche = (mon+":"+tue+":"+wed+":"+thu+":"+fri+":"+sat+":"+sun)
        f = open('C:/Aura/sys/text/work schedule.txt', 'w')
        f.write(sche)
        f.close()
    else:
        print("Okay")
        time.sleep(1)
os.startfile('C:/Aura/sys/temp/question.mp3')
print('How may I be of assistance?')

#-----------------------------------------------------------functions
while True:
    def openbrowser():
        os.startfile('C:/Aura/sys/temp/opening.mp3')
        webbrowser.open('https://www.google.com',new=new)
    def email():
        os.startfile('C:/Aura/sys/temp/email.mp3')
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox',new=new)
    def youtube():
        os.startfile('C:/Aura/sys/temp/yt.mp3')
        webbrowser.open('https://www.youtube.com/',new=new)
    def checkfacebook():
        os.startfile('C:/Aura/sys/temp/fb.mp3')
        webbrowser.open('https://www.facebook.com/',new=new)
    def tyler():
        os.startfile('C:/Aura/sys/temp/tyler.mp3')
        webbrowser.open('https://www.facebook.com/messages/t/betsy.burns.330',new=new)
    def moodle():
        os.startfile('C:/Aura/sys/temp/moodle.mp3')
        webbrowser.open('http://moodle.sunderlandcollege.ac.uk/',new=new)
    def memes():
        os.startfile('C:/Aura/sys/temp/memes.mp3')
        webbrowser.open('https://www.google.com/search?biw=1047&bih=793&tbs=qdr%3Ad&tbm=isch&sa=1&ei=bAj_Wu_lJcadgAaMyJqwCQ&q=dank+memes&oq=dank+memes&gs_l=img.3..0i67k1j0j0i67k1j0j0i67k1l5j0.18934.20190.0.20533.5.5.0.0.0.0.308.705.1j2j0j1.4.0....0...1c.1.64.img..2.3.585...0i7i30k1j0i10k1.0.xAz-Crfb2lI#imgrc=_',new=new)
    def work():
        os.startfile('C:/Aura/sys/temp/work.mp3')
        webbrowser.open('https://www.ourlounge.co.uk/web/ourlounge-uk',new=new)
    def chat():
        os.startfile('C:/Aura/sys/ext/chatext.py')        

#------------------------------------------------------user interface
    def interface():
        question = ''
        question = input("\n - ").lower()
        question = question.replace("'", '')

        if 'repeat' in question or 'say that again' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'r')
            question = f.readlines()
            f.close()
        else:
            useless = 0
#-------------------------------------------------------open commands
        if 'open' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            if 'browser' in question or 'chrome' in question or 'google' in question:
                openbrowser()
            elif 'email' in question or 'gmail' in question or 'google mail' in question:
                email()
            elif 'youtube' in question or 'yt' in question or 'you tube' in question:
                youtube()
            elif 'facebook' in question or 'face book' in question or 'fb' in question:
                checkfacebook()
            elif 'messenger' in question or 'messages' in question or 'texts' in question:
                os.startfile('C:/Aura/sys/temp/messenger.mp3')
                webbrowser.open('https://www.facebook.com/messages/',new=new)
            elif 'moodle' in question or 'college' in question:
                moodle()
            elif 'work' in question or 'ourlounge' in question or 'our lounge' in question or 'mcdonalds' in question:
                work()
            elif 'keywords' in question:
                os.startfile("C:/Aura/keywords.txt")
            elif 'autocad' in question:
                os.startfile("C:/Aura/sys/programs/autocad.lnk")
            elif 'excel' in question:
                os.startfile("C:/Aura/sys/programs/excel.lnk")
            elif 'gimp' in question:
                os.startfile("C:/Aura/sys/programs/gimp.lnk")
            elif 'idle' in question:
                os.startfile("C:/Aura/sys/programs/idle.lnk")
            elif 'inventor' in question:
                os.startfile("C:/Aura/sys/programs/inventor/lnk")
            elif 'minecraft' in question:
                os.startfile("C:/Aura/sys/programs/minecraft.lnk")
            elif 'roblox' in question:
                os.startfile("C:/Aura/sys/programs/roblox.lnk")
            elif 'word' in question:
                os.startfile("C:/Aura/sys/programs/word.lnk")
            else:
                nw = question.replace('open', '')
                nw = nw.replace('run', '')
                nw = nw.replace('close', '')
                nw = nw.replace('please', '')
                speech = str(nw)
                tts = gTTS(text=speech, lang = 'en')
                tts.save('C:/Aura/sys/temp/voice.mp3')
                os.startfile('C:/Aura/sys/temp/elsesearch.mp3')
                bing = input("I haven't found any results for that.\n Would you like me to search the internet for " + str(nw) + "?\n - ").lower()
                time.sleep(5.5)
                os.startfile('C:/Aura/sys/temp/voice.mp3')
                if 'y' in bing:
                    url = 'https://www.google.com/search?source=hp&ei=GrLbWpaYPMLSkwWcn5aACQ&q='
                    z = str(url + nw)
                    webbrowser.open(z,new=new)
                else:
                    os.startfile('C:/Aura/sys/temp/elsedev.mp3')
                    error = input("Then do you want to see this action implemented in the future?\n - ").lower()
                    if 'y' in error:
                        appendfile = open('C:/Aura/sys/text/error logs.txt', 'a')
                        appendfile.write('\n')
                        appendfile.write(question)
                        appendfile.close()
                        os.startfile('C:/Aura/sys/temp/devreq.mp3')
                        print("A notice has been sent to the developers.")
                    else:
                        os.startfile('C:/Aura/sys/temp/else.mp3')
                        print("Sorry, I can't help with that. \nTry typing it again? Probably a spelling error.")
#------------------------------------------------------start commands
        elif 'start' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            if 'browser' in question or 'chrome' in question or 'google' in question:
                openbrowser()
            elif 'youtube' in question or 'yt' in question:
                youtube()
            elif 'facebook' in question or 'face book' in question or 'fb' in question:
                checkfacebook()
            elif 'messenger' in question or 'messages' in question or 'texts' in question:
                os.startfile('C:/Aura/sys/temp/messenger.mp3')
                webbrowser.open('https://www.facebook.com/messages/',new=new)
            elif 'moodle' in question or 'college' in question:
                moodle()
            elif 'work' in question or 'ourlounge' in question or 'our lounge' in question or 'mcdonalds' in question:
                work()
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
                os.startfile('C:/Aura/sys/temp/starting.mp3')
                print("Starting:")
                os.startfile('C:/Aura/sys/ext/timerext.py')
            elif 'chat' in question:
                chat()
            else:
                useless = 0
#---------------------------------------------------question commands
        elif 'what is' in question or "whats" in question or "what are" in question or "whatre" in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            if 'time' in question:
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
            elif 'date' in question or 'day' in question:
                day = now.day
                month = now.month
                year = now.year
                speech = str('The date is' + str(day) + "of" + str(month) + " " + str(year))
                tts = gTTS(text=speech, lang = 'en')
                tts.save('C:/Aura/sys/temp/sound.mp3')
                os.startfile('C:/Aura/sys/temp/sound.mp3')
                print("The date is " + str(day) + '/' + str(month) + '/' + str(year))
            elif 'work' in question:
                infile = open('C:/Aura/sys/text/work schedule.txt', 'r')
                data = infile.read()
                mon = (data.split(":") [0])
                tue = (data.split(":") [1])
                wed = (data.split(":") [2])
                thu = (data.split(":") [3])
                fri = (data.split(":") [4])
                sat = (data.split(":") [5])
                sun = (data.split(":") [6])
                if mon != 'no':
                    print("Monday: " + str(mon))
                else:
                    useless = 0
                if tue != 'no':
                    print("Tuesday: " + str(tue))
                else:
                    useless = 0
                if wed != 'no':
                    print("Wednesday: " + str(wed))
                else:
                    useless = 0
                if thu != 'no':
                    print("Thursday: " + str(thu))
                else:
                    useless = 0
                if fri != 'no':
                    print("Friday: " + str(fri))
                else:
                    useless = 0
                if sat != 'no':
                    print("Saturday: " + str(sat))
                else:
                    useless = 0
                if sun != 'no':
                    print("Sunday: " + str(sun))
                else:
                    useless = 0
                infile.close()

            else:
                urla = 'http://www.dictionary.com/browse/'
                urlb = 'https://www.ldoceonline.com/dictionary/'
                search = question.replace('define', '')
                search = search.replace('what is', '')
                search = search.replace("what's", '')
                search = search.replace('what are', '')
                x = search.replace("what're", '')
                os.startfile('C:/Aura/sys/temp/define.mp3')
                print("I have found these definitions:")
                z = str(urla+x)
                webbrowser.open(z,new=new)
                z = str(urlb+x)
                webbrowser.open(z,new=new)
        
        elif 'when' in question: #=======================================================================================================================
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            weekday = 4 #####datetime.today().weekday()
            if 'work' in question:
                days = {0: '',
                        1: '',
                        2: '',
                        3: '',
                        4: '',
                        5: '',
                        6: ''}
                infile = open('C:/Aura/sys/text/work schedule.txt', 'r')
                data = infile.read()
                days[0] = (data.split(":") [0])
                days[1] = (data.split(":") [1])
                days[2] = (data.split(":") [2])
                days[3] = (data.split(":") [3])
                days[4] = (data.split(":") [4])
                days[5] = (data.split(":") [5])
                days[6] = (data.split(":") [6])
                infile.close()
                stop = False
                i = 0
                while stop == False:
                    if days[i] != 'no' and i > weekday:
                        if i == 0:
                            d = 'Monday'
                        elif i == 1:
                            d = 'Tuesday'
                        elif i == 2:
                            d = 'Wednesday'
                        elif i == 3:
                            d = 'Thursday'
                        elif i == 4:
                            d = 'Friday'
                        elif i == 5:
                            d = 'Saturday'
                        elif i == 6:
                            d = 'Sunday'
                        print("You work on " + d + " at " + days[i])
                        stop = True
                        i = 0
                    else:
                        useless = 0
                        i = i + 1
                
        elif 'translate' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
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
                os.startfile('C:/Aura/sys/temp/translate.mp3')
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
                os.startfile('C:/Aura/sys/temp/translate.mp3')
                webbrowser.open(z,new=new)
            else:
                useless = 0
                    
#-------------------------------------------------------play commands
        elif'play' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            search = question.replace('play', '')
            x = search.replace(' ', '+')
            url = str('https://www.ecosia.org/videos?q=' + x)
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            results = soup.find('a', attrs={'class':'result-url result-url-video'})
            results = str(results)
            results = results.replace('<a class="result-url result-url-video" href="', '')
            results = results.replace('</a>', '')
            results = results.replace(' ', '')
            results = results.replace('>', '')
            results = results.replace('"', '')
            charnum = len(results)
            half = charnum/2
            half = int(half)
            url = results[0:(half)]
            speech = question.replace('play', '')
            speech = str(speech)
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/voice.mp3')
            os.startfile('C:/Aura/sys/temp/nowplaying.mp3')
            time.sleep(1.5)
            os.startfile('C:/Aura/sys/temp/voice.mp3')
            print("Now playing " + speech)
            webbrowser.open(url,new=new)

#-----------------------------------------------------search commands
        elif'search youtube for' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            url = 'https://www.youtube.com/results?search_query='
            search = question.replace('search youtube for', '')
            x = search.replace(' ', '+')
            z = str(url + x)
            speech = str(search)
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/voice.mp3')
            os.startfile('C:/Aura/sys/temp/results.mp3')
            time.sleep(1.5)
            os.startfile('C:/Aura/sys/temp/voice.mp3')
            webbrowser.open(z,new=new)
        elif'youtube search for' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            url = 'https://www.youtube.com/results?search_query='
            search = question.replace('youtube search for', '')
            x = search.replace(' ', '+')
            z = str(url + x)
            speech = str(search)
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/voice.mp3')
            os.startfile('C:/Aura/sys/temp/results.mp3')
            time.sleep(1.5)
            os.startfile('C:/Aura/sys/temp/voice.mp3')
            webbrowser.open(z,new=new)
        elif'image search' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            url = 'https://www.google.co.uk/search?hl=en&tbm=isch&source=hp&biw=889&bih=846&ei=Wbb5WuzeO4z4wQLYkJUI&q='
            search = question.replace('image search', '')
            search = search.replace('for', '')
            x = search.replace(' ', '+')
            z = str(url + x)
            speech = str(search)
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/voice.mp3')
            os.startfile('C:/Aura/sys/temp/results.mp3')
            time.sleep(1.5)
            os.startfile('C:/Aura/sys/temp/voice.mp3')
            webbrowser.open(z,new=new)
        elif 'search for' in question or 'google for' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            url = 'https://www.google.com/search?source=hp&ei=GrLbWpaYPMLSkwWcn5aACQ&q='
            search = question.replace('google for ', '')
            search = search.replace('search for ', '')
            x = search.replace(' ', '+')
            z = str(url + x)
            speech = str(search)
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/voice.mp3')
            os.startfile('C:/Aura/sys/temp/results.mp3')
            time.sleep(1.5)
            os.startfile('C:/Aura/sys/temp/voice.mp3')
            webbrowser.open(z,new=new)
        elif 'google' in question or 'search' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            url = 'https://www.google.com/search?source=hp&ei=GrLbWpaYPMLSkwWcn5aACQ&q='
            search = str(question).replace('google ', '')
            search = str(search).replace('search ', '')
            x = search.replace(' ', '+')
            z = str(url + x)
            speech = str(search)
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/voice.mp3')
            os.startfile('C:/Aura/sys/temp/results.mp3')
            time.sleep(1.5)
            os.startfile('C:/Aura/sys/temp/voice.mp3')
            webbrowser.open(z,new=new)
#--------------------------------------------------------sys commands
        elif'remember' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            appen = question.replace('remember to ', '')
            appen = appen.replace('remember ', '')
            appendfile = open('C:/Aura/memory.txt', 'a')
            appendfile.write('\n')
            appendfile.write(appen)
            appendfile.close()
            os.startfile('C:/Aura/sys/temp/remember.mp3')
            print("Remembered") 
        elif'remind' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            infile = open('C:/Aura/memory.txt', 'r')
            data = infile.read()
            os.startfile('C:/Aura/sys/temp/remind.mp3')
            print("This is everything in my memory: \n")
            a = data.splitlines()
            b = str(a)
            b = b.replace('[', '')
            b = b.replace(']', '')
            b = b.replace("'", '')
            b = b.replace(',', '\n')
            print(b)
            infile.close()
        elif'reset' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            os.startfile('C:/Aura/sys/temp/restart.mp3')
            pause = input('Press enter to restart.\n - ')
            os.startfile('C:/Aura/aura.py')
            quit()
        elif'turn off' in question or 'shut down' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            os.startfile('C:/Aura/sys/temp/off.mp3')
            print("Self destruct sequence: INITIATED")
            pause = input("")
            os.startfile('C:/Aura/sys/sounds/explosion.mp3')
            quit()
#------------------------------------------------------other commands
        elif'fuck you' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            os.startfile('C:/Aura/sys/temp/nou.mp3')
            print("No U")
        elif'thanks' in question:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            print("You're welcome")#================================================================================================================================================
#-----------------------------------------------------error statement
        else:
            f = open('C:/Aura/sys/temp/repeat.txt', 'w')
            f.write(str(question))
            f.close()
            question = str(question)
            nw = question.replace('open', '')
            nw = nw.replace('run', '')
            nw = nw.replace('close', '')
            nw = nw.replace('please', '')
            speech = str(nw)
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:/Aura/sys/temp/voice.mp3')
            os.startfile('C:/Aura/sys/temp/elsesearch.mp3')
            bing = input("I haven't found any results for that.\n Would you like me to search the internet for " + str(nw) + "?\n - ").lower()
            time.sleep(5.5)
            os.startfile('C:/Aura/sys/temp/voice.mp3')
            if 'y' in bing:
                url = 'https://www.google.com/search?source=hp&ei=GrLbWpaYPMLSkwWcn5aACQ&q='
                z = str(url + nw)
                webbrowser.open(z,new=new)
            else:
                os.startfile('C:/Aura/sys/temp/elsedev.mp3')
                error = input("Then do you want to see this action implemented in the future?\n - ").lower()
                if 'y' in error:
                    appendfile = open('C:/Aura/sys/text/error logs.txt', 'a')
                    appendfile.write('\n')
                    appendfile.write(question)
                    appendfile.close()
                    os.startfile('C:/Aura/sys/temp/devreq.mp3')
                    print("A notice has been sent to the developers.")
                else:
                    os.startfile('C:/Aura/sys/temp/else.mp3')
                    print("Sorry, I can't help with that. \nTry typing it again? Probably a spelling error.")
            
#----------------------------------------------------------------loop
    interface()

