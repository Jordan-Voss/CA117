import sys


def upper_seq(s):

    len_longest = 0
    ind_longest = 0

    i = j = 0
    while i < len(s):
        while j < len(s) and not s[j].isupper():
            j += 1

        i = j

        while j < len(s) and s[j].isupper():
            j += 1

        if j - i > len_longest:
            len_longest = j - i
            ind_longest = i

    return s[ind_longest:ind_longest + len_longest]


def main():
    strings = [l.strip() for l in sys.stdin]
    print(*[upper_seq(s) for s in strings], sep="\n")


if __name__ == '__main__':
    main()