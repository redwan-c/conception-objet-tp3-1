from tp2 import *

def test_box_create():
    b = Box ()

def test_box_add():
    b = Box ()
    b.add("truc1")
    b.add("truc2")

def test_box_in():
    b = Box ()
    b.add("truc1")
    b.add("truc2")

    assert "truc1" in b
    assert "truc2" in b

    def test_box_remove ():
    b = Box ()
    b.add("truc1")
    b.remove("truc2")

    assert "truc2" not in b