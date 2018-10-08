import sys

def main():
	try:
		highest = 0
		f = open(sys.argv[1], 'r')
		for line in f:
			line = line.split()
			if int((line[0].strip())) > highest:
				highest = int((line[0].strip()))
				best = ' '.join(line[1:])
		print('Best student: ' + best)
		print('Best mark: ' + str(highest))
	except FileNotFoundError:
		print('The file {} could not be found'.format(sys.argv[1]))


if __name__ == '__main__':
	main()

