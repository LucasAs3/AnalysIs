import pyautogui

def open_chrome():
    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    pyautogui.write("gmail")
    pyautogui.press('enter')