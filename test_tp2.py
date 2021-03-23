from tp2 import *

def test_box_create():
    b = Box()

def test_box_add():
    b = Box()
    b.add("truc1")
    b.add("truc2")

def test_box_in():
    b = Box()
    b.add("truc1")
    b.add("truc2")

    assert "truc1" in b
    assert "truc2" in b

def test_box_remove ():
    b = Box()
    b.add("truc1")
    b.remove("truc2")

    assert "truc2" not in b

def test_box_open():
    b= Box()
    b.open()

    assert b.is_open()

def test_box_close():
    b= Box()
    b.close()

    assert not b.is_open()

def test_box_look():
    b = Box ()
    b.add("ceci")
    b.add("cela")

    b.open()
    assert b.action_look()=="la boite contient ceci, cela"

    b.close()
    assert b.action_look()=="la boite est fermée"

def test_thing_create():
    t = Thing(3)
    assert t.volume==3

def test_box_capacity():
    b= Box()

    assert b.capacity() is None

    b.set_capacity(5)
    assert b.capacity()==5

def test_has_room_for():
    b = Box()
    t = Thing(3)

    assert b.has_room_for(t)

    b.set_capacity(3)
    assert b.has_room_for(t)

    b.set_capacity(0)
    assert b.has_room_for(t)

def test_box_from_yaml():
    text= """
    - is_open: True
    capacity: 3
    - is_open: False
    capacity: 5
    """
    stream=io.StringIO(text)
    l=yaml.load(stream)

    b1=Box.from_yaml(l[0])
    b2=Box.from_yaml(l[1])

    assert b1.is_open()
    assert b1.capacity()==3
    assert not b2.id_open()
    assert b2.capacity()==5

def test_things_from_yaml():
    text= """
    - volume: 3
    - volume: 4
    name: bidule1
    """
    stream=io.StringIO(text)
    l=yaml.load(stream)

    t1=Things.from_yaml(l[0])
    t2=Things.from_yaml(l[1])

    assert t1.volume()
    assert t1.has_name("bidule")
    assert not t2.volume()
    assert t2.has_name("bidule1")

def test_things_from_yaml():
    text= """
    -type: Box
    capacity: 3
    is_open=true
    -type: Things
    volume: 3
    name: bidule
    """
    stream=io.StringIO(text)
    l=yaml.load(stream)

    l_obj=list_from_yaml(l)
    
    assert l_obj[0].capacity()==3
    assert l_obj[0].is_open()
    assert l_obj[1].volume()
    assert l_obj[1].capacity()==3