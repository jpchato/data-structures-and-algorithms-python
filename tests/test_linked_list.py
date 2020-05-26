# # from linked_list import Node, LinkedList

# def test_instance():
#     ll = LinkedList
#     assert ll.head == None

# def test_insert_empty():
#     ll = LinkedList()
#     ll.insert("apples")
#     assert ll.head.value == "apples"

# def test_insert_full():
#     ll = LinkedList()
#     ll.insert("apples")
#     ll.insert("bananas")
#     assert ll.head.value == "bananas"
#     assert ll.head.next.value == "appples"

# def test_str():
#     ll = LinkedList()
#     ll.insert("apples")
#     ll.insert("bananas")
#     assert str(ll) == "{ bananas } -> { apples } -> NULL"

# def test_kth_method():
#     ll = LinkedList()
#     ll.insert(1)
#     ll.append(2)
#     ll.append(3)
#     ll.append(4)
#     ll.append(5)

#     assert ll.kth_from_end(1) == 4
