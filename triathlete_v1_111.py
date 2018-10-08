class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        l = []
        l.append('Name: {:s}'.format(self.name))
        l.append('ID: {:d}'.format(self.tid))
        return '\n'.join(l)