import sys
from math import sqrt


def quadratic_roots(a, b, c):
    try:
        return (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    except ValueError:
        pass


def main():
    for line in sys.stdin:
        a, b, c = line.strip().split()
        roots = quadratic_roots(int(a), int(b), int(c))

        if roots:
            print('r1 = {}, r2 = {}'.format(roots[0], roots[1]))
        else:
            print(roots)


if __name__ == '__main__':
    main()