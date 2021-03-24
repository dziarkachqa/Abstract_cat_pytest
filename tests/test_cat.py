from scr.Cat import Cat

def test_cat_meow(my_cat):
    assert my_cat.meow() == "MEOW..."

def test_cat_get_name(my_cat):
    assert my_cat.get_name() == "Molly"