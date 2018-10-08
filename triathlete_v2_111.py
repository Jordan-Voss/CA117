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

    def add_time(self, discipline, time):
        self.times[discipline] = time
        self.race_time += time

    def get_time(self, discipline):
        return self.times[discipline]