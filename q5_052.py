import sys


def validate_scores(scores):
    try:
        [int(x) for x in scores]
    except ValueError:
        return False

    return True


def main():
    lines = [l.strip().split(":") for l in sys.stdin]
    students = [(l[0], l[1].split(",")) for l in lines]

    valid_students = [s for s in students if validate_scores(s[1])]
    valid_students = [(s[0], sum(map(int, s[1]))) for s in valid_students]
    invalid_students = [s for s in students if not validate_scores(s[1])]

    for name, score in sorted(valid_students, key=lambda x: x[1], reverse=True):
        print(name, ":", score)

    print("Skipped:")
    for s in invalid_students:
        print(s[0])


if __name__ == '__main__':
    main()