import sys


def validate_times(times):
    for t in times:
        t = t.split(":")
        if not (len(t) == 2 and t[0].isdigit() and t[1].isdigit()):
            return False

    return True


def times_to_secs(times):
    times = [list(map(int, t.split(":"))) for t in times]
    return [t[0] * 60 + t[1] for t in times]


def secs_to_mins(t):
    return "{}:{:0>2}".format(t // 60, t % 60)


def main():
    lines = [l.strip().split() for l in sys.stdin]
    best_times = [(l[0], min(times_to_secs(l[1:])))
                  for l in lines if validate_times(l[1:])]
    best_runner = min(best_times, key=lambda l: l[1])
    print(best_runner[0], ":", secs_to_mins(best_runner[1]))


if __name__ == '__main__':
    main()