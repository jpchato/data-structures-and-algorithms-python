from depth_first import depth_first_search

def test_depth_first_search():
    test_graph = {
        'A' : ['B','S'],
        'B' : ['A'],
        'C' : ['D','E','F','S'],
        'D' : ['C'],
        'E' : ['C','H'],
        'F' : ['C','G'],
        'G' : ['F','S'],
        'H' : ['E','G'],
        'S' : ['A','C','G']
    }
    actual = depth_first_search(test_graph, 'A')
    expected = ['A', 'B', 'S', 'C', 'D', 'E', 'H', 'G', 'F']
    assert actual == expected

def test_depth_first_search_again():
    test_graph = {
    '1' : ['2','9'],
    '2' : ['1'],
    '3' : ['4','5','6','9'],
    '4' : ['3'],
    '5' : ['3','8'],
    '6' : ['3','7'],
    '7' : ['6','9'],
    '8' : ['5','7'],
    '9' : ['1','3','7']
    }   
    actual = depth_first_search(test_graph, '9')
    expected = ['9', '1', '2', '3', '4', '5', '8', '7', '6']
    assert actual == expected

def test_depth_first_search_lastly():
    test_graph = {
        'la' : ['seattle','santa cruz'],
        'seattle' : ['la'],
        'san francisco' : ['portland','phoenix','new york','santa cruz'],
        'portland' : ['san francisco'],
        'phoenix' : ['san francisco','austin'],
        'new york' : ['san francisco','orlando'],
        'orlando' : ['new york','santa cruz'],
        'austin' : ['phoenix','orlando'],
        'santa cruz' : ['la','san francisco','orlando']
    }
    actual = depth_first_search(test_graph, 'phoenix')
    expected = ['phoenix', 'san francisco', 'portland', 'new york', 'orlando', 'santa cruz', 'la', 'seattle', 'austin']
    assert actual == expected