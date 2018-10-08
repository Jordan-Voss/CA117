class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return '{} {} {}'.format(self.name, self.phone, self.email)


class ContactList(object):

    def __init__(self, d = {}):
        self.cl = d

    def __str__(self):
        header = 'Contact list\n------------\n'
        for k, v in sorted(self.cl.items()):
            header += v.name + ' ' + v.phone + ' ' + v.email + '\n'
        return header.strip()

    def add_contact(self, contact):
        self.cl[contact.name] = contact

    def del_contact(self, name):
        try:
            del self.cl[name]
        except KeyError:
            pass

    def get_contact(self, name):
        try:
            details = self.cl[name]
            return details
        except KeyError:
            return ('{:s} : No such contact'.format(name))
