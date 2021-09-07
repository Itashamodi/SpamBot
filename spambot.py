import pyautogui
import webbrowser
import time
webbrowser.open("https://whatsapp.com")
time.sleep(60)
for i in range(20):
    pyautogui.press("I")
    pyautogui.press("T")
    pyautogui.press("A")
    pyautogui.press("S")
    pyautogui.press("H")
    pyautogui.press("A")
    pyautogui.press("enter")
