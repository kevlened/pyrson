import pyttsx

class TTSX():
    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    def __init__(self):
        self.engine = pyttsx.init()
        self.engine.setProperty("rate", 150)