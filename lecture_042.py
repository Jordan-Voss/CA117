import sys

vowels = 'aeiou'
word = 'sequoia'
vset = set(vowels)
wset = set(word)
vset.issubset(wset)
#'True'
vset.intersection(wset) 
# {'a', 'u', 'o', 'i', 'e'}
vset & wset 
# {'a', 'u', 'o', 'i', 'e'}
wset.difference(vset) 
# {'q', 's'}
wset - vset 
# {'q', 's'}

def allvowels2(s):
	vset = set(vowels)
	wset = set(s)
	return vset.issubset(wset)
def canform(letters, word)
	lett = set(letters)
	wor = set(word)
	return lett.issubset(wor)

