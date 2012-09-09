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
from rivescript import RiveScript

failed_response = "I don't know what to say"

class PyAIML():
    def respond_to(self, text):
        response = self.k.respond(text)
        return response

    def learn(self, filefoldername):
        self.k.learn(filefoldername)

    def __init__(self):
        self.k = aiml.Kernel()

class RiveScriptBot():
    def respond_to(self, text, user="localuser"):
        response = self.k.reply(user,text)
        rivescript_failed_responses = set(["ERR: No Reply Found" , "ERR: No Reply Matched"])
        if response in rivescript_failed_responses:
            response = failed_response
        return response

    def learn(self, filefoldername):
        #need to see if it is a file or folder - for now we'll assume it's the
        #brain folder
        self.k.load_directory(filefoldername)
        self.k.sort_replies()

    def __init__(self):
        self.k = RiveScript()