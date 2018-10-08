import sys

def contains(x,y):
	for letter in x:
		if letter in y:
			y = x.replace(letter, '', 1)
		else:
			return False
	return True


def main():
	for line in sys.stdin:
		[left, right] = line.strip().split()
		print(contains(left,right))

if __name__ == '__main__':
	main()