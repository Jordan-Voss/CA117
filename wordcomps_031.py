import sys

def contain17(words):
	return [w for w in words if len(w) == 17]


def contain18(words):
	return [w for w in words if len(w) > 17]

def shortvowel(words):
	return(min([w for w in words if all(c in w for c in list("aeiou"))], key=len))

def ax4(words):
	return [w for w in words if w.casefold().count('a') == 4]

def more2q(words):
	return [w for w in words if w.casefold().count('q') >= 2]

def containcie(words):
	return [w for w in words if 'cie' in w]

def letters(w):
	return 'a' in w and 'n' in w and 'g' in w and 'l' in w and 'e' in w
	
def angle(words):
	return [w for w in words if letters(w.casefold()) and len(w) == 5 and w != 'angle']

def ending(words):
	return len([w for w in words if w[-4:] == 'iary'])

def qu(words):
	return [w for w in words if 'q' in w.casefold() and 'u' not in w.casefold()]

def e(words):
	high_e =0
	for w in words:
		if w.casefold().count('e') > high_e:
			high_e = w.casefold().count('e')
	return [w for w in words if w.count('e') == high_e]

	


def main():
	s = [w.strip() for w in sys.stdin]


	print('Words containing 17 letters: {}'.format(contain17(s)))
	print('Words containing 18+ letters: {}'.format(contain18(s)))
	print('Shortest word containing all vowels: {}'.format(shortvowel(s)))
	print("Words with 4 a's: {}".format(ax4(s)))
	print("Words with 2+ q's: {}".format(more2q(s)))
	print("Words containing cie: {}".format(containcie(s)))
	print("Anagrams of angle: {}".format(angle(s)))
	print("Words ending in iary: {}".format(ending(s)))
	print("Words with q but no u: {}".format(qu(s)))
	print("Words with most e's: {}".format(e(s)))
	

	
if __name__ == '__main__':
	main()