#This program finds a word ladder between two words by changing one letter at a time, ensuring each word in between is also a valid English word. 

import string

alphabets = string.ascii_lowercase

def formatSequence(sequence):
	sequenceLength = len(sequence)

	print "The shortest path has length",sequenceLength,":"

	# for word in sequence:
	# 	word = lstToWord(word)
	# 	print word, "->",

	for idx, wordL in enumerate(sequence):
		if idx != len(sequence) - 1:
			print lstToWord(wordL), "->",
		else:
			print lstToWord(wordL)
	
def lstToWord(lst):
	return "".join(lst)


allWords = set()
usedWords = set()

with open("words.txt") as f:
	for line in f:
		allWords.add(line.strip())

def oneLetterModifications(word):
	oneLetterChanged = []

	for index, letter in enumerate(word):
		for alpha in alphabets:
			newWord = list(word)

			if alpha != letter:
				newWord[index] = alpha
				if lstToWord(newWord) in allWords and lstToWord(newWord) not in usedWords:
					oneLetterChanged.append(newWord)
					usedWords.add(lstToWord(newWord))

	return oneLetterChanged

def wordLadder(word1,word2):
	usedWords.add(word1)
	word1L = list(word1)
	word2L = list(word2)


	if word1 == word2:
		print "the words cannot be the same"
		return
	if len(word1) != len(word2):
		print "the words must be the same length"
		return
	if word1 not in allWords or word2 not in allWords:
		print "one of these words are not English words"
		return

	allSequences = []
	allSequences.append([word1L])

	while len(allSequences) > 0:

		currentSequences = allSequences.pop(0)

		#import pdb; pdb.set_trace()

		lastWord = currentSequences[len(currentSequences)-1]

		if lastWord == word2L: 
			#print "DONE !@#!@##!@#!!!"
			#print currentSequences
			formatSequence(currentSequences)
			return 
		# call oneLetterModifications 

		lastWordModifications = oneLetterModifications("".join(lastWord))

		# iterate through each element of oneletterModifications and append to allSequences

		for elem in lastWordModifications:
			newSequence = list(currentSequences)
			newSequence.append(elem)
			allSequences.append(newSequence)


	print "there was no path between the words"


#wordLadder("code","data")
wordLadder("code","data")

# print oneLetterModifications("code")
# print oneLetterModifications("data")
# print oneLetterModifications("nice")
