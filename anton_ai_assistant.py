import pyttsx3 # for text-to-speech
import datetime # for date and time
import speech_recognition as sr # to listen
import wikipedia # to search on wiki
import smtplib # to send email
import webbrowser as wb # for searching
import os # for all computer tasks -> shut down/restart
import pyautogui # for screenshots
import psutil # for cpu usage & battery
import pyjokes # for jokes.. DUH!
import requests # for local-host check
import socket # for connectivity check

engine = pyttsx3.init()

brother_name = "Kyle"
brother_dob = "Twenty Seventh of March Nineteen Ninety eight"
brother_email = "abc@gmail.com"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("And the current time is ")
    speak(Time)

def date():
    Year = int(datetime.datetime.now().year)
    Month = int(datetime.datetime.now().month)
    Date = int(datetime.datetime.now().day)
    speak("Today is ")
    speak(Date)
    speak(Month)
    speak(Year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour > 0 and hour <= 12:
        speak("Good Morning! master")
    elif hour > 12 and hour <= 17:
        speak("Good Afternoon! master")
    elif hour > 17 and hour <= 20:
        speak("Good Evening! master")
    else:
        speak("Good Night! master")
    
    speak("My name is Anton.")
    date()
    time()
    speak("How may I help you?")

email = name@domain.com
password = mypassword

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email,password)
    server.sendmail(email, to, content)
    server.close()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(query)
    except Exception as err:
        print(err)
        speak("I'm sorry I didn't quiet get that. Could you repeat?")
        return "None"
    return query

def take_screenshot():
    img = pyautogui.screenshot()
    img.save("E:/Python Practice/screenshot.png")
    return None

def cpu_usage():
    usage = str(psutil.cpu_percent(1))
    speak("CPU is at." + usage)
    return None

def battery_usage():
    usage = psutil.sensors_battery()
    speak("Battery is at")
    speak(usage.percent)
    speak("percent")
    return None

def check_localhost():
    localhost = socket.gethostbyname("localhost")
    if localhost == '127.0.0.1':
        speak("Local host seems good.")
    else:
        speak("There seems to be a problem in Local Host.")
    return None

def check_connectivity():
    request = requests.get("http://www.google.com")
    result = request.status_code
    if result == 200:
        speak("Network connectivity seems good.")
    else:
        speak("Your device might not be connected through the internet. Please check.")
    return None

def tell_a_joke():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    greeting()

    while True:
        query = take_command().lower()
        if 'time' in query:
            time()
        elif 'brother' in query and 'date of birth' in query:
            speak(brother_name + "birthday is on" + brother_dob)
        elif 'brother' in query and 'name' in query:
            speak(brother_name)
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching")
            query = query.replace("search on wikipedia", '')
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)
        elif 'send' in query and 'email' in query:
            try:
                confirmed = False
                while(not confirmed):
                    speak("What should I say?")
                    content = take_command()
                    speak(content)
                    speak("Do you want me to confirm the content of this mail?")
                    confirm = take_command()
                    if 'yes' in confirm:
                        confirmed = True
                speak("Who do you want to send this mail to?")
                recipient = take_command()
                if brother_name in recipient or 'brother' in recipient:
                    sendemail(brother_email, content)
                else:
                    speak("Please type in the mail address")
                    mail_id = input()
                    sendemail(mail_id, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")
        elif 'open' in query:
            query = query.replace("open ", '')
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            wb.get(chrome_path).open_new_tab(query + ".com")
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'music' in query or 'song' in query:
            music_dir = "C:/Users/nikun/Desktop/Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'forget' in query and 'remember' in query:
            try:
                os.remove("remember_data.txt")
                speak("Done.")
            except:
                speak("I don't even remember anything.")
        elif 'remember' in query:
            confirm = False
            data = ""
            while not confirm:
                speak("What should I remember?")
                data = take_command()
                speak("Do you want me to remember that ")
                speak(data)
                confirm_query = take_command()
                if 'yes' in confirm_query:
                    confirm = True
            file = open("remember_data.txt", 'w')
            file.write(data)
            file.close()
        elif 'do you know anything' in query:
            try:
                file = open("remember_data.txt", 'r')
                speak("Yes. I remember that " + file.read())
                file.close()
            except:
                speak("No.")
        elif 'screenshot' in query:
            take_screenshot()
            speak("screenshot saved.")

        elif 'health' in query or 'cpu' in query:
            cpu_usage()
            battery_usage()
            check_localhost()
            check_connectivity()

        elif 'joke' in query:
            tell_a_joke()
        
        elif 'offline' in query:
            quit()

        else:
            speak("I'm sorry I don't know what I can do with that.")
            
        speak("What else can I help you with?")