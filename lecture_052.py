import sys

def arithmetic(a, b, c=3, d=4):
	return a + b + c + d

def main():
	print(arithmetic(1, 2, 3, 4))
	print(arithmetic(3, 4, 5))
	print(arithmetic(3, 4))
	print(arithmetic(3, 4, d=3))
	print(arithmetic(4, b=5, d=2, c=1))
if __name__ == '__main__':
	main()

def foo(x):
	x = 33
	print(x)

def main():
	x = 44
	foo(x)
	print(x)

#if a variable name is bound to an object in a function it is local to that function