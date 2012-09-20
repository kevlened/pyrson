pyrson
======

A Digital Life Assistant (DLA) currently linking the following libraries:

* [dragonfly](http://code.google.com/p/dragonfly/) - for speech recognition
* [pyttsx](http://pypi.python.org/pypi/pyttsx) - for text-to-speech
* [RiveScript](http://www.rivescript.com/rivescript) or [pyAIML](http://pyaiml.sourceforge.net/) - for chat bots
* [AutoPy](http://www.autopy.org/) - for action support in RiveScripts
* [opencv](http://opencv.willowgarage.com/documentation/python/index.html) - face detection

pyrson may eventually include the following features:

* opencv - face recognition
* [AT&T Watson](http://www.research.att.com/projects/WATSON/index.html?fbid=sS3GdYGyIR4), [pocketsphinx](http://cmusphinx.sourceforge.net/), [Julius](http://pypi.python.org/pypi/pyjulius), or [Google SST](http://wiki.openmoko.org/wiki/Google_Voice_Recognition) - cross-platform speech recognition
* [voiceid](http://code.google.com/p/voiceid/) - voice identification (diarization) to maintain a user context
* [nltk](http://nltk.org/) - natural language processing (sentiment mining to change bot context)
* [smartThings](http://www.kickstarter.com/projects/smartthings/smartthings-make-your-world-smarter) - home automation

Currently, the project is only supported on Windows due to the dragonfly dependency for speech recognition. Ideally, the libraries will be easy to change in order to accomodate for different platforms/changing technologies/user preferences.