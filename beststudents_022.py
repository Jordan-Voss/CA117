import sys

def main():
	try:
		i = 0
		results = []
		best = []
		highest = 0
		f = open(sys.argv[1], 'r')
		for line in f:
			results.append(line)
			line = line.strip().split()
			try:
				mark = int(line[0])
				name = ' '.join(line[1:])
				if mark > highest:
					highest = mark
			except ValueError:
				pass
			
		every = ''.join(results)

		x = every.split('\n')
		
		while i < len(x):
			mark = x[i][:2]
			name = x[i][3:]
			try:
				if int(mark) == int(highest):
					best.append(name)
			except ValueError:
				pass
			i += 1

		print('Best student(s): ' + ', '.join(best))
		print('Best mark: ' + str(highest))



	except FileNotFoundError:
		print('The file {} could not be found'.format(sys.argv[1]))
			

if __name__ == '__main__':
	main()
