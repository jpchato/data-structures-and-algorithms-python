# reference: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
# reference: https://www.youtube.com/watch?v=Y40bRyPQQr0
# reference: https://stackoverflow.com/questions/43430309/depth-first-search-dfs-code-in-python

def depth_first_search(graph, start_vertex):
    # The set() builtin creates a set in Python.
    # A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements
    visited = set()
    traversal = []
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            # The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
            # The reversed() function returns the reversed iterator of the given sequence.
            stack.extend(reversed(graph[vertex]))   # add vertex in the same order as visited
    return traversal

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

print(depth_first_search(test_graph, 'phoenix'))