import datetime
import os
import smtplib
import sys
import time
import webbrowser
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import PyPDF2
import cv2
import pyautogui
import instaloader
import pyjokes
import pyttsx3
import pywhatkit as kit
import requests
import speech_recognition as sr
import wikipedia
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)


# text to speech


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to convert voices into text.


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.adjust_for_ambient_noise(source)                 # listen for 1 second to calibrate the energy threshold for ambient noise levels
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        #audio = r.record(source, duration=4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


# to wish


def wish():
    """
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning!")
    elif 12 < hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I help you sir?")
    """

    now = datetime.datetime.now()
    if 0 <= now.hour < 12:
        speak("Good Morning!")
        hour = now.hour
        am_pm = 'AM'
    elif 12 <= now.hour < 18:
        speak("Good Afternoon!")
        if now.hour != 12:
            hour = now.hour - 12
        am_pm = 'PM'
    else:
        speak("Good Evening!")
        hour = now.hour - 12
        am_pm = 'PM'
    speak(f"Its {hour} :{now.minute} {am_pm}.")
    speak("I am Jarvis. How can I help you sir?")



# to send emails

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.google.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email_id', 'password')
    server.sendmail('email_id', to, content)
    server.close()



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
def pdf_reader():
    book = open('py3.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)  # pip install PyPDF2
    pages = pdfReader.numPages
    speak(f"Total number of pages in this pdf is {pages}")
    speak("Sir, please enter the page number I have to read")
    pg = int(input("Enter the page number:"))
    page = pdfReader.getPAge(pg)
    text = page.extractText()
    speak(text)


def start():
    wish()
    while True:
        # if 1:

        query = takecommand().lower()

        # logic building for tasks:

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
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

        elif "ip address" in query:
            ip = get('http://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia")
            results = wikipedia.summary(query, sentences=2)
            speak("according to Wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "open google" in query:
            speak("sir, what should I search on Google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+916299481791",
                            "this is a testing protocol from Jarvis", 13, 31)

        elif "play song on youtube" in query:
            kit.playonyt("see you again")

        elif "email to me" in query:
            try:
                speak("what should I say?")
                content = takecommand().lower()
                to = "jameelk809@hotmail.com"
                sendEmail(to, content)
                speak("Email sent!")

            except Exception as e:
                print(e)
                speak("unable to send mail!")

        elif "no thanks" in query:
            speak("Thank you. have a good day!")
            sys.exit()

        elif "close notepad" in query:
            speak("Okay, closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "set an alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = "C:\\Users\\jamee\\Music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.keyDown("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()

        elif "email to Kamran" in query:
            speak("Sir, what should I say?")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'your@gmail.com'  # your email here
                password = 'your_pass'  # your email password
                send_to_email = 'person@gmail.com'  # receiver's email

                speak("Okay sir, What is the Subject?")
                query = takecommand().lower()
                subject = query

                speak("And Sir, what is the message ?")
                query2 = takecommand().lower()
                message = query2

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
                message = query  # The message in mail

                server = smtplib.SMTP('smtp.google.com', 587)  # Connect to server
                server.starttls()  # use TTL
                server.login(email, password)  # login to email server
                server.sendmail(email, send_to_email, message)  # send the mail
                server.quit()  # logout
                speak("email has been sent to Kamran")

        elif "where am I" in query or "where we are" in query:
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
        elif "instagram profile" in query or "profile on instagram" in query:
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

        elif "take screenshot" in query or "screenshot" in query:
            # speak("sir, tell me the filename for this screenshot.")
            # name = takecommand().lower()
            name = 'screenshot'
            speak("Please sir, hold the screen for few seconds, I am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Done sir! The screenshot has been saved in our main folder.")

        elif "read pdf" in query:
            pdf_reader()

        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
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

        elif "you can sleep now" in query or "sleep" in query:
            speak("Thank you. HAve a good day sir!")
            sys.exit()

        # speak("Sir, do you have any other work for me ?")


if __name__ == "__main__":
    start()
