import os
from multiprocessing import Process, Queue
import MessageType

import userinput
from stt import Dragonfly_stt
from tts import TTSX
from bots import RiveScriptBot
from vision import FaceDetection

stt_library = Dragonfly_stt()
tts_library = TTSX()
bot_library = RiveScriptBot()
vision_library = FaceDetection()

message_queue = Queue()
processes = []

def main():
    botdn = os.path.join(os.path.dirname(__file__),'bots','RiveScript')
    bot_library.learn(botdn)

    stt_process = Process(name='stt',target=stt_library.start, args=(message_queue,))
    processes.append(stt_process)
    stt_process.start() #comment out to disable stt for testing

    vision_process = Process(name='vision',target=vision_library.start, args=(message_queue,))
    processes.append(vision_process)
    vision_process.start()

    userinput_process = Process(name='userinput', target=userinput.getchloop, args=(message_queue,))
    processes.append(userinput_process)
    userinput_process.start()

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

    response = bot_library.respond_to(text)

    print response
    tts_library.say(response)

def endprocesses():
    for p in self.processes:
        p.terminate()

if __name__ == '__main__':
    main()