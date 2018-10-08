class Customer(object):

    discount = 0.0

    def __init__(self, name, balance, addr_line1, addr_line2, addr_line3):
        self.name = name
        self.balance = balance
        self.addr_line1 = addr_line1
        self.addr_line2 = addr_line2
        self.addr_line3 = addr_line3

    def __str__(self):
        l = []
        l.append('{:s}'.format(self.name))
        l.append('{:s}'.format(self.addr_line1))
        l.append('{:s}'.format(self.addr_line2))
        l.append('{:s}'.format(self.addr_line3))
        l.append('Balance: {:.2f}'.format(self.balance))
        l.append('Discount: {:d}%'.format(int(self.discount * 100)))
        l.append('Amount due: {:.2f}'.format(self.owes()))
        return '\n'.join(l)

    def owes(self):
        discounted = self.balance * self.discount
        return self.balance - discounted


class ValuedCustomer(Customer):

    discount = 0.1