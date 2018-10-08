import sys
totals = {}
disqual = []

s = {-4 : 6, -3 : 5, -2 : 4, -1 : 3, 0 : 2, 1 : 1,}
def sorter(t):
    return t[1]
def main():
    a = [l.strip().split() for l in sys.stdin]
    par = a[0]
    index = a[1]
    final_score = {}
    names = []
    for line in a[2:]:
        name = " ".join(line[:-19])
        names.append(name)
        hcap = int(line[-19])
        shots = line[-18:]
        totals[name] = 0
        for i, shot in enumerate(shots):
            try:
                shot = int(shot)
                idx = int(index[i])
                current_par = int(par[i])
                if hcap >= 1 and hcap <= 18:
                    if idx <= hcap:
                        net = shot - 1
                    else:
                        net = shot
                elif hcap > 18 and hcap <= 36:
                    if idx <= hcap - 18:
                        net = shot - 2
                    else:
                        net = shot - 1
                elif hcap > 36 and hcap <= 54:
                    if idx <= hcap - 36:
                        net = shot - 3
                    else:
                        net = shot - 2
                else:
                    net = shot

                distance_from_par = net - current_par
                if distance_from_par in s:
                    totals[name] += s[distance_from_par]
            except ValueError:
                if name not in disqual and shot != 'X':
                    disqual.append(name)
                    totals[name] = 0
                
        final_score[name] = totals[name]
    names = sorted(names, key=len, reverse = True)
    for n, scr in sorted(final_score.items(), key=sorter, reverse=True):
        print("{:>{}} : {:2}".format(n, len(names[0]), scr))



if __name__ == "__main__":
    main()