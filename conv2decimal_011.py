import sys

def reverse(s):
	n = ''
	i = 0
	while i < len(s):
		n = s[i] + n
		i += 1
	return n 


def main():
	for line in sys.stdin:
		line = line.strip().split()
		line[0] = reverse(line[0])
		total = 0
		i = 0
		while i < len(line[0]):
			total = total + (int(line[0][i]) * (int(line[1]) ** i))
			i = i + 1
		print(total)


if __name__ == '__main__':
	main()