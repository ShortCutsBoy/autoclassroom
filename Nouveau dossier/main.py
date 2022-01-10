import pyautogui
import webbrowser
import time
import pyperclip
from datetime import datetime
import re
import sys


data = ""
looping = True

classes = True

matiere = 0
link = ""

link_math = "https://classroom.google.com/c/MzE5ODIxOTUxMzky"
link_science = "https://classroom.google.com/c/MzE5ODMwODg1NzEx"
link_francais = "https://classroom.google.com/c/MzE5ODM4NjUxMDc2"
link_anglais = "https://classroom.google.com/c/NDAxNzMxNzYyMDY2"
link_ecr = "https://classroom.google.com/c/MzE5OTQxMjc0MTIx"
link_musique = "https://classroom.google.com/c/Mzk3NDA4OTAzOTYz"
link_educ = "https://classroom.google.com/c/NDMyMDAzMzMyNjI1"
link_histoire = "https://classroom.google.com/c/MzIwMDc5Nzg4MTA4"

while classes:
    matiere = int(input("dans quel cours va tu aller \n(1)math; \n(2)science; \n(3)francais \n(4)anglais \n(5)ECR \n(6)musique \n(7)educ \n(8)histoire(dont work) \n(9)no link \n"))

    if matiere == 1:
        link = link_math
        classes = False
    elif matiere == 2:
        link = link_science
        classes = False
    elif matiere == 3:
        link = link_francais
        classes = False
    elif matiere == 4:
        link = link_anglais
        classes = False
    elif matiere == 5:
        link = link_ecr
        classes = False
    elif matiere == 6:
        link = link_musique
        classes = False
    elif matiere == 7:
        link = link_educ
        classes = False
    elif matiere == 8:
        link = link_histoire
        classes = False
    elif matiere == 9:
        print("no class has been specify yet so be sure to have your computer open on a class")
        link = ""
        classes = False
    else:
        print("please enter a valid answer")

def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "ok"


while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")

    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

while True:
    now = datetime.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Wake Up ur class are starting!")
                    if link == "":
                        print("no link has been specify script starting the scanning")
                    else:
                        webbrowser.open(link)
                    break

while looping:

    time.sleep(5)
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')


    s = pyperclip.paste()

    with open('file.txt', 'w') as f:
        try:
            f.write(s)
        # block raising an exception
        except:
            pass


    stringToMatch = 'https://meet.google.com/'
    matchedLine = ''

    # get line
    with open('file.txt', 'r') as file:
        for line in file:
            if stringToMatch in line:
                matchedLine = line
                break

        # and write it to the file
    with open('result.txt', 'w') as file:
        file.write(matchedLine)

    with open('result.txt', 'r') as f:
        if 'https://meet.google.com/' in f.read():
            with open('result.txt', 'r') as file:
                data = file.read().rstrip()
                print(f"{data}")
                data = re.search("(?P<url>https?://[^\s]+)", data).group("url")
                print(data)
                data = data.replace('"', '')
                print(data)
                pyautogui.click(1800, 500)
                webbrowser.open(data)
                looping = False
                with open('file.txt', 'w') as f:
                    f.write("")
                with open('result.txt', 'w') as f:
                    f.write("")

                time.sleep(3)

                pyautogui.hotkey('ctrl', 'd')
                pyautogui.hotkey('ctrl', 'e')
                pyautogui.click(1410, 700)
        else:
            print("false")
            with open('file.txt', 'w') as f:
                f.write("")
            with open('result.txt', 'w') as f:
                f.write("")
            pyautogui.click(1800, 700)

            time.sleep(1)

            pyautogui.moveTo(340, 790, 1)
            pyautogui.click()
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.sleep(1)

            p = pyperclip.paste()
            pyautogui.click(1800, 500)

            if "https://meet.google.com/" in p:
                print("true")
                pyautogui.hotkey('ctrl', 'd')
                pyautogui.hotkey('ctrl', 'e')
                pyautogui.click(1410, 700)
                looping = False
            else:
                print("false")
