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

from events import EventHook
from stt import dragonfly_stt
from tts import TTSX
from bots import RiveScriptBot

stt_library = dragonfly_stt()
tts_library = TTSX()
bot_library = RiveScriptBot()
#vision_library = PyOpenCV()

def main():
    stt_library.onNewText += new_text
    bot_library.learn("./RiveScript")

    #test bot to avoid stt mixups
    #text = "Give me an alert"
    #new_text(text)

    #comment out to disable stt for testing
    stt_library.start()

def new_text(text):
    text = str(text)
    print text

    response = bot_library.respond_to(text)

    print response
    tts_library.say(response)

if __name__ == '__main__':
    main()