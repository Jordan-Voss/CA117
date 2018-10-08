import sys


def read_calorie_data(filename):
    with open(filename) as f:
        lines = [l.strip().split() for l in f]
        return {" ".join(l[:-1]): int(l[-1]) for l in lines}


def main():
    calorie_data = read_calorie_data(sys.argv[1])
    diets = [l.strip().split(",") for l in sys.stdin]

    calories = {s[0]: sum(calorie_data.get(c, 100)
                          for c in s[1:]) for s in diets}

    max_name_len = max(len(n) for n in calories)
    max_cals_len = max(len(str(x)) for x in calories.values())
    for name, cals in sorted(calories.items(), key=lambda x: x[1]):
        print("{:>{}} : {:>{}}".format(name, max_name_len, cals, max_cals_len))


if __name__ == '__main__':
    main()