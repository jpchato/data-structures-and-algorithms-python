from hashtable import Hashtable

def test_add():
    ht = Hashtable()
    ht.size = 0
    ht.add("test_key", "test_value")
    ht.size = 1
    assert ht.buckets[ht.hash("test_key")].value == "test_value"

