from multiprocessing import Process, Queue

from stt import dragonfly_stt
from tts import TTSX
from bots import RiveScriptBot

stt_library = dragonfly_stt()
tts_library = TTSX()
bot_library = RiveScriptBot()
#vision_library = PyOpenCV()

message_queue = Queue()

def main():
    bot_library.learn("./RiveScript")

    #test bot to avoid stt mixups
    #text = "Give me an alert"
    #new_text(text)

    stt_process = Process(name='stt',target=stt_library.start, args=(message_queue,))
    stt_process.start() #comment out to disable stt for testing

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