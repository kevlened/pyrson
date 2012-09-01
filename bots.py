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

import aiml

class PyAIML():
    def respond_to(self, text):
        response = self.k.respond(text)
        return response

    def learn(self, filefoldername):
        self.k.learn(filefoldername)

    def __init__(self):
        self.k = aiml.Kernel()