class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def greater_than(self, score):
        return self.goals * 3 + self.points > score.goals * 3 + score.points

    def less_than(self, score):
        return self.goals * 3 + self.points < score.goals * 3 + score.points

    def equal_to(self, score):
        return self.goals * 3 + self.points == score.goals * 3 + score.points