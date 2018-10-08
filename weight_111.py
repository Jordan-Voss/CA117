class Weight(object):

    OUNCES_PER_POUND = 16

    def __init__(self, pounds=0, ounces=0):
        self.pounds = pounds
        self.ounces = ounces

    @classmethod
    def from_ounces(cls, ounces):
        pounds, ounces = divmod(ounces, cls.OUNCES_PER_POUND)
        return cls(pounds, ounces)

    def __str__(self):
        return '{:d} pound(s) and {:d} ounce(s)'.format(self.pounds, self.ounces)

    def to_ounces(self):
        return (self.pounds * self.OUNCES_PER_POUND) + self.ounces

    def __ne__(self, other):
        return self.to_ounces() != other.to_ounces()

    def __eq__(self, other):
        return self.to_ounces() == other.to_ounces()

    def __lt__(self, other):
        return self.to_ounces() < other.to_ounces()

    def __le__(self, other):
        return self.to_ounces() <= other.to_ounces()

    def __gt__(self, other):
        return self.to_ounces() > other.to_ounces()

    def __ge__(self, other):
        return self.to_ounces() >= other.to_ounces()

    def __add__(self, other):
        return self.from_ounces(self.to_ounces() + other.to_ounces())

    def __iadd__(self, other):
        z = self + other
        self.pounds, self.ounces = z.pounds, z.ounces
        return self

    def __mul__(self, n):
        return self.from_ounces((self.to_ounces() * n))
