import sys


def qnotu(s):
    return 'q' in s and s.count('q') > s.count('qu')


def main():
    words = []

    for line in sys.stdin:
        words.append(line.strip())

    print('Words with q but no u: {}'.format([word for word in words if qnotu(word.casefold())]))

if __name__ == '__main__':
    main()