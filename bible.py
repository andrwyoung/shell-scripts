#!/bin/python
# bible - parse a verse by random or by name
import json
import sys
import random
from pathlib import Path

# file location and error message
home = str(Path.home())
file = home + "/.bin/esv.js"
usage = "usage: bible [book] [chapter] [verse]"

# import data
data = [] 
with open(file) as f:
	data.append(json.load(f))

# main part: parsing the file
# getting book name. if none given, get random one
if len(sys.argv) >= 2:
	book = sys.argv[1]

else:
	book = random.choice(list(data[0]))
# print("Book: " + book)

# see how many chapters are in the book
n_chps = len(data[0][book])
#print("total chapters in " + book + ": " + str(n_chps))
# now get chapter number. if none given, get a random one
if len(sys.argv) >= 3:
	chp = sys.argv[2]
	# making sure it's a valid chapter
	if n_chps < int(chp) or 0 >= int(chp):
		print("ERROR: chapter out of range")
		print(usage)
		sys.exit()
else:
	# assign a random chapter
	chp = str(random.randint(1,n_chps))
#print("chapter: " + chp)

# see how many verses are in the verse
n_vers = len(data[0][book][chp])
#print("total verses in " + book + " " + chp + ": " + str(n_vers))
# now pick a verse. if none given, get a random one
if len(sys.argv) >= 4:
	vers = sys.argv[3]
	#making sure valid chapter
	if n_vers < int(vers) or 0 >= int(vers):
		print("ERROR: verse out of range")
		print(usage)
		sys.exit()
else:
	#assign a random verse
	vers = str(random.randint(1,n_vers))
#print("verse: " + vers)

print(data[0][book][chp][vers])
print(book + " " + chp + ":" + vers)
