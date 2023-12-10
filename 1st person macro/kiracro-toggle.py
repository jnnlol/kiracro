import colorama
from colorama import Fore
import time
import pyfiglet
import os
import webbrowser
from pynput.mouse import Controller
from pynput import keyboard

mouse = Controller()

colorama.init()
keyboard_controller = keyboard.Controller()
mouse = Controller()

# kbc=kb.c()
# call kb_c for in-game movements

title = Fore.RED + """  _  _______ _____            _____ _____   ____  
 | |/ /_   _|  __ \     /\   / ____|  __ \ / __ \ 
 | ' /  | | | |__) |   /  \ | |    | |__) | |  | |
 |  <   | | |  _  /   / /\ \| |    |  _  /| |  | |
 | . \ _| |_| | \ \  / ____ \ |____| | \ \| |__| |
 |_|\_\_____|_|  \_\/_/    \_\_____|_|  \_\\____/ 
                                                  
                                                  """ + Fore.LIGHTMAGENTA_EX + "Coded by JNN and sponsered edi\n" + Fore.CYAN + "Need support \ OR / Want TO support? " + Fore.RED + "Join the discord!: https://discord.gg/dsaJRn9wnr" + Fore.RESET
os.system("cls")
key_to_toggle = input(Fore.YELLOW+"What would you like the key to toggle the macro to be?: ").lower()

toggle_enabled = False


def on_press(key):
    global toggle_enabled
    try:
        if key.char == key_to_toggle:
            toggle_enabled = not toggle_enabled
            print_status()
    except AttributeError:
        pass


def print_status():
    os.system("cls")
    print("Press " + key_to_toggle + " to toggle the macro.")
    print(title)
    print("------------------------------------------")
    if toggle_enabled:
        print(Fore.GREEN + "JNNMACRO STARTED" + Fore.RESET)
    else:
        print(Fore.RED + "JNNMACRO STOPPED" + Fore.RESET)


def run_macro():
    mouse.scroll(0, 1)
    time.sleep(0.01)

    mouse.scroll(0, -1)
    time.sleep(0.01)


def main():
    print(f"Press {key_to_toggle} to TOGGLE JNNMACRO.")
    print(title)

    with keyboard.Listener(on_press=on_press) as listener:
        while True:
            if toggle_enabled:
                run_macro()
            time.sleep(0.01)


if __name__ == "__main__":
    main()

input()
