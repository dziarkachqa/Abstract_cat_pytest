'''При наследовании классов класс-наследник обычно имеет
больший функционал, чем родительский класс.
 А у котов все наоборот. Кошка по сравнению с котенком умеет ловить мышей (котенок пока нет)
 и мяукает громче (CAPS LOCK`ом). Поэтому логично кошку наследовать от котенка…
Напишите классы:
----Класс АбстрактныйКот (AbstractCat), который инициализируется без аргументов.
Умеет: – eat – есть. За каждые 10 единиц еды вес увеличивается на 1 единицу, пока не станет 100,
дальше не растет. Если при одном приеме пищи количество еды не кратно 10,
остаток запасается, а потом суммируется с новой едой. – возвращать строковое представление в виде <Имя класса> (вес).
-----Класс Котенок (Kitten), наследуется от кота с аргументом вес.
Умеет мяукать тоненько: – meow – возвращает строку "meow..."
Еще умеет спать – sleep – возвращает строку Snore,
повторенную столько раз, сколько число 5 помещается в весе.
-----Класс Кошка (Cat), наследуется от котенка с аргументами вес и кличка.
Умеет мяукать громко (meow): "MEOW..." и возвращать свое имя (get_name).
Также умеет ловить мышей: – catch_mice – возвращает строку: Got it!'''

from src.Kitten import Kitten


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