import serial
import time
from functions import *
from buttonFunction import *

# Change the port based on your arduino configuration
port = "COM3"
baudRate = "9600"

# Set ser as serial port COM3 at 9600 baud rate
ser = serial.Serial(port, baudRate)

# Button definitions
valorant = ButtonFunction("openValorant", True, '"D:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=valorant --launch-patchline=live', None)
lol = ButtonFunction("openLol", True, '"D:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live', None)
chrome = ButtonFunction("openChrome", True, "start chrome", None)
discordMute = ButtonFunction("mute", False, None, muteDiscord)
discordUnMute = ButtonFunction("unmute", False, None, muteDiscord)

# Here we add the buttons created earlier to the list
buttonList.append(valorant)
buttonList.append(lol)
buttonList.append(chrome)
buttonList.append(discordMute)
buttonList.append(discordUnMute)

# An endless loop that searchs for incoming commands
while (True):
    if (ser.inWaiting() > 0):   # Checks if incoming bytes are waiting to be read from the serial input buffer
        data_str = ser.read(ser.inWaiting()).decode('ascii') # Reads the bytes and converts them from binary array to ASCII
        data_str = data_str.rstrip("\r\n") # Strips the useless chars at the end of the incoming command
        print(data_str)
        for button in buttonList: # Iterates in the buttonList
           button.controlCommand(data_str) # Checks if the current button's commandName is the same as the one read from the serial bus
    
    # Optional, but recommended: sleep 10 ms (0.01 sec) once per loop to let 
    # other threads on your PC run during this time. 
    time.sleep(0.01) 