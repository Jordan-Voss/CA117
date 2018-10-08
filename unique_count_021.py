import sys
import string

def token(x):
	seen = []
	for i in x: 
		sent = i.split()
		for word in sent:
			word = word.lower()
			for letter in word:
				if letter in string.punctuation:
					word = word.replace(letter, "")
			if word not in seen:
				seen.append(word)
	return len(seen) - 1

def main():
   s = sys.stdin.readlines()
   print (token(s))

if __name__ == "__main__":
   main()