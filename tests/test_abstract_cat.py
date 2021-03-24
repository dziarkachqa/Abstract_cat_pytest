from scr.AbstractCat import AbstractCat

def test_cat_initialization(my_abstract_cat):
    assert isinstance(my_abstract_cat, AbstractCat)

def test_cat_eat1(my_abstract_cat):
    my_abstract_cat.eat(10)
    assert my_abstract_cat.weight == 1

def test_cat_eat_more_then_100(my_abstract_cat):
    my_abstract_cat.eat(2000)
    assert my_abstract_cat.weight == 100

def test_eat_less_10(my_abstract_cat):
    my_abstract_cat.eat(9)
    assert my_abstract_cat.weight == 0

def test_leftover(my_abstract_cat):
    my_abstract_cat.eat(12)
    assert my_abstract_cat.saved_food == 2

def test_cat_save_food(my_abstract_cat):
    weight = my_abstract_cat.weight
    my_abstract_cat.eat(12)
    my_abstract_cat.eat(18)
    assert my_abstract_cat.weight == weight + 3
