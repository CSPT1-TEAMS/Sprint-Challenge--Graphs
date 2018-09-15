"""
Simple graph implementation compatible with BokehGraph class.
"""

from random import sample


class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        stack = [start]
        visited = set([start])

        while stack:
            current = stack.pop(-1)
            if current == target:
                break
            visited.add(current)
            stack.extend(self.vertices[current] - visited)
            visited.update(self.vertices[current])

        return visited

    def graph_rec(self, start, target=None):
        visited = set()

        def rec(s):
            visited.add(s)
            for v in self.vertices[s]:
                if v not in visited:
                    visited.add(v)
                    rec(v)
        rec(start)
        return visited

    def find_components(self):
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component

graph = Graph()
one = Vertex('1')
two = Vertex('2')
three = Vertex('3')
four = Vertex('4')
graph.add_vertex(one)
graph.add_vertex(two)
graph.add_vertex(three)
graph.add_vertex(four)
graph.add_edge(one, four)
graph.add_edge(three, one)
graph.add_edge(one, two)

print(graph.vertices)
print(graph.dfs(one))
print(graph.graph_rec(one))
# graph.dfs(one)
