import colorama
from colorama import Fore
import time
import os
from pynput.mouse import Listener as MouseListener
from pynput.mouse import Button
from pynput import keyboard
from pynput.mouse import Controller
import webbrowser

mouse = Controller()

colorama.init()
keyboard_controller = keyboard.Controller()
mouse = Controller()

new_script_content = """
{
  "FLogNetwork": "7",
  "DFIntTaskSchedulerTargetFps": "9999",
  "DFIntNewRunningBaseAltitudeD": "195",
  "DFIntRunningBaseOrientationP": "450",
  "FIntPGSAngularDampingPermillPersecond": "9999999999",
  "FFlagFixGraphicsQuality": "True",
  "FFlagHandleAltEnterFullscreenManually": "False",
  "DFFlagDebugPauseVoxelizer": "True",
  "FFlagDebugSkyGray": "True",
  "DFFlagDebugPerfMode": "True",
  "FFlagFastGPULightCulling3": "True",
  "FFlagPreloadAllFonts": "True",
  "DFIntS2PhysicsSenderRate": "250",
  "FFlagCommitToGraphicsQualityFix": "True",
  "DFIntClientLightingTechnologyChangedTelemetryHundredthsPercent": "0",
  "DFStringCrashUploadToBacktraceBaseUrl": "null",
  "DFStringCrashUploadToBacktraceMacPlayerToken": "null",
  "DFStringCrashUploadToBacktraceWindowsPlayerToken": "null",
  "GoogleAnalyticsAccountPropertyID": "null",
  "GoogleAnalyticsAccountPropertyIDPlayer": "null",
  "FStringCoreScriptBacktraceErrorUploadToken": "null",
  "FStringGamesUrlPath": "/games/",
  "DFFlagBaseNetworkMetrics": "False",
  "DFFlagBrowserTrackerIdTelemetryEnabled": "False",
  "DFStringRobloxAnalyticsURL": "null",
  "DFStringTelegrafHTTPTransportUrl": "null",
  "DFStringAltTelegrafHTTPTransportUrl": "null",
  "DFStringTelemetryV2Url": "null",
  "DFFlagEnableLightstepReporting2": "False",
  "DFIntLightstepHTTPTransportHundredthsPercent2": "0",
  "DFStringLightstepHTTPTransportUrlHost": "null",
  "DFStringLightstepHTTPTransportUrlPath": "null",
  "DFStringLightstepToken": "null",
  "FFlagDebugDisableTelemetryEphemeralCounter": "True",
  "FFlagDebugDisableTelemetryEphemeralStat": "True",
  "FFlagDebugDisableTelemetryEventIngest": "True",
  "FFlagDebugDisableTelemetryPoint": "True",
  "FFlagDebugDisableTelemetryV2Counter": "True",
  "FFlagDebugDisableTelemetryV2Event": "True",
  "FFlagDebugDisableTelemetryV2Stat": "True",
  "DFStringHttpPointsReporterUrl": "null",
  "DFStringAltHttpPointsReporterUrl": "null",
}
"""

title = Fore.RED+f"""
 ██ ▄█▀ ██▓ ██▀███   ▄▄▄       ▄████▄   ██▀███   ▒█████  
 ██▄█▒ ▓██▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▓██ ▒ ██▒▒██▒  ██▒
▓███▄░ ▒██▒▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓██ ░▄█ ▒▒██░  ██▒
▓██ █▄ ░██░▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒██   ██░
▒██▒ █▄░██░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░░██▓ ▒██▒░ ████▓▒░
▒ ▒▒ ▓▒░▓  ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ 
░ ░▒ ▒░ ▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒     ░▒ ░ ▒░  ░ ▒ ▒░ 
░ ░░ ░  ▒ ░  ░░   ░   ░   ▒   ░          ░░   ░ ░ ░ ░ ▒  
░  ░    ░     ░           ░  ░░ ░         ░         ░ ░  
                              ░                         
.gg/jnn {Fore.BLUE}MADE BY JNN! IF YOU SEE ME ON ROBLOX LET ME KNOW{Fore.RESET}"""

os.system("cls")
print(Fore.GREEN + "V4 IS OUT!\nIf you see me in roblox dont be scared to say hi" + Fore.RESET)
print(title)
kts = input("\n1. Type (boost) for macro booster (1 time use, edis method)\n2. Type (mouse) to use mouse keybinds\n3. Or type your keybind (keyboard only, for mouse type (mouse)\n\nENTER CHOICE: ").lower()


key_to_start = None

if kts == "mouse":
    middlemousebutton = input("What mouse button would you like to have as your keybind? (Middle, X1, or X2): ").lower()
    if middlemousebutton == "middle":
        key_to_start = Button.middle
    elif middlemousebutton == "x1":
        key_to_start = Button.x1
    elif middlemousebutton == "x2":
        key_to_start = Button.x2
else:
    key_to_start = keyboard.KeyCode.from_char(kts)

if kts == "boost":
    os.system("cls")
    print(title)
    folder_path = input(Fore.GREEN+"Enter your roblox path, to find your roblox path type PATH: ").lower()
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    filename_cas = os.path.join(folder_path, "ClientAppSettings.json")
    with open(filename_cas, "w") as new_script_file:
        new_script_file.write(new_script_content)
    print("Boosted macro! closing in 3 seconds...")
    time.sleep(3)
    quit()


macro_enabled = False


def on_press(key):
    global macro_enabled
    try:
        if key == key_to_start:
            macro_enabled = not macro_enabled
            print_status()
    except AttributeError:
        pass


def on_release(key):
    pass


def print_status():
    os.system("cls")
    print(f"Press {key_to_start} to toggle the macro.")
    print(title)
    print("------------------------------------------")
    if macro_enabled:
        print(Fore.GREEN + "KIRACO STARTED" + Fore.RESET)
    else:
        print(Fore.RED + "KIRACO STOPPED" + Fore.RESET)


def run_macro():
    if macro_enabled:
        keyboard_controller.press('i')
        time.sleep(0.01)
        keyboard_controller.release('i')

        keyboard_controller.press('o')
        time.sleep(0.01)
        keyboard_controller.release('o')


def on_click(x, y, button, pressed):
    global macro_enabled
    if button == key_to_start and pressed:
        macro_enabled = not macro_enabled
        print_status()


def main():
    print_status()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener, MouseListener(on_click=on_click) as mouse_listener:
        while True:
            run_macro()
            time.sleep(0.01)


if __name__ == "__main__":
    main()

input()