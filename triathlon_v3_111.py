class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {}
        self.race_time = 0

    def __str__(self):
        l = []
        l.append('Name: {:s}'.format(self.name))
        l.append('ID: {:d}'.format(self.tid))
        l.append('Race time: {:d}'.format(self.race_time))
        return '\n'.join(l)

    def __eq__(self, other):
        return self.race_time == other.race_time

    def __lt__(self, other):
        return self.race_time < other.race_time

    def __gt__(self, other):
        return self.race_time > other.race_time

    def add_time(self, discipline, time):
        self.times[discipline] = time
        self.race_time += time

    def get_time(self, discipline):
        return self.times[discipline]


class Triathlon(object):

    def __init__(self):
        self.mapping = {}

    def __str__(self):
        l = []
        for e in sorted(self.mapping.values(), key=lambda x: x.name):
            l.append('Name: {:s}'.format(e.name))
            l.append('ID: {:d}'.format(e.tid))
        return '\n'.join(l)

    def add(self, triathlete):
        self.mapping[triathlete.tid] = triathlete

    def remove(self, tid):
        del(self.mapping[tid])

    def lookup(self, tid):
        if tid in self.mapping:
            return self.mapping[tid]
        return None

    def best(self):
        return min(self.mapping.values(), key=lambda x: x.race_time)

    def worst(self):
        return max(self.mapping.values(), key=lambda x: x.race_time)