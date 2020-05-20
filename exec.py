#!/usr/bin/env python3

import os
import sys
import platform
import itertools

extensions = ['mp3', 'pcm', 'wav', 'aiff', 'aac', 'wma', 'flac', 'alac']

counter = itertools.count(1)

files = [f for f in os.listdir('.')
        if os.path.isfile(f)
        and os.path.splitext(f)[1][1:] in extensions]

if len(files) == 0:
    print("No file found. Exiting...")
    sys.exit()

menu = '\n'.join(['{a}. {b}'.format(a=next(counter), b=f) for f in files])

prompt = """
Found files:
------------

{}

------------
Please enter the desired ID : """.format(menu)

while 1:
    choice = int(input(prompt)) - 1

    while choice not in range(len(files)):
        print("\nInvalid ID")
        choice = int(input(prompt)) - 1

    path = files[choice]

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
            " ":  r"\ ",
            "|":  r"\|"
        }))

    if platform.system() == 'Windows':
        path = path.translate(str.maketrans({"/": "\\"}))
        cmd = "vlc -q --start-time=00 "
    else:
        cmd = "/Applications/VLC.app/Contents/MacOS/VLC -q --start-time=00 "

    os.system(cmd + path)
