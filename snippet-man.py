#!/usr/bin/env python3

# Copied from https://askubuntu.com/a/544388

import os
import subprocess

home = os.environ["HOME"]
directory = home+"/.config/snippet_paste"
if not os.path.exists(directory):
    os.mkdir(directory)

# create file list with snippets
files = [
    directory+"/"+item for item in os.listdir(directory) \
         if not item.endswith("~") and not item.startswith(".")
    ]
files.sort()

# create string list
strings = []
for file in files:
    strings.append(file.rsplit("/")[-1])

# create list to display in option menu
list_items = strings+["manage snippets"]

# define (zenity) option menu
command = 'zenity --list '+'"'+('" "')\
      .join(list_items)+'"'\
      +f' --column="text fragments" --title="Paste snippets" --height={120+len(list_items)*27}'

# process user input
try:
    choice = subprocess.check_output(["/bin/bash", "-c", command]).decode("utf-8").strip()
    print(choice)
    if "manage snippets" in choice:
        subprocess.call(["xdg-open", directory])
    else:
        # i = int(choice[:choice.find(".")])
        # copy the content of corresponding snippet
        copy = f"xclip -in -selection c \"{directory}/{choice}\""
        print(copy)
        subprocess.call(["/bin/bash", "-c", copy])
        # paste into open frontmost file
        paste = "xdotool key Control_L+v"
        subprocess.Popen(["/bin/bash", "-c", paste])
except Exception as e:
    print(e)

