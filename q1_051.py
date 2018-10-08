import sys

def main():
	word = sys.argv[1]

	for i in range(0, len(word), 2):
		print(end=word[i:i+2][::-1])

	print()

if __name__ == '__main__':
	main()