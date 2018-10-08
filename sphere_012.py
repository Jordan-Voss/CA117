import sys
import math

def area(x):
    x = 4 * (math.pi) * (x ** 2)
    return x

def volume(x):
    x = (4/3) * (math.pi) * (x ** 3)
    return x

def main():
    n = float(sys.argv[1])
    inc = float(sys.argv[2])
    end = float(sys.argv[3])

    h1 = 'Radius (m)'
    h4 = '-' * len(h1)
    h2 = 'Area (m^2)'
    h5 = '-' * len(h2)
    h3 = 'Volume (m^3)'
    h6 = '-' * len(h3)

    print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3))
    print('{:>s} {:>15s} {:>15s}'.format(h4, h5, h6))

    while n <= end:
        a = area(n)
        v = volume(n)
        print("{0:>10.1f} {1:>15.2f} {2:>15.2f}".format(n, a, v))
        n = n + inc

if __name__ == '__main__':
    main()
