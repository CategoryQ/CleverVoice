# NO MORE UPDATES WILL COME
# Please head to https://notabug.org/Category for future updates
# Because of MS acquisition, obvs

# CleverVoice
Voice-only interface to RotaryPi

This was originally made on a linux box, using BASH & Python. Target for "real" installation is a RaspberryPi inside an old rotary phone. There are a few prerequisites, enumeraed below:-

+ BASH shell
+ Python (also install pip from your repos)
+ ffmpeg - should be available in your repos
+ festival - TtS engine, again should be in your repos
+ Cleverbot python midule - "pip install cleverbot" from a terminal to add this
+ Wikipedia python module - "pip install wikipedia"


After that , edit StT.sh to add your own Google Speech API Key, and change the spoken language setting (lines 63 & 66)

Then run "python CleverVoicePOC.py" for vocal Cleverbot chat
Or run "python WikiVoice.py" for vocal Wikipedia search
If it doesn't, make sure StT.sh is set to be excutable ("chmod +x StT.sh" in the terminal)
If it still doesn't work, tell me!

Script coming to slect betwen modes... At some point!

When you've had enough nonsense discussion with CleverVoice, just say "goodbye"


Peace, Category
