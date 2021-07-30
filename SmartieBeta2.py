import random as r
import time
import datetime
import webbrowser
import os
import subprocess
import json
import requests
from datetime import date

today = date.today()
wday = today.weekday()
def nowtime():
  ctime = datetime.datetime.now()
  cmin = ctime.minute
  if cmin == 0:
    str(cmin)
    cmin = '00'
  chour = ctime.hour + 1
  if chour == chour > 13:
      chour = chour - 12
      print(chour, ':', cmin, 'PM')
  else:
      chour = chour
      print(chour, ':', cmin, 'AM')

if wday == 0:
    wday = 'Monday'
elif wday == 1:
    wday = 'Tuesday'
elif wday == 2:
    wday = 'Wednesday'
elif wday == 3:
    wday = 'Thursday'
elif wday == 4:
    wday = 'Friday'
elif wday == 5:
    wday = 'Saturday'
else:
    wday = 'Sunday'

if today.month == 1:
    month = 'January'
elif today.month == 2:
    month = 'February'
elif today.month == 3:
    month = 'March'
elif today.month == 4:
    month = 'April'
elif today.month == 5:
    month = 'May'
elif today.month == 6:
    month = 'June'
elif today.month == 7:
    month = 'July'
elif today.month == 8:
    month = 'August'
elif today.month == 9:
    month = 'September'
elif today.month == 10:
    month = 'october'
elif today.month == 11:
    month = 'November'
else:
    month = 'December'


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        print("Hello,Good Afternoon")
    else:
        print("Hello,Good Evening")
    print('The date today is:', today.day, month, today.year)
    print('The day today is', wday)
    nowtime()


print(
    "Loading Smartie version 0.0.1 Alpha UwU. I am currently not sorking at full capacity due to errors, but don't worry, a patch is being worked on and we will soon be finished and back to normal."
)
print('                                           ')
print('                                           ')
print('                                           ')
print('                                           ')

print(
    'Ask me "Who are you?", "Tell me some quotes", "Tell me a joke" or "Who made you?" if you want to see some of my early features.'
)
print('                                           ')
print('                                           ')
print('                                           ')

wishMe()

while True:
    print('                                           ')
    print('                                           ')
    print('                                           ')
    print('                                           ')
    print("How can I help you now?")
    inputString = input('Type Human...          ')
    inputString = str(inputString)

    inputString = inputString.lower()
    print('                                           ')

    if inputString == 0:
        continue

    if 'good bye' in inputString or "ok bye" in inputString or "stop" in inputString or 'bye' in inputString:
        print('Your personal assistant Smartie is shutting down, Good bye')
        break

    elif 'who are you' in inputString or 'what can you do' in inputString:
        print(
            'I am Smartie v0.0.1 Alpha, your persoanl assistant. I am programmed to complete minor tasks like'
        )
        time.sleep(5)
        print(
            'ermmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm'
        )
        time.sleep(5)
        print(
            '......... Not much to be honest but I am only in alpha stage UwU!'
        )

    elif "who made you" in inputString or "who created you" in inputString or "who discovered you" in inputString or "made" in inputString:
        ran = r.randint(1, 15)
        if ran == 37:
            print("UwU Daddy Loukas built me. Hehe. ^*^")
        else:
            print("I was built by Loukas")

    elif "joke" in inputString:
        j1 = "Yo momma so dumb, she tried to surf the microwave!"
        j2 = "Why are frogs always so happy? They eat what ever bugs them!"
        j3 = 'I went down the street to a 24-hour grocery store. When I got there, the guy was locking the front door. I said, "Hey! The sign says you are open 24 hours." He Said, "Yes, but not in a row!"'
        j4 = "Yo mama is so ugly she made my happy meal cry!"
        j5 = "I couldn't figure out why the ball kept getting larger. Then it hit me."
        j6 = "Yo mama so fat, she doesn't need internet, she's already worldwide."
        j7 = "I’m so bored that I just memorized six pages of the dictionary. I learned next to nothing."
        rannum = r.randint(1, 7)
        if rannum == 1:
            print(j1)
        elif rannum == 2:
            print(j2)
        elif rannum == 3:
            print(j3)
        elif rannum == 4:
            print(j4)
        elif rannum - -5:
            print(j5)
        elif rannum == 6:
            print(j6)
        else:
            print(j7)
       

    elif 'hello' in inputString or "hi" in inputString or "stop" in inputString:
        print('Hello!')

    elif 'time' in inputString:
        nowtime()

    elif 'youtube' in inputString:
            webbrowser.open_new_tab("https://www.youtube.com")
            print('Good watching!')

    elif 'bing' in inputString:
            webbrowser.open_new_tab("https://www.bing.com")
            print("Enjoy!")

    elif 'quote' in inputString:
            print('Copy and Paste ;)')
            time.sleep(0.3)
            print("Just killed a woman, feeling good! -- Tommyinnit")
            time.sleep(0.5)
            print("YOOOOOOOOOOOOOOO SUCK IT GREEENNN BOIIIIIIIIIIIIIIII -- Wilbur soot")
            time.sleep(0.5)
            print("I HOPE YOU ALL STARVE! -- Nihachu")
            time.sleep(0.5)
            print("Egg, Mouth, OMMM -- Tubbo")
            time.sleep(0.5)
            print("AMERICA -- Ranboo")
            time.sleep(0.5)
            print('I AM A PICKLE -- Fresh')

    elif 'just killed a woman' in inputString:
            print('YT -- 0')
            print('TWITCH -- 1')
            yot = int(input('0 or 1?'))
            if yot == 0:
              webbrowser.open_new_tab("https://www.youtube.com/channel/UC5p_l5ZeB_wGjO_yDXwiqvw")
            else:
              webbrowser.open_new_tab("https://www.twitch.tv/tommyinnit")
            print("Enjoy!")

    elif 'suck it' in inputString:
            print('YT -- 0')
            print('TWITCH -- 1')
            yot = int(input('0 or 1?'))
            if yot == 0:
                webbrowser.open_new_tab("https://www.youtube.com/channel/UC1n_PfsVqxllCcnMPlxBIjwt")
            else:
                webbrowser.open_new_tab("https://www.twitch.tv/wilbursoot")
            print("Enjoy!")

    elif 'all starve' in inputString:
            print('YT -- 0')
            print('TWITCH -- 1')
            yot = int(input('0 or 1?'))
            if yot == 0:
                webbrowser.open_new_tab("https://www.youtube.com/channel/UC_bjOaM7jR8lmPoAmaRPPnQ")
            else:
                webbrowser.open_new_tab("https://www.twitch.tv/nihachu")
            print("Enjoy!")
            
    elif 'egg, mouth, ommm' in inputString:
            print('YT -- 0')
            print('TWITCH -- 1')
            yot = int(input('0 or 1?'))
            if yot == 0:
                webbrowser.open_new_tab("https://www.youtube.com/channel/UCAz5JW1_oryewk0eR-eP7Bw")
            else:
                webbrowser.open_new_tab("https://www.twitch.tv/tubbo")
            print("Enjoy!")

    elif 'pickle' in inputString:
            print('YT -- 0')
            print('TWITCH -- 1')
            yot = int(input('0 or 1?'))
            if yot == 0:
                webbrowser.open_new_tab("https://www.youtube.com/channel/UCqsBym4OHrzSp0Nq1eZoMIA")
            else:
                webbrowser.open_new_tab("https://www.twitch.tv/fresh")
            print("Enjoy!")

    elif 'load egirl' in inputString or 'girl' in inputString or 'uwu' in inputString:
            print('Okie! Loading up my secret personality ;)')
            os.open('SmartieBeta2.py')

    else:
        print('Please try again.')

time.sleep(3)
