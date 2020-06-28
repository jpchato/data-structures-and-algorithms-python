class Graph:
    
    def __init__(self):
        # leading underscore indicates that it is internal to the graph class
        self._adjacency_list = {}

    def add_vertex(self, value):
        v = Vertex(value)
        # vertex is the kye, and the value of the kye is a list
        self._adjacency_list[v] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=1):
        # both must be in graph, else error
        
        if start_vertex not in self._adjacency_list:
            raise KeyError('Start Vertex not in graph')

        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not in graph')

        edge = Edge(end_vertex, weight)

        # list of neighbors is start_vertex
        adjacencies = self._adjacency_list[start_vertex] 
        
        adjacencies.append(edge)

    def get_vertices(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self._adjacency_list.get(vertex, [])

    # this is our size function
    def __len__(self):
        return len(self._adjacency_list)

class Vertex:
    def __init__(self, value):
        # no leading underscore here, we want access to this value outside of the class
        self.value = value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight