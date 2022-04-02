import keyboard

# Here you can define your own functions

muted = True

discordShortcut = "alt + c"
def muteDiscord():
    global muted
    if not muted:
        keyboard.press_and_release(discordShortcut)
        muted = not muted
    else:
        keyboard.press_and_release(discordShortcut)
        muted = not muted