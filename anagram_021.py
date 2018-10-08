import sys

def anagram(x):
	x = x.split()
	first = x[0]
	second = x[1]
	for letter in first:

		if letter in second:
			first.replace(letter, '', 1)
		else:
			return False
	return second == ''



		if len(second) > 0 and len(first) == len(second):
			return True
		else:
			return False


def main():
	for line in sys.stdin:
		print(anagram(line))



if __name__ == '__main__':
	main()