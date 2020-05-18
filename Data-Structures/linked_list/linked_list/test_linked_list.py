from linked_list import LinkedList

def test_instance():
    ll = LinkedList
    assert ll.head == None

def test_insert_empty():
    ll = LinkedList()
    ll.insert("apples")
    assert ll.head.value == "apples"

def test_insert_full():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    assert ll.head.value == "bananas"
    assert ll.head.next.value == "appples"

def test_str():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    assert str(ll) == "{ bananas } -> { apples } -> NULL"
