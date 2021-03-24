from scr.Kitten import Kitten


class Cat(Kitten):

    def __init__(self, weight, name):
        super().__init__(weight)
        self.name = name

    def meow(self):
        return super().meow().upper()

    def get_name(self):
        return self.name

    def catch_mice(self):
        return "Got it!"