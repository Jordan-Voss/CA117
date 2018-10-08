import sys

def builddictionary(filename):
	d = {}
	with open(filename, 'r') as file:
		for line in file:
			name, phone = line.strip().split()
			d[name] = phone
	return d

def main():
	d = builddictionary(sys.argv[1])
	for line in sys.stdin:
		name = line.strip()
		print('Name: {}'.format(name))
		if name in d:
			print('Phone: {}'.format(d[name]))
		else:
			print('No such contact')

if __name__ == '__main__':
	main()