import os, sys
from multiprocessing import Process, Queue
import MessageType

import userinput
import stt
import tts
import bots
import vision

try:
    global stt_library
    stt_library = stt.Dragonfly_stt() 
    print "Successfully loaded speech to text"
except:
    print "Couldn't load speech to text"

try:
    global tts_library 
    tts_library = tts.TTSX()
    print "Successfully loaded text to speech"
except:
    print "Couldn't load text to speech"

try:    
    global bot_library 
    bot_library = bots.RiveScriptBot()
    print "Successfully loaded bot"
except:
    print "Couldn't load bot"

try:
    global vision_library 
    vision_library = vision.FaceDetection()
    print "Successfully loaded vision"
except:
    print "Couldn't load vision"  

message_queue = Queue()
processes = []

def main():
    # Load and teach the bot
    if exists('bot_library'):
        botdn = os.path.join(os.path.dirname(__file__),'bots','RiveScriptFiles')
        bot_library.learn(botdn)

    # Load speech recognition
    if exists('stt_library'):
        stt_process = Process(name='stt',target=stt_library.start, args=(message_queue,))
        processes.append(stt_process)
        stt_process.start()

    # Load vision processing
    if exists('vision_library'):
        vision_process = Process(name='vision',target=vision_library.start, args=(message_queue,))
        processes.append(vision_process)
        vision_process.start()

    #Try to load direct user input
    try:
        userinput_process = Process(name='userinput', target=userinput.easygui_input, args=(message_queue,))
        processes.append(userinput_process)
        userinput_process.start()
    except Exception, e:
        print "Couldn't load user input"

    if len(processes) == 0:
        print "No input libraries are loaded. Closing."
        return

    print "Starting to poll for messages..."

    dead = False
    while not dead:
        message = message_queue.get() #waits for a message from any source

        #types determine where the message is coming from
        incomingtype = message[0]
        messagevalue = message[1]

        if incomingtype == MessageType.TEXT:
            new_text(messagevalue)
        elif incomingtype == MessageType.VISION:
            #TODO: a way to make RiveScript know this is vision
            new_text(messagevalue)
        elif incomingtype == MessageType.USERESCAPE:
            if messagevalue in ['q','e']:
                print "Wrapping up"
                endprocesses()
                print "Done"
                dead = True
            elif messagevalue in ['w','i','t']:
                text = raw_input("Enter text: ")
                new_text(text)

def new_text(text):
    text = str(text)
    print text

    if exists('bot_library'):
        response = bot_library.respond_to(text)
        print response
        if exists('tts_library'):
            tts_library.say(response)
        else:
            print "It appears the bot has lost it's voice"
    else:
        print "There is no bot to provide a response"

def endprocesses():
    for p in processes:
        p.terminate()

def exists(x):
    if x in globals():
        return True
    else:
        return False

if __name__ == '__main__':
    main()