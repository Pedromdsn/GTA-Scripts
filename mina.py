from pynput.keyboard import Key, KeyCode, Listener
import pydirectinput
from typing import Union, Optional
import time

paused = False
count = 0

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
    global count
    print("Starting in 5 seconds...")
    print("Press 'i' to quit")
    time.sleep(5)
    listener = Listener(on_press=on_press)
    listener.start()

    print("Started")
    while listener.running and count < 100:
        if paused:
            time.sleep(0.5)
            continue
        pydirectinput.press('e')
        time.sleep(0.02)
        pydirectinput.press('e')
        count = count + 1
        print(f"Cancelling... {count}")
        if count % 2 == 1:
            time.sleep(2)
        if count % 2 == 0:
            time.sleep(5)


if __name__ == "__main__":
    main()
