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
import time
import pythoncom
from dragonfly import (Grammar, AppContext, MappingRule, CompoundRule,
                        Dictation, Choice, Key, Text)
from events import EventHook

class dragonfly_stt():
    def __init__(self):
        self.onNewText = EventHook()

    #method to send new text to main Pyrson
    def fire(self, text):
        self.onNewText.fire(text)

    #rule that simply passes all input to the newtext event
    class Passthrough(CompoundRule):
        spec = "<text>"
        extras = [Dictation("text"), ]
        newtext = EventHook()

        def _process_recognition(self, node, extras):
            text = extras["text"]
            self.newtext.fire(text)

    def start(self):
        #instantiating the grammar and rule
        grammar = Grammar("passthrough")
        rule = self.Passthrough()

        #attaching the event
        rule.newtext+=self.fire

        #adding and loading rule
        grammar.add_rule(rule)
        grammar.load()

        while 1:
            pythoncom.PumpWaitingMessages()
            time.sleep(.1)