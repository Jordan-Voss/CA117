import sys

def palindrome(x):
	lin = ''
	pal = ''
	x = x.casefold()
	i = 0
	while i < len(x):
		if x[i].isdigit() or x[i].isalpha():
			lin = x[i] + lin
		i += 1
		j = 0
	while j < len(lin)/2 and lin[j] == lin[len(lin) -j -1]:
		j += 1
	if len(lin) == 1:
		return 'True'
	elif lin[j] == lin[len(lin) -j -1]:
		return 'True'
	else:
		return 'False'

def main():
	for line in sys.stdin:
		pa = palindrome(line)
		print(pa)
		


if __name__ == '__main__':
	main()