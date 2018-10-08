import sys

def main():
	for s in sys.stdin:
		s = s.strip().upper()
		a = s.split()[0]
		b = s.split()[1]
		check = True
		for ch in a:
			if ch in b:
				b = b.replace(ch, '')
			else:
				check = False
		print(check)

		




if __name__ == '__main__':
	main()