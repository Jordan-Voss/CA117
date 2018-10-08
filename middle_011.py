import sys
def mid(s):
 	if len(s) % 2 != 0 :
 		return (s[len(s) // 2])
 	else:
 		return ('No middle character!')

def main():
	for line in sys.stdin:
		ml = mid(line.strip())
		print(ml)

if __name__ == '__main__':
	main()