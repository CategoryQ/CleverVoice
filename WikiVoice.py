#!/bin/python
# coding=utf-8
#
# ##################################
# #                                #
# # Q's Wikipedia Abstract Scraper #
# #                                #
# ##################################
#
# vPOC - Proof of Concept
# 
# This is a quick script to search Wikipedia, and scrape out the
# abstract of an article. Eventually for use in my CleverVoice system
#
# This is the Python component of a larger piece of work...
#
# Relies on "wikipedia" python module - "pip install wikipedia"
#
# Part of the "Clever Voice" suite
#
# Copyright © 2016 Category <categoryNOSPAM@quintendo.uk>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import wikipedia
import subprocess

# Get voice input - GOOGLE MAGIC
subprocess.call("./StT.sh")
	
# Import Google Speech question
WikiSearch = open("question.txt").read()
print "Searching Wikipedia for %s" % WikiSearch

# Get Wikipedia summary
try:
	WikiResult = wikipedia.summary(WikiSearch)	
except wikipedia.exceptions.DisambiguationError as WikiError:
	# Solve disambiguation clashes
	WikiError = WikiError.options
	WikiResult = ', '.join(WikiError)
	WikiResult = "This could refer to one of the following, " + WikiResult
except wikipedia.exceptions.PageError as WikiError:
	# Solve missing pages
	WikiResult = "Sorry, no matches found for " + WikiSearch
except:
	# Cope with any other error output
	WikiResult = "Sorry, something has gone horribly wrong"

# Fix encoding (Unicode failures)
WikiResult = WikiResult.encode('utf-8')

#Output to textfile
with open("WikiResult.txt", "w") as text_file:
		text_file.write("%s" % WikiResult)

# Print result/Speak result aloud
print WikiResult
subprocess.call(["festival", "--tts", "WikiResult.txt"])
	

