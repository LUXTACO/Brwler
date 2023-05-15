import os
import time
import psutil
import ctypes
import random
import requests
import pyautogui
import configparser
from pyautogui import locateOnScreen
from pynput.keyboard import Controller
from pystyle import Colorate, Colors, Center

# Variables
x = 836
y = 929
config = configparser.ConfigParser()
primary_process_name = "BrawlhallaGame.exe"
title = "Brawlhalla"
keyboard = Controller()
separator = (f"\n{Colors.pink}======{Colors.white}======{Colors.pink}======{Colors.white}======{Colors.pink}======{Colors.white}======{Colors.pink}======{Colors.white}======{Colors.pink}======{Colors.white}======{Colors.pink}======\n{Colors.white}")

# Functions

def show_window(title):
    window = pyautogui.getWindowsWithTitle(title)[0]
    window.activate()

def hide_window(title):
    window = pyautogui.getWindowsWithTitle(title)[0]
    window.minimize()
    
def wait_for_process(process_name, timeout=60):
    start_time = time.time()
    while time.time() < start_time + timeout:
        for proc in psutil.process_iter():
            if proc.name() == process_name:
                return True
        time.sleep(0.1)
    raise TimeoutError(f"{Colors.pink}Timed out waiting for process:{Colors.white} {process_name}")

def wait_for_window(title):
    while True:
        windows = pyautogui.getWindowsWithTitle(title)
        if len(windows) > 0:
            return windows[0]
        time.sleep(0.1)
        
def match_check():
    time.sleep(1)
    checker_1 = False
    image = locateOnScreen('./med/correct.png', confidence=0.8)
    if image is not None:
        checker_1 = True
    if image is None:
        checker_1 = False
    if checker_1 == True:
        print(f"{Colors.pink}Match setup is correct!{Colors.white}")
        return checker_1
    else:
        print(f"{Colors.pink}Match setup is incorrect!{Colors.white}")

def match_custom(title):
    #perso: (84, 556)
    #crear: (595, 538)
    #privada: (595, 538)
    
    show_window(title)
    image = locateOnScreen('./med/start.png', confidence=0.5)
    time.sleep(2)
    if image is not None:
        pyautogui.moveTo(84, 556, duration=(random.randint(1, 2)))
        pyautogui.click()
        pyautogui.moveTo(595, 538, duration=(random.randint(1, 2)))
        pyautogui.click()
        pyautogui.moveTo(595, 538, duration=(random.randint(1, 2)))
        pyautogui.click()
        return True
    if image is None:
        hide_window(title)
        print(f"{Colors.pink}Please return to main menu!{Colors.white}")
        wait = input(f"{Colors.pink}Press {Colors.white}ENTER{Colors.pink} to continue...{Colors.white}")
        pass
    
def add_bots():
    #bot1: (38, 258)
    #bot2: (49, 325)
    #bot3: (38, 371)
    #bot4: (42, 416)
    #bot5: (31, 461)
    #bot6: (35, 521)
    #bot7: (35, 560)
    
    print(f"{Colors.pink}Adding bots...{Colors.white}")
    show_window(title)
    image = locateOnScreen('./med/nobots.png', confidence=0.8)
    image2 = locateOnScreen('./med/allbots.png', confidence=0.8)
    if image is not None:
        pyautogui.moveTo(35, 258, duration=(random.randint(1, 2)))
        pyautogui.click()
        pyautogui.moveTo(35, 325, duration=(random.randint(1, 2)))
        pyautogui.click()
        pyautogui.moveTo(35, 371, duration=(random.randint(1, 2)))
        pyautogui.click()
        pyautogui.moveTo(35, 416, duration=(random.randint(1, 2)))
        pyautogui.click()
        pyautogui.moveTo(35, 461, duration=(random.randint(1, 2)))
        pyautogui.click()
        pyautogui.moveTo(35, 521, duration=(random.randint(1, 2)))
        pyautogui.click()
        pyautogui.moveTo(35, 560, duration=(random.randint(1, 2)))
        pyautogui.click()
        return True
    if image is None:
        image2 = locateOnScreen('./med/allbots.png', confidence=0.8)
        if image2 is not None:
            print(f"{Colors.pink}Bots are already added!{Colors.white}")
        else:
            print(f"{Colors.pink}Incorrect bot setup!{Colors.white}")
            wait = input(f"{Colors.pink}Press {Colors.white}ENTER{Colors.pink} to continue...{Colors.white}")
            time.sleep(5)
    if image2 is not None:
        print(f"{Colors.pink}Correct bot setup!{Colors.white}")
        time.sleep(3)
    else:
        print(f"{Colors.pink}Incorrect bot setup!{Colors.white}")

def choose_legend():
    #legend: (381, 165)
    
    print(f"{Colors.pink}Choosing legend...{Colors.white}")
    pyautogui.moveTo(381, 165, duration=(random.randint(1, 2)))
    pyautogui.click()
    pyautogui.click()
    image = locateOnScreen('./med/ready.png', confidence=0.8)
    if image is not None:
        print(f"{Colors.pink}Ready for battle!{Colors.white}")
        keyboard.press("c")
        return True

# Config

try:
    config.read('config.cfg')
except:
    with open('config.cfg', 'w') as f:
        f.write('[DEFAULT]\n')
        f.close()

if config['DEFAULT']:
    stp_img = config['DEFAULT']['stp_img']
    webhook = config['DEFAULT']['webhook']
else:
    stp_img = input(f"{Colors.pink}Do you want to show setup image on startup? (Y/N): {Colors.white}")
    if stp_img == "Y" or stp_img == "y":
        stp_img = True
        webhook = input(f"{Colors.pink}Enter your Discord webhook: {Colors.white}")
        with open('config.cfg', 'w') as f:
            config.set('DEFAULT', 'webhook', webhook)
            config.set('DEFAULT', 'stp_img', str(stp_img))
            config.write(f)
            f.close()
    else:
        with open('config.cfg', 'w') as f:
            config.set('DEFAULT', 'webhook', 'False')
            config.set('DEFAULT', 'stp_img', 'False')
            config.write(f)
            f.close()
    
# MainLoop

try:
    print(f"{Colors.pink}Waiting for {Colors.white}{primary_process_name}{Colors.pink} to start...{Colors.white}")
    wait_for_process(primary_process_name)
    print(f"{Colors.pink}The {Colors.white}{primary_process_name}{Colors.pink} has started!{Colors.white}")
    time.sleep(1)
    
except Exception as e:
    print(f"Error occurred: {str(e)}")
    exit()
    
try:
    print(f"{Colors.pink}Waiting for {Colors.white}{title}{Colors.pink} to start...{Colors.white}")
    wait_for_window(title)
    print(f"{Colors.pink}The {Colors.white}{title}{Colors.pink} has started!{Colors.white}")
    time.sleep(1)
    
except Exception as e:
    print(f"Error occurred: {str(e)}")
    exit()

# Match Setup

while True:
    match = match_custom(title)
    if match == True:
        time.sleep(2)
        break

# Match

while True:
    print(f"{Colors.pink}Waiting for match setup...{Colors.white}")
    time.sleep(2)
    if stp_img == "False":
        pass
    else: 
        print(f"{Colors.pink}Opening image of correct setup!{Colors.white}")
        os.system("start ./med/correct.png")
    setup = input(f"{Colors.pink}Press {Colors.white}ENTER{Colors.pink} to continue...{Colors.white}")
    print(f"{Colors.pink}Cheking for correct setup...{Colors.white}")
    print(f"{Colors.pink}Please switch over to your {Colors.white}brawlhalla{Colors.pink} tab!{Colors.white}")
    show_window(title)
    time.sleep(2)
    output = match_check()
    if output == True:
        hide_window(title)
        wait = input(f"{Colors.pink}Press {Colors.white}ENTER{Colors.pink} to continue...{Colors.white}")
        break

while True:
    output = add_bots()
    print(f"{Colors.pink}Done adding bots!{Colors.white}")
    if output == True:
        break

while True:
    output = choose_legend()
    if output == True:
        keyboard.press("c")
        break
    
# Farmer

matches = 0
runtime = 0

while True:
    image = locateOnScreen('./med/end.png', confidence=0.3)
    if image is not None:
        print(f"{Colors.pink}Match ended!{Colors.white}")
        time.sleep(2)
        matches += 1
        runtime += 15
        payload = {
        "content": "",
        "embeds": [
            {
            "title": "Brwler Stats!",
            "description": f"**{matches}** matches played! \n**{runtime}** runtime in minutes!",
            "color": 16777215,
            "author": {
                "name": "Brwler",
                "icon_url": "https://cdn.discordapp.com/attachments/1089053910838284339/1089053980040122408/Sin_titulo.jpg"
            }
            }
        ],
        "attachments": []
        }
        response = requests.post(webhook, data=payload, headers={"Content-Type": "application/json"})
    else:
        print(f"{Colors.pink}Match in progress...{Colors.white}")
        time.sleep(2)
        keyboard.press("j")
        time.sleep(random.randint(1, 2))
        keyboard.press("k")
        time.sleep(random.randint(1, 2))
        keyboard.press("a")
        time.sleep(random.randint(1, 4))
        keyboard.release("a")
        keyboard.press("s")
        time.sleep(random.randint(1, 2))
        keyboard.release("s")
        keyboard.press("l")
        time.sleep(random.randint(1, 2))
        keyboard.press("k")
        time.sleep(random.randint(1, 2))
        keyboard.press("d")
        time.sleep(random.randint(1, 4))
        keyboard.release("d")