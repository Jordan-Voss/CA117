class Student(object):

    def __init__(self, surname, forename, sid, modlist=[]):
        self.sid = int(sid)
        self.surname = surname
        self.forename = forename
        self.modlist = modlist

    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)

    def del_module(self, module):
        try:
            self.modlist.remove(module)
        except ValueError:
            pass

    def print_details(self):
        print('ID: {:d}'.format(self.sid))
        print('Surname: {:s}'.format(self.surname))
        print('Forename: {:s}'.format(self.forename))
        print('Modules: {:s}'.format(' '.join(self.modlist)))