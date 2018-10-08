import sys

vowels = "aeiou"

def match(s):
	if False in [s.count(c) == 1 for c in vowels]:
		return False

	indexes = [s.index(c) for c in vowels]
	return indexes == sorted(indexes)




def main():
	words = [l.strip() for l in sys.stdin]
	print(*[w for w in words if match(w.lower())], sep="\n")



if __name__ == '__main__':
	main()