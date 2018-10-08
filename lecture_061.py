import sys
def append2list(l1, l2=[]):
	for e in l1:
		l2.append(e)
	return l2
def fixed(l1, l2=None):
	if l2 is None:
		l2 = []
	for e in l1:
		l2.append(e)
	return l2


def main():
	list1= ['pony', 'penguin']
	new_list = fixed(list1)
	print(new_list)

if __name__ == '__main__':
	main()