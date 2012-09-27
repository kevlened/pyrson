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

import pyaiml

failed_response = "I don't know what to say"

class PyAIMLBot():
    def respond_to(self, text):
        response = self.k.respond(text)
        return response

    def learn(self, filefoldername):
        self.k.learn(filefoldername)

    def __init__(self):
        self.k = pyaiml.Kernel()