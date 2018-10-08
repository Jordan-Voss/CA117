import sys

def capital(s):
	return (s[0].upper() + s[1:-1] + s[-1].upper())
def main():
	for line in sys.stdin:
		if len(line) > 2:
			cw = capital(line.strip())
			print(cw)


if __name__ == '__main__':
	main()