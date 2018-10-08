import sys
 
numbers = list(range(1,999))

def multiple(upto):
	return[n for n in numbers if not n % 3 and n <= int(upto)]

def sq(upto):
	return[n * n for n in numbers if not n % 3 and n <= int(upto)]

def multiple4x2(upto):
	return[n * 2 for n in numbers if not n % 4 and n <= int(upto)]

def multiple3or4(upto):
	return[n for n in numbers if (not n % 3 and n <= int(upto) ) or not n % 4 and n <= int(upto)]

def multiple3and4(upto):
	return[n for n in numbers if not n % 4 and not n % 3 and n <= int(upto)]

def multiple3x(upto):
	return[n if n % 3 else 'X' for n in numbers if n <= int(upto)] 

def prime(upto):
	return[n for n in range(2, int(upto)) if all(n % y != 0 for y in range(2, n))]



def main():
	s = sys.argv[1]
	print('Multiples of 3: {}'.format(multiple(s)))
	print('Multiples of 3 squared: {}'.format(sq(s)))
	print('Multiples of 4 doubled: {}'.format(multiple4x2(s)))
	print('Multiples of 3 or 4: {}'.format(multiple3or4(s)))
	print('Multiples of 3 and 4: {}'.format(multiple3and4(s)))
	print('Multiples of 3 replaced: {}'.format(multiple3x(s)))
	print('Primes: {}'.format(prime(s)))



if __name__ == '__main__':
	main()