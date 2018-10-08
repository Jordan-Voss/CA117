import sys
import functools

class Boggle(object):
    positions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    score = [0, 0, 0, 1, 1, 2, 3, 5, 11]

    def __init__(self, words, grid = 4):
        self.words = words
        self.prefix = {w[:i] for w in words for i in range(1 , len(w) + 1)}

    def isinmygrid(self, x, y):
        return x >= 0 <= y and x < len(self.list) > y

    def char(self, x, y, seen):
        return self.isinmygrid(x, y) and (x, y) not in seen

    def deptfirstsearch(self, sysarg, x, y, seen):
        foundwords = set()
        if sysarg not in self.prefix:
            return foundwords
        if sysarg in self.words:
            foundwords.add(sysarg)
        for firstx  , firsty in Boggle.positions:
            newx , newy = firstx + x , firsty + y
            if self.char(newx, newy, seen):
                character = self.list[newy][newx]
                seen.add((x, y))
                foundwords |= self.deptfirstsearch(sysarg + character, newx, newy, seen)
                seen.remove((x, y))
        return foundwords

    def word(self):
        yoda = set()
        for y , up in enumerate(self.list):
            for x, thing in enumerate(up):
                yoda1 = self.deptfirstsearch(thing, x, y, {(x, y)})
                yoda |= yoda1
        return yoda

    def scorethis(self):
        scoreonthis = self.word()
        return sum(Boggle.score[min(8 , len(x))] for x in scoreonthis)

    def createagrid(self, sysarg1, m = 4):
        self.list = [sysarg1[i:i + m] for i in range(0 , m ** 2 , m)]










def newdictionary(words, grid):
    d = set(functools.reduce(lambda x, y: x + y, grid))
    addtothis = set()
    for w in words:
        w = w.strip().lower()
        if len(set(w) & d) == len(set(w)):
            addtothis.add(w)
    return addtothis










def main():
    with open(sys.argv[1]) as a:
        grid = tuple(line.strip() for line in a.readlines())
    with open(sys.argv[2]) as b:
        words = b.readlines()
    inst = newdictionary(words, grid)
    g = Boggle(inst)
    for anything in grid:
        g.createagrid(anything)
        print("Possible points: {}".format(g.scorethis()))
if __name__ == '__main__':
    main()
    # main()