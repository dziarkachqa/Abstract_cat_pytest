from src.AbstractCat import AbstractCat


class Kitten(AbstractCat):

    def __init__(self, weight):
        super().__init__(weight)

    def meow(self):
        return "meow..."

    def sleep(self):
        return (self.weight // 5) * "Snore"


if __name__ == "__main__":
    k = Kitten(10)
    print(k.meow())

