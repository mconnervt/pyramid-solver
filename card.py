class Card:
    def __init__(self, suit, value):
        self.s = suit
        self.v = value
    def __str__(self):
        return self.s + self.v