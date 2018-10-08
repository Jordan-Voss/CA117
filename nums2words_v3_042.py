import sys

mappings = {}

numbers = {0: 'zero',
           1: 'one',
           2: 'two',
           3: 'three',
           4: 'four',
           5: 'five',
           6: 'six',
           7: 'seven',
           8: 'eight',
           9: 'nine',
           10: 'ten'}


def mapping(filename):
    with open(filename, 'r') as f:
        for line in f:
            english, translation = line.strip().split()
            mappings[english] = translation


def main():
    mapping(sys.argv[1])
    for line in sys.stdin:
        tokens = line.strip().split()
        for i, n in enumerate(tokens, 1):
            if i == len(tokens):
                print(mappings[numbers[int(n)]])
            else:
                print(mappings[numbers[int(n)]] + ' ', end='')

if __name__ == '__main__':
    main()