import sys

def lower(x):
	i = 0
	for letter in x:
		if letter.islower():
			i += 1
		if i > 0:
			j = 1
			letter.replace(letter,' ')
		else:
			j = 0
	return j

def upper(x):
	i = 0
	for letter in x:
		if letter.isupper():
			i += 1
		if i > 0:
			j = 1
			letter.replace(letter,' ')
		else:
			j = 0
	return j
def digit(x):
	i = 0
	for letter in x:
		if letter.isdigit():
			i += 1
		if i > 0:
			j = 1
			letter.replace(letter,' ')
		else:
			j = 0
	return j

def symbol(x):
	i = 0
	for letter in x:
		if not letter.isalnum():
			i += 1
		if i > 0:
			j = 1
			letter.replace(letter,' ')
		else:
			j = 0
	return j


def main():
	for line in sys.stdin:
		passw = lower(line.strip()) + upper(line.strip()) + digit(line.strip()) + symbol(line.strip())
		print(passw)


if __name__ == '__main__':
	main()