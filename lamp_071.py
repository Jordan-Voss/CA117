class Lamp(object):
    def __init__(self, on=False):
        self.on = on

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def toggle(self):
        if self.on:
            self.on = False
        else:
            self.on = True