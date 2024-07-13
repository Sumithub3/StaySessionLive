import time
import importlib.util
import subprocess
import sys

def check_module_installed(module_name):
    spec = importlib.util.find_spec(module_name)
    return spec is not None

if not check_module_installed('pyautogui'):
    print("pyautogui is not installed. Installing...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])
    print("pyautogui has been installed.")
else:
    print("pyautogui is already installed.")


import pyautogui


def move_mouse_in_square():
    time.sleep(10)
    pyautogui.moveRel(100, 0, duration=0.25)  # Move right
    pyautogui.click()  # Click after moving
    pyautogui.moveRel(0, 100, duration=0.25)  # Move down
    pyautogui.click()  # Click after moving
    pyautogui.moveRel(-100, 0, duration=0.25)  # Move left
    pyautogui.click()  # Click after moving
    pyautogui.moveRel(0, -100, duration=0.25)  # Move up
    pyautogui.click()  # Click after moving

    time.sleep(10)
    move_mouse_in_square()

move_mouse_in_square()
