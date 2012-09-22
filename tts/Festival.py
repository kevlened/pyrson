#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Owner
#
# Created:     23/08/2012
# Copyright:   (c) Owner 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import subprocess

class Festival():
    def say(self, text):
        #TODO: potential to change installed festival directory
        #process = 'echo ' + text + ' | ' + self.location + ' --libdir ' + self.library + ' --tts'
        process = 'echo ' + text + ' | ' + self.location + ' --tts'
        return_code = subprocess.call(process, shell=True)

    def __init__(self):
        self.location = r'C:\festival\src\main\festival.exe'
        self.library = r'C:\festival'