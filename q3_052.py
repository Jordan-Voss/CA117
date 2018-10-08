import sys



def build_dictionary(filename):
    with open(filename) as f:
    	lines = [l.strip().split() for l in f]
    	return {l[0]: int(l[1]) for l in lines}



def extract_range(d, low, high):
	return {k: v for (k, v) in d.items() if low <= v <= high}



def main():
    d = build_dictionary(sys.argv[1])
    d2 = extract_range(d, 5, 15)
    print(*d2.items(), sep="\n")


if __name__ == '__main__':
    main()