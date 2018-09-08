"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label

    """Trying to make this Graph class work..."""
class Graph:
    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            print('Cannot connect vertices that are not in graph')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, graph):
        def dfs_helper(v):
            history[v] = 'scheduled'
            nodes.append(v)
            for n in graph.vertices[v]:
                if history[n] == 'unvisited':
                    dfs_helper(n)
            history[v] = 'visited'
        nodes = []
        history = {}
        for key in graph.vertices.keys():
            history[key] = 'unvisited'
        for v in graph.vertices:
            if history[v] == 'unvisited':
                dfs_helper(v)
        return nodes
    

    def find_components(self):
        draw_components = []
        visited = set()
        for v in graph.vertices.keys():
            if v not in visited:
                component = self.dfs(graph)
                draw_components.append(component)
                for c in component:
                    visited.update(c)
        return draw_components
        # visited = set()
        # current_component = 0

        # for vertex in self.vertices:
        #     if vertex in visited:
        #         reachable = self.dfs(vertex)
        #         for other_vertex in reachable:
        #             other_vertex.component = current_component
        #         current_component += 1
        #         visited.update(reachable)
        # self.components = current_component

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
# print(graph.vertices)
print('DFS:  ' + str(graph.dfs(graph)))
print('CC: ' + str(graph.find_components()))
