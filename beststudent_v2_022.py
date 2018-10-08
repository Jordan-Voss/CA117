import sys

def main():
	try:
		best = ''
		highest = 0
		f = open(sys.argv[1], 'r')
		try:
			for line in f:
				line = line.strip().split()
				mark = int(line[0])
				name = ' '.join(line[1:])
				if mark > highest:
					highest = mark
					best = name 
			print('Best student: ' + best)
			print('Best mark: ' + str(highest))
		except ValueError:
			print('Invalid mark {} encountered. Exiting.'.format(line[0]))



	except FileNotFoundError:
		print('The file {} could not be found'.format(sys.argv[1]))
			

if __name__ == '__main__':
	main()
