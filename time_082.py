from functools import total_ordering


@total_ordering
class Time:

    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s

    def __str__(self):
        return "The time is {:0>2}:{:0>2}:{:0>2}".format(self.hour, self.minute, self.second)


    def __eq__(self, other):
        return self.time_to_seconds() == other.time_to_seconds()

    def __gt__(self, other):
        return self.time_to_seconds() > other.time_to_seconds()

    def __add__(self, other):
        tot = self.time_to_seconds() + other.time_to_seconds()
        return self.seconds_to_time(tot)

    def __iadd__(self, other):
        tot = self.time_to_seconds() + other.time_to_seconds()
        self.hour, over = divmod(tot, 3600)
        self.hour %= 24
        self.minute, self.second = divmod(over, 60)
        return self

    def time_to_seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    @classmethod
    def seconds_to_time(cls, seconds):
        h, over = divmod(seconds, 3600)
        h %= 24
        m, s = divmod(over, 60)
        return Time(h, m, s)