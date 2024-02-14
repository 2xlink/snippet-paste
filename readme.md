# Snippet-Paste

Easily manage text snippets and paste them using a minimalistic GUI.

```bash
➜  ~ ls $HOME/.config/snippet_paste/
contact-data  my-user-id  rickroll-lyrics
➜  ~ cat $HOME/.config/snippet_paste/rickroll-lyrics 
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you 

```

https://github.com/2xlink/snippet-paste/assets/8763936/3ff33213-13a9-49cf-add8-68cadb752351

## Requirements

- python3
- zenity
- xdotool
- xclip
- xdg-open
- bash

## Installing

Move the script to your preferred location and either

- give it execute rights (`chmod +x $file`) or
- call it using python (`python3 $file`)

## Usage

Calling the script the first time will create a directory at `$HOME/.config/snippet_paste`. There, create files with your desired (text) content. They will then be listed when the script is called.