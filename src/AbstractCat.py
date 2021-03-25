class AbstractCat:

    def __init__(self, weight=0):
        self.weight = weight
        self.saved_food = 0

    def __repr__(self):
        return "{} ({})".format(self.__class__.__name__, self.weight)

    def eat(self, amount):
        self.weight += (amount + self.saved_food) // 10
        if self.weight > 100:
            self.weight = 100
        self.saved_food += (amount + self.saved_food) % 10
