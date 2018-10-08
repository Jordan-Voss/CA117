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
           10: 'ten',
           11: 'eleven',
           12: 'twelve',
           13: 'thirteen',
           14: 'fourteen',
           15: 'fifteen',
           16: 'sixteen',
           17: 'seventeen',
           18: 'eighteen',
           19: 'nineteen',
           20: 'twenty',
           30: 'thirty',
           40: 'forty',
           50: 'fifty',
           60: 'sixty',
           70: 'seventy',
           80: 'eighty',
           90: 'ninety',
           100: 'one hundred'}


def main():
    for line in sys.stdin:
        tokens = line.strip().split()
        for i, n in enumerate(tokens, 1):
            if int(n) in numbers:
                if i == len(tokens):
                    print(numbers[int(n)])
                else:
                    print(numbers[int(n)] + ' ', end='')
            else:
                if i == len(tokens):
                    print(numbers[int(n[0] + '0')] + '-' + numbers[int(n[1])])
                else:
                    print(numbers[int(n[0] + '0')] + '-' +
                          numbers[int(n[1])] + ' ', end='')


if __name__ == '__main__':
    main()