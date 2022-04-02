import os

# List that contains buttons created
buttonList = []

# Button class definition
class ButtonFunction:
    # Each button is defined as follows
    def __init__(self, commandName, cmdEnabled, cmd, callback):
        self.commandName = commandName # A commandName, which is the command passed through serial, i.e. "openChrome" or "muteDiscord"
        self.cmdEnabled = cmdEnabled # cmdEnabled indicates if the button defined uses the "command prompt"
        self.cmd = cmd # If cmdEnabled is set to True then put here the string to execute in the cmd. Set this to "None" if you want to execute only the callback funtion
        self.callback = callback # If cmdEnabled is set to False then put here the function you want to callback. Set this to "None" if you want to execute only in the cmd

    # Checks if the button's cmdEnabled is set to True or False
    def isCmdEnabled(self):
        if not self.cmdEnabled:
            return False
        else:
            return True

    # Executes the command assigned to the button in the cmd
    def exeCmd(self):
        os.system(self.cmd)

    # Execute the assigned callback function
    def exeCallback(self):
        self.callback()

    # Based on the button configuration decides to execute the command in the cmd or to callback the function defined
    def controlCommand(self, inputCommand):
        if(self.commandName == inputCommand):
            if self.isCmdEnabled():
                self.exeCmd()
            else:
                self.callback()