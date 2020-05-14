#!/usr/bin/env python3

import os
import platform
import itertools

extensions = ['mp3', 'pcm', 'wav', 'aiff', 'aac', 'wma', 'flac', 'alac']

counter = itertools.count(1)

files = [f for f in os.listdir('.')
        if os.path.isfile(f)
        and os.path.splitext(f)[1][1:] in extensions]

menu = '\n'.join(['{a}. {b}'.format(a=next(counter), b=f) for f in files])

prompt = """
Found files:
------------

{}

------------
Please enter the desired ID : """.format(menu)

choice = int(input(prompt)) - 1

while choice not in range(len(files)):
    print("\nInvalid ID")
    choice = int(input(prompt)) - 1

path = files[choice - 1]

path = path.translate(str.maketrans(
    {
        "-":  r"\-",
        "]":  r"\]",
        "\\": r"\\",
        "^":  r"\^",
        "$":  r"\$",
        "*":  r"\*",
        ".":  r"\.",
        "(":  r"\(",
        ")":  r"\)",
        " ":  r"\ "
    }))

if platform.system() == 'Windows':
    cmd = "vlc -q --start-time=00 "
else:
    cmd = "/Applications/VLC.app/Contents/MacOS/VLC -q --start-time=00 "

os.system(cmd + path)
