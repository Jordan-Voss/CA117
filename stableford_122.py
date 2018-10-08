import sys
totals = {}
disqual = []

s = {
	-7 : 9,
	-6 : 8,
	-5 : 7,
	-4 : 6,
	-3 : 5,
	-2 : 4,
	-1 : 3,
	 0 : 2,
	 1 : 1,
	 }
def sorter(t):
    return t[1]
def main():
    a = [l.strip().split() for l in sys.stdin]
    par = a[0]
    index = a[1]
    final = {}
    names = []
    for line in a[2:]:
        name = " ".join(line[:-19])
        names.append(name)
        handicap = int(line[-19])
        shots = line[-18:]
        totals[name] = 0
        for n, shot in enumerate(shots):
            try:
                shot = int(shot)
                indx = int(index[n])
                current_par = int(par[n])
                if handicap >= 1 and handicap <= 18:
                    if indx <= handicap:
                        net = shot - 1
                    else:
                        net = shot
                elif handicap > 18 and handicap <= 36:
                    if indx <= handicap - 18:
                        net = shot - 2
                    else:
                        net = shot - 1
                elif handicap > 36 and handicap <= 54:
                    if indx <= handicap - 36:
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
        if name not in disqual:        
        	final[name] = totals[name]
    names = sorted(names, key=len, reverse = True)
    for n, score in sorted(final.items(), key=sorter, reverse=True):
        print("{:>{}} : {:2}".format(n, len(names[0]), score))
    for name in disqual:
    	print("{:>{}} : {:2}".format(name, len(names[0]), 'Disqualified'))



if __name__ == "__main__":
    main()
