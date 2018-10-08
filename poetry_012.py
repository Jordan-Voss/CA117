import sys

def main():
	longest = 0
	lines = []
	for line in sys.stdin:
		line = line.strip()
		lines.append(line)
		if len(line) > longest:
			longest = len(line)
		for token in line:
			print('{:^{}s}'.format(token, longest))
		
		

if __name__ == '__main__':
	main()
