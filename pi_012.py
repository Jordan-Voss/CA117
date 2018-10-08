import sys

def dec(x):
	from math import pi
	return '{:.{}f}'.format(pi, x)
def main():
	line = sys.argv[1]
	pl = dec(int(line))
	print(pl)

if __name__ == '__main__':
	main()