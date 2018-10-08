import sys

def main():
	word = sys.argv[1]
	n = int(sys.argv[2]) % len(word)

	print(word[-n:], word[:-n], sep="")



if __name__ == '__main__':
	main()