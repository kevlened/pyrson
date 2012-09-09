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
#from action import dragonfly_action

stt_library = dragonfly_stt()
tts_library = TTSX()
bot_library = RiveScriptBot()
#action_library = dragonfly_action()
#vision_library = PyOpenCV()

def main():
    stt_library.onNewText += new_text
    bot_library.learn("./RiveScript")

    #action_library.load("actions.txt")

    text = "Hello Bot"
    new_text(text)

    stt_library.start()

def new_text(text):
    text = str(text)
    print text

    #acted_on, response = action_library.act_on(text)

    response = bot_library.respond_to(text)

    print response
    tts_library.say(response)

if __name__ == '__main__':
    main()