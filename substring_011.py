import sys

def sub(s):
	return s.casefold().split()

def main():
	for line in sys.stdin:
		sl = sub(line.strip())
		if sl[0] in sl[1]:
			print ('True')
		else:
			print('False')

if __name__ == '__main__':
	main()