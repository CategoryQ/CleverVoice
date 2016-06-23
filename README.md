# CleverVoice
Voice-only interface to Cleverbot chat AI

This was made on a linux box, using BASH & Python. There are a few prerequisites, enumeraed below:-

+ BASH shell
+ Python (also install pip from your repos)
+ ffmpeg - should be available in your repos
+ festival - TtS engine, again should be in your repos
+ Cleverbot.py  - run "pip install cleverbot" from a terminal to add this


After that , edit StT.sh to add your own Google Speech API Key, and change the spoken language setting (lines 63 & 66)

Then run "python CleverVoicePOC.py", and it should automagically work.
If it doesn't, make sure StT.sh is set to be excutable ("chmod +x StT.sh" in the terminal)
If it still doesn't work, tell me!

Peace, Category
