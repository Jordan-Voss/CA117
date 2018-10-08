import sys

pattern = "evil"

def is_evil(s):
	for c in pattern:
		if s.count(c) != 1:
			return False

	ind = [s.index(c) for c in pattern]

	return ind == sorted(ind)


def main():
	words = [l.strip() for l in sys.stdin]
	print(*[w for w in words if is_evil(w.lower())], sep="\n")

if __name__ == '__main__':
	main()