import sys

def main():
	i = 0
	nothing = 0
	pair = 0
	two_pair = 0
	three = 0
	straight = 0
	flush = 0
	full = 0
	four = 0
	sf = 0
	rf = 0
	for line in sys.stdin:
		line = line.strip()
		if line[-1] == '0':
			nothing += 1
		elif line[-1] == '1':
			pair += 1
		elif line[-1] == '2':
			two_pair += 1
		elif line[-1] == '3':
			three += 1
		elif line[-1] == '4':
			straight += 1
		elif line[-1] == '5':
			flush += 1
		elif line[-1] == '6':
			full += 1
		elif line[-1] == '7':
			four += 1
		elif line[-1] == '8':
			sf += 1
		elif line[-1] == '9':
			rf += 1
		i += 1
	print('The probability of nothing is ' + '{:.4f}%'.format(nothing/i * 100))
	print('The probability of one pair is ' + '{:.4f}%'.format(pair/i * 100))
	print('The probability of two pairs is ' + '{:.4f}%'.format(two_pair/i * 100))
	print('The probability of three of a kind is ' + '{:.4f}%'.format(three/i * 100))
	print('The probability of a straight is ' + '{:.4f}%'.format(straight/i * 100))
	print('The probability of a flush is ' + '{:.4f}%'.format(flush/i * 100))
	print('The probability of a full house is ' + '{:.4f}%'.format(full/i * 100))
	print('The probability of four of a kind is ' + '{:.4f}%'.format(four/i * 100))
	print('The probability of a straight flush is ' + '{:.4f}%'.format(sf/i * 100))
	print('The probability of a royal flush is ' + '{:.4f}%'.format(rf/i * 100)) 


if __name__ == '__main__':
	main()







