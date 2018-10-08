import sys

def token(x):
	x = x.split()
	return int(len(x))

def main():
	tok = 0
	for line in sys.stdin:
		tok = token(line) + tok
	print(tok)

if __name__ == '__main__':
	main()