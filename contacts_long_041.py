import sys

def builddictionary(filename):
	d = {}
	with open(filename, 'r') as f:
		for line in f:
			name, phone, email = line.strip().split()
			d[name] = (phone, email)
	return d



def main():
	d = builddictionary(sys.argv[1])
	for line in sys.stdin:
		name = line.strip()
		print('Name: {}'.format(name))
		if name in d:
			print('Phone: {}'.format(d[name][0]))
			print('Email: {}'.format(d[name][1]))
		else:
			print('No such contact')


if __name__ == '__main__':
	main()