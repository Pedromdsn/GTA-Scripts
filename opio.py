import pyautogui
import time
import pydirectinput
from typing import Union
from pynput.keyboard import Key, KeyCode, Listener

paused = False
hasKey = False

def on_press(key: Union[Key, KeyCode, None]):
    global paused
    if isinstance(key, KeyCode) and key.char == "i":
        paused = not paused
        if paused:
            print("Paused...")
        else:
            print("Resuming...")
        return None
    return None

def runAllSlotsAndUseKey():
    for i in range(5):
        pydirectinput.press(str(i + 1))
        time.sleep(0.05)

def drag_image(image):
    items = list(pyautogui.locateAllOnScreen(image, confidence=0.97))
    print("Found ", len(items), " items")
    # if len(items) > 1:
    #     start_pos = pyautogui.center(items[0])
    #     end_pos = pyautogui.center(items[1])
    #     # print("", start_pos.x, start_pos.y)
    #     pydirectinput.moveTo(start_pos.x, start_pos.y, duration=0.5)
    #     pydirectinput.mouseDown()
    #     pydirectinput.moveTo(end_pos.x, end_pos.y, duration=0.5)
    #     # print("", end_pos.x, end_pos.y)
    #     pydirectinput.mouseUp()
    # elif len(items) == 1:
        # print("Only one item found")
    start_pos = pyautogui.center(items[0])
    pydirectinput.moveTo(start_pos.x, start_pos.y, duration=0.5)
    pydirectinput.mouseDown()
    pydirectinput.moveTo(1478, 366, duration=0.5)
    pydirectinput.mouseUp()


def main():
    global paused
    print("Starting in 3 seconds...")
    print("Press 'i' to pause")
    time.sleep(3)
    listener = Listener(on_press=on_press)
    listener.start()

    print("Starting...")
    while listener.running:
        if paused:
            time.sleep(0.5)
            continue
        
        pydirectinput.press("e")
        time.sleep(0.5)

        try:
            hasFullImage = pyautogui.locateOnScreen("img/full.png", confidence=0.75)
            isFull = hasFullImage is not None
            if isFull:
                print("Inventory full")
                if hasKey:
                    runAllSlotsAndUseKey()
                    time.sleep(0.3)
                pydirectinput.press("f2")
                time.sleep(0.4)
                drag_image("img/opio.png")
                pydirectinput.press("esc")
                time.sleep(0.3)
                if hasKey:
                    runAllSlotsAndUseKey()
        except pyautogui.ImageNotFoundException:
            print("Collecting... ")
            time.sleep(4.5)
            pass


if __name__ == "__main__":
    main()
