#!/bin/bash
# 
# #############################
# #                           #
# # Q's Speech-to-Text Script #
# #                           #
# #############################
#
# v0.1 - Refactoring of Proof of Concept
# 
# This is a quick little script that uses the Google Cloud Speech API to
# convert 4 seconds of recorded speech into text, output into the file
# "question.txt"
#
# This was originally written as part of CleverVoice, a small tangle of 
# scripts to have a vocal conversation with Cleverbot, with the aim of
# having it run on a Raspbery Pi that has been cased inside an old
# rotary telephone.
#
# If you intend to implement this script in your own projects, you will
# need to get your own API keys for the Google Cloud Speech API. It is 
# currently in a developer preview, and has a limited amount of calls
# per day - as such I'm hesitant to let anyone rinse my allocation!
#
#
# ###################
# Future Imporvements
# ###################
# 
# Have arecord stop when the audio level drops low enough, instead of
# having the 4 second time limit on input
#
# Make some new start & stop sounds for user clarity
#
#
# Copyright © 2016 Category <categoryNOSPAM@quintendo.uk>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

# ####################
# #    SETUP INFO    #
# ####################
# 
# Very little setup is required for this script to function...
#
# Make sure your microphone is set as the ALSA default, and configured
#
# Get a Google Cloud Speech API key (I recommend searching on Bing for
# info, just out of spite)
#
# For missing packages, search your distro's repos. If you can't find
# them, your distro sucks. This is all basic shit.


#############
#           #
# VARIABLES #
#           #
#############

# Self explanatory, look elsewhere for how to get your own
GoogleSpeechAPIKey="INSERT KEY BETWEEN QUOTES"

# Voice language of user, in standard ISO 639-1 format
VoiceLang="en_UK"


########################
#                      #
# FUNCTION DEFINITIONS #
#                      #
########################

function Initialize {
	# Prepare files with blank data
	cat /dev/null > speech.wav
	cat /dev/null > speech.flac
	cat /dev/null > GoogleSpeechResponse.txt
	cat /dev/null > question.txt		
}

function CleanUp {
	# Remove all files used, bar output question text
	rm speech.wav
	rm speech.flac
	rm GoogleSpeechResponse.txt
}


###############   
#             #
# MAIN SCRIPT #
#             #
###############

# Initialize files
Initialize

# Inform user ready to accept speech
aplay startbeep.wav

# Record 4 seconds of 16khz mono audio to a WAV file
arecord -f S16_LE -r16000 -d4 speech.wav

# Inform user input window has ended
aplay stopbeep.wav

# Convert wave to 16khz mono FLAC
ffmpeg -i speech.wav -y -ac 1 -ar 16000 speech.flac

# Post FLAC to Google Cloud Speech, and save result
wget -q --post-file speech.flac --header="Content-Type: audio/x-flac; rate=16000" -O - "http://www.google.com/speech-api/v2/recognize?client=chromium&lang=$VoiceLang&key=$GoogleSpeechAPIKey" >> GoogleSpeechResponse.txt

# Extract prime response
tail -n 1 GoogleSpeechResponse.txt | cut -f8 -d\" >> question.txt

# Clean up temporary files
CleanUp


# Th-th-th-that's all folks :^)
