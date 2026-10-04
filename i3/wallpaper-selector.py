#!/usr/bin/env python3
from pathlib import Path
import subprocess
from pynput import keyboard

dir_path = Path("~/Pictures/Wallpapers").expanduser()
wallpapers = [item.name for item in dir_path.iterdir() if item.is_file()]
current = 0

def on_press(key):
    global current
    try:
        char = key.char
    except AttributeError:
        return  # ignore special keys (ctrl, shift, etc.)

    if char == 'n':
        current = (current + 1) % len(wallpapers)
        subprocess.run(['kitty', 'icat', str(dir_path / wallpapers[current])])
        print("Press 'n' next, 'p' prev, 'a' apply, 'q' quit")
    elif char == 'p':
        current = (current - 1) % len(wallpapers)
        subprocess.run(['kitty', 'icat', str(dir_path / wallpapers[current])])
        print("Press 'n' next, 'p' prev, 'a' apply, 'q' quit")
    elif char == 'a':
        subprocess.run(['feh', '--bg-fill', str(dir_path / wallpapers[current])])
        print("Wallpaper Changed")
        print("Press 'n' next, 'p' prev, 'a' apply, 'q' quit")
    elif char == 'q':
        return False  # stops the listener

# Show first wallpaper initially
subprocess.run(['kitty', 'icat', str(dir_path / wallpapers[current])])
print("Press 'n' next, 'p' prev, 'a' apply, 'q' quit")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()   