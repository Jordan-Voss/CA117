import sys


def sumFac(n):
    return sum([i for i in range(1, (n // 2) + 1) if not n % i])


def isPerfect(n):
    return n == sumFac(n)


def main():
    for n in sys.stdin:
        print(isPerfect(int(n.strip())))

if __name__ == '__main__':
    main()