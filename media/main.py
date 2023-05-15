import os
import art
import time
import random
import ctypes
import subprocess
from pystyle import Colorate, Colors, Center

# Variables

user = Colors.white + os.getlogin() + Colors.pink
welcome_messages = [
    f"Hi {user}, welcome!",
    f"Welcome {user}! We're happy to have you.",
    f"Hey {user}, glad you could join us!",
    f"Greetings {user}! We hope you enjoy your time here.",
    f"Welcome aboard {user}!",
    f"Hello {user}! We're excited to have you here.",
    ]
separator = (f"\n{Colors.pink}======{Colors.white}======{Colors.pink}======{Colors.white}======{Colors.pink}======{Colors.white}======{Colors.pink}======{Colors.white}======{Colors.pink}======{Colors.white}======{Colors.pink}======\n{Colors.white}")

# Functions

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def title():
    clear()
    banner = (Colorate.Vertical(Colors.purple_to_red, art.text2art("Brwler", font="tarty1")))
    ctypes.windll.kernel32.SetConsoleTitleW("Brwler | By: Takkeshi | Version: 1.0.0")
    print(banner)
    print(f"{separator}\n")
    
def menu():
    menu = f"""
┌───────────────────┐
│   --- {Colors.pink}Menu{Colors.white} ---    │
├───────────────────┤
│ 1. {Colors.pink}Start Farmer{Colors.white}   │
│ 2. {Colors.pink}Exit{Colors.white}           │
└───────────────────┘
    """
    print(menu)

# MainLoop

title()
print(f"{Colors.pink}{random.choice(welcome_messages)}{Colors.white}")
menu()
option = input(f"{Colors.pink}Select an option: {Colors.white}")
option = int(option)

if option == 1:
    banner = (Colorate.Vertical(Colors.purple_to_red, art.text2art("Farmer", font="standard")))
    print(f"\n{separator}\n")
    print(banner)
    subprocess.call("python ./bin/farmer.py", shell=True)
if option == 2: 
    print(f"{Colors.pink}Thanks for using Brwler!{Colors.white}")
    time.sleep(2)
    exit()