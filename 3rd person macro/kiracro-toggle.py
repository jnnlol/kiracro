import colorama
from colorama import Fore
import time
import pyfiglet
import os
from pynput.mouse import Controller
from pynput import keyboard



mouse = Controller()

colorama.init()
keyboard_controller = keyboard.Controller()
mouse = Controller()

title = Fore.RED + pyfiglet.figlet_format("kiracro") + Fore.LIGHTMAGENTA_EX + "Coded by JNN and made by edi\n" + Fore.CYAN + "Need support \ OR / Want TO support? " + Fore.RED + "Join the discord!: https://discord.gg/dsaJRn9wnr" + Fore.RESET


keytostart = input("What would you like the key to start the macro to be?: ").lower()


start_stop_key = keytostart
spam_enabled = False

def on_press(key):
    global spam_enabled
    try:
        if key.char == start_stop_key:
            toggle_spam()
            print_status()
    except AttributeError:
        pass

def toggle_spam():
    global spam_enabled
    spam_enabled = not spam_enabled

def print_status():
    if spam_enabled:
        os.system("cls")
        print("Press "+start_stop_key+" To enable macro.")
        print(title)
        print("------------------------------------------")
        print(Fore.GREEN + "KIRACO STARTED" + Fore.RESET)
    else:
        os.system("cls")
        print("Press "+start_stop_key+" To enable macro.")
        print(title)
        print(Fore.RED + "KIRACO STOPPED" + Fore.RESET)

def run_macro():
    keyboard_controller.press('i')
    time.sleep(0.01)
    keyboard_controller.release('i')

    keyboard_controller.press('o')
    time.sleep(0.01)
    keyboard_controller.release('o')

def main():
    print(f"Press {start_stop_key} to START/STOP KIRACRO.")
    print(title)

    with keyboard.Listener(on_press=on_press) as listener:
        while True:
            if spam_enabled:
                run_macro()
            time.sleep(0.01)

if __name__ == "__main__":
    main()


input()