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
    mouse.scroll(0, 1)
    time.sleep(0.01)

    mouse.scroll(0, -1)
    time.sleep(0.01)


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
