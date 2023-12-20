import cv2
import numpy as np
import pyautogui
import time
import pydirectinput
from typing import Union, Optional
from pynput.keyboard import Key, KeyCode, Listener

paused = False

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, thresholded = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    processed_path = "temp/" + image_path
    cv2.imwrite(processed_path, thresholded)
    return processed_path


def on_press(key: Union[Key, KeyCode, None]):
    global paused
    if isinstance(key, KeyCode) and key.char == 'q':
        paused = not paused
        if paused:
            print("Paused...")
        else:
            print("Resuming...")
        return None
    return None

def drag_image(image):
    items = list(pyautogui.locateAllOnScreen(image, confidence=0.85))
    if len(items) >= 1:
    #     start_pos = pyautogui.center(items[0])
    #     end_pos = pyautogui.center(items[1])
    #     pydirectinput.moveTo(start_pos.x, start_pos.y)
    #     pydirectinput.mouseDown()
    #     pydirectinput.moveTo(end_pos.x, end_pos.y, duration=1)
    #     print("", end_pos.x, end_pos.y)
    #     pydirectinput.mouseUp()
    # elif len(items) == 1:
        # print("Only one item found")
        start_pos = pyautogui.center(items[0])
        pydirectinput.moveTo(start_pos.x, start_pos.y)
        pydirectinput.mouseDown()
        pydirectinput.moveTo(1571, 471, duration=1)
        pydirectinput.mouseUp()


def main():
    global paused
    print("Starting in 5 seconds...")
    print("Press 'q' to quit")
    time.sleep(5)
    listener = Listener(on_press=on_press)
    listener.start()

    processed_inventory_image = preprocess_image("img/full.png")

    print("Started")
    while listener.running:
        if paused:
            time.sleep(0.5)
            continue
        print("Collecting...: ", end="")
        pydirectinput.press("e")
        time.sleep(0.5)
        try:
            if (
                pyautogui.locateOnScreen(processed_inventory_image, confidence=0.75)
                is not None
            ):
                print("Inventory full")
                for i in range(5):
                    pydirectinput.press(str(i + 1))
                    time.sleep(0.1)
                time.sleep(0.3)
                pydirectinput.press("f2")
                time.sleep(0.2)
                drag_image("img/opio.png")
                pydirectinput.press("esc")
                time.sleep(0.3)
                for i in range(5):
                    pydirectinput.press(str(i + 1))
                    time.sleep(0.1)
                time.sleep(0.2)
        except pyautogui.ImageNotFoundException:
            print("Inventory not full")
            time.sleep(4.5)
            pass
        

if __name__ == "__main__":
    main()
