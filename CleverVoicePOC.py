#!/bin/python
# 
# #####################
# #                   #
# # Q's "CleverVoice" #
# #                   #
# #####################
#
# v0.1 - Refacotring of Proof of Concept
#
# Just a little bit of Python plumbing. It uses my other script StT to 
# get text from some audio speech, pass it to cleverbot, and send the 
# response to festival TtS system.
#
# The end result is an internet chatbot that you can converse with,
# in natural vocal language. Aside from starting the program, everything
# else requires no input from the user, except speaking aloud.
#
# Originally coded for a Raspeberry Pi that had been cased in an old
# rotary phone, so there is always someone to talk to...
#
#
# Copyright © 2016 Category <categoryNOSPAM@quintendo.uk>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.


# Load Libraries
import subprocess
from cleverbot import Cleverbot

# Initialize Cleverbot
ChatBot = Cleverbot()


# Loop for 10 questions/responses - upgrade to continuous while loop, magic word to exit?
for x in range(0, 10):
	# Get voice input - GOOGLE MAGIC
	subprocess.call("./StT.sh")
	
	# Import Google Speech question
	question = open("question.txt").read()
	print "Q: %s" % question
	
	# Send to Cleverbot, and get response
	response = ChatBot.ask(question)
	print "A: %s" % response
	
	# Save response to text file
	with open("response.txt", "w") as text_file:
		text_file.write("%s" % response)
	
	# Speak response aloud
	subprocess.call(["festival", "--tts", "response.txt"])



