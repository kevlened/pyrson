import os
from multiprocessing import Process, Queue

from stt import Dragonfly_stt
from tts import TTSX
from bots import RiveScriptBot
from vision import FaceDetection

stt_library = Dragonfly_stt()
tts_library = TTSX()
bot_library = RiveScriptBot()
vision_library = FaceDetection()

message_queue = Queue()

def main():
    botdn = os.path.join(os.path.dirname(__file__),'bots','RiveScript')
    bot_library.learn(botdn)

    #test bot to avoid stt mixups
    #text = "Give me an alert"
    #new_text(text)

    stt_process = Process(name='stt',target=stt_library.start, args=(message_queue,))
    stt_process.start() #comment out to disable stt for testing

    vision_process = Process(name='vision',target=vision_library.start, args=(message_queue,))
    vision_process.start()

    while True:
        message = message_queue.get() #blocking for the message queue
        new_text(message)

def new_text(text):
    text = str(text)
    print text

    response = bot_library.respond_to(text)

    print response
    tts_library.say(response)

if __name__ == '__main__':
    main()