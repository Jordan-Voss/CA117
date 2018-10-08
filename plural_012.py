import sys
es_endings = ['ch', 'sh', 'x', 's','z','o']
y_endings = ['ay', 'ey','oy', 'iy','uy']

def plural(x):
	if x[-2:] in es_endings or x[-1] in es_endings:
		x = x + 'es'
	elif x[-2:] not in y_endings or x[-1] in y_endings:
		x = x[:-1] + 'ies'
	elif x.rsplit('f',1):

	else:
		x = x + 's' 
	return x


def main():
	for line in sys.stdin:
		pl =  plural(line.strip())
		print(pl)

if __name__ == '__main__':
	main()

import sys

def plural(x):
	t = ""
	if x[-2:] == 'ch' or x[-2:] == 'sh' or x[-1] == 'x' or x[-1] == 's' or x[-1] == 'z' or x[-1] == 'o':
		t = x + 'es'
	elif x[-2:] == 'fe':
		t = x[:-2] + 'ves'
	elif x[-1] == 'f':
		t = x[:-1] + 'ves'
	elif x[-1] == 'y' and x[-2:] != 'ay' and x[-2:] != 'ey' and x[-2:] != 'iy' and x[-2:] != 'oy' and x[-2:] != 'uy':
		t = x[:-1] + 'ies'
	else:
		t = x + 's' 
	return t

def main():
	for line in sys.stdin:
		pl =  plural(line.strip())
		print(pl)

if __name__ == '__main__':
	main()