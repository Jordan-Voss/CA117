import sys

def diamond(s):
	i = 1
	while i < s + 1:
		string = (' ' * ( s - i) + '* ' * i).rstrip()
		print(string)
		i += 1
	i -=2
	while i > 0:
		string = (' ' * (s - i) + '* ' * i).rstrip()
		print(string)
		i -= 1

def main():
	x = int(sys.argv[1])
	diamond(x)

if __name__ == '__main__':
	main()