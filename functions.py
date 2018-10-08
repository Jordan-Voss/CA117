import sys

def allvowels(w):
	return 'a' in w and 'e' in w and 'i' in w and 'o' in w and 'u' in w

def extractwords(words):
	vowel = 'aeiou'
	return [w for w in words if allvowels(w.casefold())]