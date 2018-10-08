import sys
import string

def builddictionary():
	d = {}
	for line in sys.stdin:
		words = line.lower().strip().split()
		for word in words:
			word = word.strip(string.punctuation)
			if word == '':
				continue
			if not word in d:
				d[word] = 1
			else:
				d[word] += 1
	return d

def main():
	d = builddictionary()
	nd = {}
	for (k,v) in sorted(d.items()):
		if len(k) > 3 and int(v) >= 3:
			nd[k] = v
	width = len(max(nd.keys(), key=len))

	for (k,v) in sorted(nd.items()):
		print('{:>{:d}} : {:>2d}'.format(k, int(width), v))

	



if __name__ == '__main__':
	main()
