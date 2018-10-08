import sys

words_dictionary = {}

def main():
	words = [w.strip() for w in sys.stdin if 5 <= len(w.strip())]
	for word in words:
		words_dictionary[word.casefold()] = True
	print([w for w in words if w[::-1].casefold() in words_dictionary])

if __name__ == '__main__':
	main()
