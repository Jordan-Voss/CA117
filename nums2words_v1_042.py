import sys

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


def main():
    for line in sys.stdin:
        tokens = line.strip().split()
        for i, n in enumerate(tokens, 1):
            if i == len(tokens):
                print(numbers[int(n)])
            else:
                print(numbers[int(n)] + ' ', end='')


if __name__ == '__main__':
    main()