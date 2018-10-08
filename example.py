import sys

def getevens(numbers):
	return [n for n in numbers if not n % 2]
def getodds(numbers):
	#odds = []
	#for number in numbers:
	#	if number % 2 == 1:
	#		odds.append(number)
#	return odds


	# List Comprehension
	return [n for n in numbers if n % 2 ]
def getsqevens(numbers):
	return [n ** 2 for n in numbers if not n % 2]
def getvowels(sentence):
    return [c for c in sentence if c not in 'aeiouAEIOU']

def ispal(line):
	w = [l.casefold() for l in line if l.isalnum()]
	return w[::-1] == w

def isprime():
	
def getprimes(numbers):
	[n for n in numbers if]



def main():
	for line in sys.stdin:
		odds = getodds(line)
		print(odds)


if __name__ == '__main__':
	main()