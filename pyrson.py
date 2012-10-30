import os, sys
from multiprocessing import Process, Queue
import MessageType

import userinput
import stt
import tts
import bots
import vision

try:
    stt_library = stt.Dragonfly_stt()    
    print "Successfully loaded speech to text"
except:
    print "Couldn't load speech to text"

try:
    tts_library = tts.TTSX()
    print "Successfully loaded text to speech"
except:
    print "Couldn't load text to speech"

try:    
    bot_library = bots.RiveScriptBot()
    print "Successfully loaded bot"
except:
    print "Couldn't load bot"

try:
    vision_library = vision.FaceDetection()
    print "Successfully loaded vision library"
except:
    print "Couldn't load vision library"  

message_queue = Queue()
processes = []

def main():
    # Load and teach the bot
    if 'bot_library' in locals():
        botdn = os.path.join(os.path.dirname(__file__),'bots','RiveScript')
        bot_library.learn(botdn)

    # Load speech recognition
    if 'stt_library' in locals():
        stt_process = Process(name='stt',target=stt_library.start, args=(message_queue,))
        processes.append(stt_process)
        stt_process.start()

    # Load vision processing
    if 'vision_library' in locals():
        vision_process = Process(name='vision',target=vision_library.start, args=(message_queue,))
        processes.append(vision_process)
        vision_process.start()

    # Try to load direct user input
    try:
        textinput = userinput.getchloop()
        userinput_process = Process(name='userinput', target=textinput, args=(message_queue,))
        processes.append(userinput_process)
        userinput_process.start()
    except Exception, e:
        print "Couldn't load text input"

    if len(processes) == 0:
        print "No libraries are loaded. Closing."
        return

    print "Starting to poll for messages..."
    while True:
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
                endprocesses()
                exit
            elif messagevalue in ['w','i','t']:
                text = raw_input("Enter text: ")
                new_text(text)

def new_text(text):
    text = str(text)
    print text

    if 'bot_library' in locals():
        response = bot_library.respond_to(text)
        print response
        if 'tts_library' in locals():
            tts_library.say(response)
    else:
        print "There is no bot to provide a response"

def endprocesses():
    for p in self.processes:
        p.terminate()

if __name__ == '__main__':
    main()