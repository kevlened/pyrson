pyrson
======

A Digital Life Assistant (DLA) currently linking the following libraries:

* [dragonfly](http://code.google.com/p/dragonfly/) - for speech recognition
* [pyttsx](http://pypi.python.org/pypi/pyttsx) - for text-to-speech
* [pyAIML](http://pyaiml.sourceforge.net/) - for chat bots

pyrson may eventually include the following features:
* actions integrated using some of the libraries from dragonfly
* [opencv](http://opencv.willowgarage.com/documentation/python/index.html) - face recognition
* [nltk](http://nltk.org/) - natural language processing (sentiment mining to change bot context)
* [voiceid](http://code.google.com/p/voiceid/) - voice identification (diarization) to maintain a user context
* [smartThings](http://www.kickstarter.com/projects/smartthings/smartthings-make-your-world-smarter) - home automation

Currently, the project is only supported on Windows due to the dragonfly dependency for speech recognition and actions.
Ideally, the libraries will be easy to change in order to accomodate for different platforms/changing technologies/user preferences.