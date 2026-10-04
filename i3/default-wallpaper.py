import random
from pathlib import Path
import subprocess

dir_path = Path("~/Pictures/Wallpapers").expanduser()
wallpapers = [item.name for item in dir_path.iterdir() if item.is_file()]
wallpaper = random.choice(wallpapers)
print(wallpaper)
subprocess.run(['feh', '--bg-fill', f'{dir_path}/{wallpaper}'])