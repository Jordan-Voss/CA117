import sys

def readint():
	print('Please enter an Integer')
	while True:
		try:
			x = input()
			d = int(x)
			break
		except ValueError:
			print('I said an *Integer*...')
	return d

def readfile(filename):
	try:
		with open(filename, 'r') as f:
			for line in f:
				try:
					line = line.split()
					person = ' '.join(line[0:-1])
					mark = int(line[-1])
					if mark < 40:
						result = 'failed'
					elif mark >= 40:
						result = 'passed'
					print('{:} {:} with {:}'.format(person, result, mark))
				except ValueError:
					pass
	except FileNotFoundError:
		print('Could Not Open File: {}'.format(filename))
	except PermissionError:
		print('Permission Error on file: {}'.format(filename))
	else:
		print('successfully opened the file...')
	finally:
		print('Leaving the function...')


def main():
	s = readfile(sys.argv[1])
	

	


if __name__ == '__main__':
	main()



	def readfile(filename):
	f = open(filename, 'r')
	for line in f:
		return(line.strip())
	f.close()