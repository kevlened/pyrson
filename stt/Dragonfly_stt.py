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
from events import EventHook
import MessageType
import pythoncom
from dragonfly import (Grammar, AppContext, MappingRule, CompoundRule,
                    Dictation, Choice, Key, Text)

class Dragonfly_stt():
    def __init__(self):
        pass

    #rule that simply passes all input to the newtext event
    class Passthrough(CompoundRule):
        spec = "<text>"
        extras = [Dictation("text"), ]
        textrecognition = EventHook()

        def _process_recognition(self, node, extras):
            text = extras["text"]
            self.textrecognition.fire([MessageType.TEXT,text])

    def start(self, queue):
        #instantiating the grammar and rule
        grammar = Grammar("passthrough")
        rule = self.Passthrough()

        #attaching the event
        rule.textrecognition+=queue.put

        #adding and loading rule
        grammar.add_rule(rule)
        grammar.load()

        while 1:
            pythoncom.PumpWaitingMessages()
            time.sleep(.1)