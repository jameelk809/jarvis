import datetime
import operator
import os
import smtplib
import sys
import webbrowser
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import PyPDF2
import cv2
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit as kit
import requests
import speech_recognition as sr
import wikipedia
import instaloader
from requests import get
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JARVIS_basic import takecommand, pdf_reader, sendEmail
from jarvisUI import Ui_JARVIS
from bs4 import BeautifulSoup
# from pywikihow import search_wikihow
import psutil
import MyAlarm
import urllib.request
import cv2
import numpy as np
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[len(voices) - 1].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to wish
def wish():
    now = datetime.datetime.now()
    if 0 <= now.hour < 12:
        speak("Good Morning!")
        hour = now.hour
        am_pm = 'AM'
    elif 12 <= now.hour < 18:
        speak("Good Afternoon!")
        if now.hour != 12:
            hour = now.hour - 12
        else:
            hour = now.hour
        am_pm = 'PM'
    else:
        speak("Good Evening!")
        hour = now.hour - 12
        am_pm = 'PM'
    speak(f"Its {hour} :{now.minute} {am_pm}.")
    speak("I am Jarvis. How can I help you sir?")


# for news
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513'
    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ",head[i])
        speak(f"today's {day[i]} news is: {head[i]}")


# to read pdf
# def pdf_reader():
#     book = open('py3.pdf', 'rb')
#     pdfReader = PyPDF2.PdfFileReader(book)  # pip install PyPDF2
#     pages = pdfReader.numPages
#     speak(f"Total number of pages in this pdf is {pages}")
#     speak("Sir, please enter the page number I have to read")
#     pg = int(input("Enter the page number:"))
#     page = pdfReader.getPAge(pg)
#     text = page.extractText()
#     speak(text)


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        speak("Please wake me up whenever in need")
        while True:
            self.query = self.takecommand()
            if "wake up" in self.query or "are you there" in self.query or "hello" in self.query:
                self.TaskExecution()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(
                source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
            audio = r.listen(source)
            # audio = r.listen(source, timeout=5, phrase_time_limit=5)
            # audio = r.record(source, duration=4)
        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"user said: {self.query}")
        except Exception as e:
            return "none"
        self.query = self.query.lower()
        return self.query

    def TaskExecution(self):
        wish()
        while True:
            self.query = self.takecommand().lower()

            if "open notepad" in self.query:
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif "play music" in self.query:
                music_dir = "C:\\Users\\jamee\\Music"
                songs = os.listdir(music_dir)

                """
                # for playing random music
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd)
                """

                # for playing only .mp3 files.
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))

            elif "ip address" in self.query:
                ip = get('http://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia...")
                self.query = self.query.replace("wikipedia")
                results = wikipedia.summary(self.query, sentences=2)
                speak("according to Wikipedia")
                speak(results)

            elif "open youtube" in self.query:
                webbrowser.open("youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("facebook.com")

            elif "open stackoverflow" in self.query:
                webbrowser.open("stackoverflow.com")

            elif "open google" in self.query:
                speak("sir, what should I search on Google")
                cm = takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "send message" in self.query:
                kit.sendwhatmsg("+916299481791",
                                "this is a testing protocol from Jarvis", 13, 31)

            elif "play song on youtube" in self.query:
                kit.playonyt("see you again")

            elif "email to me" in self.query:
                try:
                    speak("what should I say?")
                    content = takecommand().lower()
                    to = "jameelk809@hotmail.com"
                    sendEmail(to, content)
                    speak("Email sent!")

                except Exception as e:
                    print(e)
                    speak("unable to send mail!")

            elif "close notepad" in self.query:
                speak("Okay, closing Notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "set an alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn == 22:
                    music_dir = "C:\\Users\\jamee\\Music"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.keyDown("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in self.query:
                speak("please wait sir, fetching the latest news")
                news()

            elif "email to Kamran" in self.query:
                speak("Sir, what should I say?")
                self.query = takecommand().lower()
                if "send a file" in self.query:
                    email = 'your@gmail.com'  # your email here
                    password = 'your_pass'  # your email password
                    send_to_email = 'person@gmail.com'  # receiver's email

                    speak("Okay sir, What is the Subject?")
                    self.query = takecommand().lower()
                    subject = self.query

                    speak("And Sir, what is the message ?")
                    self.query2 = takecommand().lower()
                    message = self.query2

                    speak("Sir, enter the path of the file which you want to attach")
                    file_location = input("enter the path here:")

                    speak("Please wait, I am sending your mail")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    # Setup Attachment:
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                    # Attach the attachment to the MIMEMultipart object
                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("Email has been sent to Kamran")

                else:
                    email = 'your@gmail.com'  # your email
                    password = 'your_pass'  # your email password
                    send_to_email = 'person@gmail.com'  # receiver's email
                    message = self.query  # The message in mail

                    server = smtplib.SMTP('smtp.google.com', 587)  # Connect to server
                    server.starttls()  # use TTL
                    server.login(email, password)  # login to email server
                    server.sendmail(email, send_to_email, message)  # send the mail
                    server.quit()  # logout
                    speak("email has been sent to Kamran")

            elif "do some calculations" in self.query or "can you calculate" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what you want to calculate? Example: 3 plus 3")
                    print("listening...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)

                def get_operator_fn(op):
                    return {
                        '+': operator.add,  # plus
                        '-': operator.sub,  # minus
                        '×': operator.mul,  # multiplied by
                        'divided': operator.__truediv__,  # divided
                    }[op]

                def eval_binary_expr(op1, oper, op2):  # 5 plus 3
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)

                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))

            elif "where am I" in self.query or "where we are" in self.query:
                speak("Wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print(geo_data)
                    city = geo_data['city']
                    state = geo_data['state']
                    country = geo_data['country']
                    speak(f"Sir, I am not sure, but I think we are in {city} city of {state}, {country}")
                except Exception as e:
                    speak("Sorry Sir, due to network issues, I am unable to track")
                    pass

            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak("Please enter the username correctly")
                name: str = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"here is the profile")
                time.sleep(5)
                speak("sir, would you like to download profile picture of this account?")
                condition = takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()  # pip install instaloader
                    mod.download_profile(name, profile_pic_only=True)
                    speak("I am done, Profile picture is saved in our main folder.")
                else:
                    pass

            elif "take screenshot" in self.query or "screenshot" in self.query:
                # speak("sir, tell me the filename for this screenshot.")
                # name = takecommand().lower()
                name = 'screenshot'
                speak("Please sir, hold the screen for few seconds, I am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("Done sir! The screenshot has been saved in our main folder.")

            elif "read pdf" in self.query:
                pdf_reader()

            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("Sir, please tell me if you want to hide this folder or make it visible for everyone?")
                condition = takecommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak("Sir, all teh files in this folder are now hidden.")
                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("Sir, all the files in this folder are now visible to everyone. ")
                elif "leave it" in condition or "leave for now" in condition:
                    speak("Ok Sir!")

            elif "goodbye" in self.query:
                speak("Thank you for today! Have a good day sir.")
                sys.exit()

            elif "temperature" in self.query:
                search = "temperature in Ranchi"
                url = f"https://google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp}")

            

            elif "How much power left" in self.query or "how much power we have" in self.query or "power" in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"Sir I have {percentage} percent power left")
                if percentage >= 75:
                    speak("I have enough power to continue work")
                elif percentage <= 15:
                    speak("I don't have enough power.")

            elif "internet speed" in self.query:
                import speedtest
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                speak(f"I have a {dl} bit per second downloading speed and {up} bit per second uploading speed")
                """
                # JARVIS will terminate after this execution!!
                try:
                    os.system('cmd /k ""speedtest"')
                except:
                    speak("There is no internet connection")
                """

            elif "volume up" in self.query:
                pyautogui.press("volumeup")

            elif "volume down" in self.query:
                pyautogui.press("volumedown")

            elif "volume mute" in self.query or "mute" in self.query:
                pyautogui.press("volumeumute")

            elif "set alarm" in self.query or "alarm" in self.query:
                speak("Sir, tell me the time to set the alarm. for example set alarm to 5: 30 am")
                tt = takecommand()
                tt = tt.replace("set alarm to", "")
                tt = tt.replace(".", "")
                tt = tt.upper()
                speak("Alarm has been set")
                MyAlarm.alarm(tt)

            elif "open mobile camera" in self.query:
                URL = "http://192.168.177.151:8080/shot.jpg"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                    img = cv2.imdecode(img_arr, -1)
                    cv2.imshow('IPWebcam', img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                        break;
                cv2.destroyAllWindows()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JARVIS()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/ASUS/Downloads/images/212508.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Users/ASUS/Downloads/images/00545cb7179c504433d4c8f5e845f286.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
