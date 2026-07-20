import pyautogui # import pyautogui's library
import time
import pyscreeze


class Funcs_Aut:
    def image_click(image):
        x, y, largura, altura = pyautogui.locateOnScreen(image, confidence=0.8, grayscale=True)
        pyautogui.moveTo(x + largura / 2, y + altura / 2)
        pyautogui.click()

    def wait_time(image, sec):
        while not pyautogui.locateOnScreen(image):
            time.sleep(sec)

    def move_to(image):
        x, y, largura, altura = pyautogui.locateOnScreen(image, confidence=0.8, grayscale=True)
        pyautogui.moveTo(x + largura / 2, y + altura / 2)
