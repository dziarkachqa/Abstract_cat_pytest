import pytest
from scr.AbstractCat import AbstractCat
from scr.Cat import Cat

@pytest.fixture
def my_abstract_cat():
    return AbstractCat()

@pytest.fixture
def my_cat():
    return Cat(100, "Molly")