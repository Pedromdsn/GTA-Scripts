from pynput.keyboard import Key, KeyCode, Listener
import pydirectinput
from typing import Union, Optional
import time

paused = False

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

def main():
    global paused
    print("Starting in 5 seconds...")
    print("Press 'q' to quit")
    time.sleep(5)
    listener = Listener(on_press=on_press)
    listener.start()

    print("Started")
    while listener.running:
        if paused:
            time.sleep(0.5)
            continue
        pydirectinput.press('w')
        pydirectinput.press('e')
        time.sleep(20)