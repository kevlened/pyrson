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

import pyttsx

class TTSX():
    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    def __init__(self):
        self.engine = pyttsx.init()
        self.engine.setProperty("rate", 150)