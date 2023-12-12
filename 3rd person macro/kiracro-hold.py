import colorama
from colorama import Fore
import time
import pyfiglet
import os
from pynput import keyboard

colorama.init()
keyboard_controller = keyboard.Controller()

title = Fore.RED + """  _  _______ _____            _____ _____   ____  
 | |/ /_   _|  __ \     /\   / ____|  __ \ / __ \ 
 | ' /  | | | |__) |   /  \ | |    | |__) | |  | |
 |  <   | | |  _  /   / /\ \| |    |  _  /| |  | |
 | . \ _| |_| | \ \  / ____ \ |____| | \ \| |__| |
 |_|\_\_____|_|  \_\/_/    \_\_____|_|  \_\\____/ 
                                                  
""" + Fore.LIGHTMAGENTA_EX + "Coded by JNN and sponsered edi\n" + Fore.CYAN + "Need support \ OR / Want TO support? " + Fore.RED + "Join the discord!: https://discord.gg/dsaJRn9wnr" + Fore.RESET
os.system("cls")
print(Fore.GREEN+"EXE VERSION!!"+Fore.RESET)
key_to_hold = input(Fore.YELLOW + "What would you like the key to hold to enable the macro?: ").lower()

holding_key = False

def on_press(key):
    global holding_key
    try:
        if key.char == key_to_hold:
            holding_key = True
            print_status()
    except AttributeError:
        pass

def on_release(key):
    global holding_key
    try:
        if key.char == key_to_hold:
            holding_key = False
            print_status()
    except AttributeError:
        pass

def print_status():
    os.system("cls")
    print(f"Hold {key_to_hold} to enable the macro.")
    print(title)
    print("------------------------------------------")
    if holding_key:
        print(Fore.GREEN + "KIRACO STARTED" + Fore.RESET)
    else:
        print(Fore.RED + "KIRACO STOPPED" + Fore.RESET)

def run_macro():
    keyboard_controller.press('i')
    time.sleep(0.01)
    keyboard_controller.release('i')

    keyboard_controller.press('o')
    time.sleep(0.01)
    keyboard_controller.release('o')

def main():
    print_status()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        while True:
            if holding_key:
                run_macro()
            time.sleep(0.01)

if __name__ == "__main__":
    main()

input()
