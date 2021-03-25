import pytest
from src.Kitten import Kitten

def test_kitten_meow(my_kitten):
    assert my_kitten.meow() == "meow..."

def test_kitten_sleep(my_kitten):
    assert my_kitten.sleep() == "SnoreSnoreSnoreSnoreSnoreSnoreSnore"

@pytest.mark.parametrize("amount,expected_snore",[(68,"Snore"),(100,"Snore"*2),(3000,"Snore"*20),(-8,"")])
def test_kitten_sleep1(my_abstract_cat, amount, expected_snore):
    my_abstract_cat.eat(amount)
    my_kitten = Kitten(my_abstract_cat.weight)
    assert my_kitten.sleep() == expected_snore

# def test_kitten_sleep1(my_abstract_cat):
#     my_abstract_cat.eat(68)
#     my_kitten1 = Kitten(my_abstract_cat.weight)
#     assert my_kitten1.sleep() == "Snore"
#
# def test_kitten_sleep2(my_abstract_cat):
#     my_abstract_cat.eat(100)
#     my_kitten1 = Kitten(my_abstract_cat.weight)
#     assert my_kitten1.sleep() == "SnoreSnore"
#
# def test_kitten_sleep3(my_abstract_cat):
#     my_abstract_cat.eat(3000)
#     my_kitten1 = Kitten(my_abstract_cat.weight)
#     assert my_kitten1.sleep() == "Snore"*20
#
# def test_kitten_sleep4(my_abstract_cat):
#     my_abstract_cat.eat(-8)
#     my_kitten1 = Kitten(my_abstract_cat.weight)
#     assert my_kitten1.sleep() == ""