from merge_sort import merge_sort

def test_merge_sort():
    array_one = [5, 26, 9, 4, 3]
    actual = merge_sort(array_one)
    expected = [3, 4, 5, 9, 26]
    assert actual == expected

def test_negative_insertion_sort():
    array_two = [-1, 2, 7, -100, 42]
    actual = merge_sort(array_two)
    expected = [-100, -1, 2, 7, 42]
    assert actual == expected

def test_duplicates_insertion_sort():
    array_three = [4, 1, 2, 2, 4, -23, -100, 1]
    actual = merge_sort(array_three)
    expected = [-100, -23, 1, 1, 2, 2, 4, 4]
    assert actual == expected
