def test_cat_meow(my_cat):
    assert my_cat.meow() == "MEOW..."

def test_cat_get_name(my_cat):
    assert my_cat.get_name() == "Molly"

def test_cat_catch_mice(my_cat):
    assert my_cat.catch_mice() == "Got it!"

def test_cat_waigth(my_cat):
    assert my_cat.weight == 73