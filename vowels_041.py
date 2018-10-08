import sys

vowels = 'aeiou'
vowel_freq = {'a': 0,
              'e': 0,
              'i': 0,
              'o': 0,
              'u': 0}


def vowel_frequencies(s):
    for vowel in vowels:
        vowel_freq[vowel] += s.count(vowel)


def sorter(t):
    return t[1]


def main():
    for line in sys.stdin:
        line = line.strip().casefold()
        vowel_frequencies(line)
    max_width_values = len(str(max(vowel_freq.values())))
    for k, v in sorted(vowel_freq.items(), key=sorter, reverse=True):
        print('{:s} : {:>{}d}'.format(k, v, max_width_values))

if __name__ == '__main__':
    main()