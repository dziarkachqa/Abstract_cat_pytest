import pytest
from src.AbstractCat import AbstractCat
from src.Cat import Cat
from src.Kitten import Kitten


@pytest.fixture
def my_abstract_cat():
    return AbstractCat()


@pytest.fixture
def my_cat():
    return Cat(73, "Molly")


@pytest.fixture
def my_kitten():
    return Kitten(35)