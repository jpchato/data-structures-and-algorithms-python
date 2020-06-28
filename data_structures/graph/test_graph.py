import pytest

from graph import Graph, Vertex

# 1. Node(vertex) can be successfully added to the graph
def test_add_vertex():
    g = Graph()
    expected = 'spam'
    vertex = g.add_vertex('spam')
    actual = vertex.value
    assert actual == expected

# 2. An edge can be successfully added to the graph
def test_add_edge():

    g = Graph()

    apples = g.add_vertex('apples')
    bananas = g.add_vertex('bananas')
    g.add_edge(apples, bananas)

    assert True, ('will be fully exercised in get_neighbors tests')

def test_add_edge_interloper():
    g = Graph()

    insider = g.add_vertex('insider')
    outsider = Vertex('outsider')
    
    with pytest.raises(KeyError):
        g.add_edge(outsider, insider)

# 3. A collection of all nodes can be properly retrieved from the graph
def test_get_vertices():
    # returns a collection of all vertices
    g = Graph()
    apples = g.add_vertex('apples')
    bananas = g.add_vertex('bananas')

    actual = g.get_vertices()

    assert len(actual) ==  2

# 4. All appropriate neighbors can be retrieved from the graph
def test_get_neighbors():
    
    g = Graph()
    
    apple = g.add_vertex('apple')
    
    banana = g.add_vertex('banana')
    
    g.add_edge(apple, banana)

    neighbors = g.get_neighbors(apple)

    assert len(neighbors) == 1

    print('neighbors', neighbors)

    neighbor = neighbors[0]

    assert neighbors[0].vertex.value == 'banana'

    assert neighbor.weight == 1

# 6. The proper size is returned, representing the number of nodes in the graph
def test_get_size():
    g = Graph()
    
    apple = g.add_vertex('apple')
    
    banana = g.add_vertex('banana')

    assert len(g) == 2

# 8. An empty graph properly returns null
def test_size_empty():

    g = Graph()

    expected = 0

    actual = len(g)

    assert actual == expected