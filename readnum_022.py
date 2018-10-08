import sys

def main():
	while True:
		try:
			x = input()
			d = int(x)
			break
		except ValueError:
			print('{} is not a number'.format(x))
	print('Thank you for {}'.format(d))

if __name__ == '__main__':
	main()
	