from quick_sort import quick_sort

def test_quick_sort():
    array_one = [5, 26, 9, 4, 3]
    actual = quick_sort(array_one, 0, (len(array_one)-1))
    expected = [3, 4, 5, 9, 26]
    assert actual == expected

def test_negative_quick_sort():
    array_two = [-1, 2, 7, -100, 42]
    actual = quick_sort(array_two, 0, (len(array_two)-1))
    expected = [-100, -1, 2, 7, 42]
    assert actual == expected

def test_duplicates_quick_sort():
    array_three = [4, 1, 2, 2, 4, -23, -100, 1]
    actual = quick_sort(array_three, 0, (len(array_three)-1))
    expected = [-100, -23, 1, 1, 2, 2, 4, 4]
    assert actual == expected
