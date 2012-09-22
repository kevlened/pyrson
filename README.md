pyrson
======

A Digital Life Assistant (DLA) currently linking the following libraries:

* [dragonfly](http://code.google.com/p/dragonfly/) - for speech recognition
* [pyttsx](http://pypi.python.org/pypi/pyttsx) or [Festival](http://www.cstr.ed.ac.uk/projects/festival/) - for text-to-speech
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

Installation
------------

Download and install the following dependencies:

###Windows 7 32-bit: works 64-bit: works (see notes)
* [32-bit Python 2.7](http://www.python.org/ftp/python/2.7.3/python-2.7.3.msi)
* [32-bit pywin32 Build 217](http://sourceforge.net/projects/pywin32/files/pywin32/Build%20217/pywin32-217.win32-py2.7.exe/download)
* [dragonfly 0.6.5](http://dragonfly.googlecode.com/files/dragonfly-0.6.5.win32.exe)
* [pyttsx 1.0](http://pypi.python.org/packages/any/p/pyttsx/pyttsx-1.0.win32.exe#md5=1bdf526eec286b683d61d97eb2922d4a)
* (optional)[Festival 2.1](http://downloads.sourceforge.net/e-guidedog/festival-2.1-win.7z) - extract to `C:\festival`
* (optional)[PyAIML 0.8.6](http://sourceforge.net/projects/pyaiml/files/PyAIML%20%28unstable%29/0.8.6/PyAIML-0.8.6.win32.exe/download)
* [python-rivescript 1.00](http://www.rivescript.com/files/win32/python-rivescript-1.00.win32.exe)
* [32-bit autopy 0.51](http://pypi.python.org/packages/2.7/a/autopy/autopy-0.51.win32-py2.7.exe#md5=93e91799367e9207383747a633408185)
* [numpy 1.6.2](http://sourceforge.net/projects/numpy/files/NumPy/1.6.2/numpy-1.6.2-win32-superpack-python2.7.exe/download)
* [opencv 2.4.2 for Windows](http://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.2/OpenCV-2.4.2.exe/download) - unpack to C:\opencv
* [32-bit opencv 2.4.2 python bindings (opencv-python-2.4.2.win32-py2.7.exe)](http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv)
* working microphone and webcam
* download [zip](https://github.com/kevlened/pyrson/zipball/master) and extract to desired folder

####notes:
* The libraries must be run with administrator rights unless UAC is disabled.
* Pywin32 on 64-bit may encounter pywin32 errors on installation that can be [fixed](http://sourceforge.net/tracker/?func=detail&aid=3402824&group_id=78018&atid=551954).
* Tests were run using an Intel Core-i5 2500 @3.30 GHz with great performance

Run
------

Double-click pyrson.py

or

(if UAC is enabled)
* Set `C:\python27` in your PATH environment variable
* Open cmd as administrator
* Run `python your\pyrson\directory\pyrson.py`

Modify
---------

###RiveScript

By default pyrson uses RiveScript as its speech comprehension engine. Documentation for writing your own RiveScript files can be found [here](http://www.rivescript.com/docs/Tutorial.html). Any RiveScript files in the `your\pyrson\directory\bots\RiveScript` folder are loaded by pyrson.

In addition to the standard RiveScript responses, pyrson also includes functions to type text, move the mouse, or click within RiveScript. Here are examples:

	//shows an alert
	+ give me an alert
	- <call>alert do what?</call>

	//moves the mouse to 100,150
	+ move the mouse
	- <call>mouse 100 150</call>

	//types Look at me! I'm typing.
	+ can you type for me?
	- <call>typekeys Look at me! I'm typing.<call>
	
###PyAIML (if installed)

Pyrson can also use AIML instead of RiveScript. It will load all the AIML files in `your\pyrson\directory\bots\AIML`. Just change the following lines in pyrson.py:

* `from bots import RiveScriptBot` to `from bots import PyAIML`
* `bot_library = RiveScriptBot()` to `bot_library = PyAIML()`
* `botdn = os.path.join(os.path.dirname(__file__),'bots','RiveScript')` to `botdn = os.path.join(os.path.dirname(__file__),'bots','AIML')`