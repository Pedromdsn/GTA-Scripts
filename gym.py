from pynput.keyboard import Key, KeyCode, Listener
import pydirectinput
from typing import Union, Optional
import time

paused = False

def on_press(key: Union[Key, KeyCode, None]):
    global paused
    if isinstance(key, KeyCode) and key.char == 'i':
        paused = not paused
        if paused:
            print("Paused...")
        else:
            print("Resuming...")
        return None
    return None

def main():
    global paused
    print("Starting in 3 seconds...")
    print("Press 'i' to quit")
    time.sleep(3)
    listener = Listener(on_press=on_press)
    listener.start()

    print("Started")
    while listener.running:
        if paused:
            time.sleep(0.5)
            continue
        print("Training...")
        pydirectinput.press('e')
        time.sleep(25)


if __name__ == "__main__":
    main()
