import sys
x = []
def reverse(words_list):
	return[w for w in words_list if len(w) >= 5 and w.strip().casefold()[::-1] in words_list]

def main():
	line = sys.stdin.read()
	for l in line:
		x.append(reverse(l))
	print(x)





if __name__ == '__main__':
	main()