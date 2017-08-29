from math import inf

class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}
        self.n_vertices = 0

    def add_vertex(self, name):
        if name not in self.adjacency_list:
            self.adjacency_list[name] = [] #implement as dict
            self.n_vertices += 1
            return name
        return False

    def add_edge(self, a, b, weight):
        if a not in self.adjacency_list or b not in self.adjacency_list:
            return False
        self.adjacency_list[a].append((b, weight))

    def print_adjacency_list(self):
        for vertex, list in self.adjacency_list.items():
            print(vertex, list)

    def bfs(self, start):
        if start not in self.adjacency_list:
            return False
        queue = [start]
        visited = []
        while len(queue) > 0:
            current = queue.pop(0)
            print(current)
            visited.append(current)
            #print(current)
            for vertex, weight in self.adjacency_list[current]:
                if vertex not in visited:
                    queue.append(vertex)
                #print(queue)

    def dfs(self, start):
        if start not in self.adjacency_list:
            return False
        stack = [start]
        visited = []
        while len(stack) > 0:
            current = stack.pop(0)
            print(current)
            visited.append(current)
            for vertex, weight in self.adjacency_list[current]:
                if vertex not in visited:
                    stack.insert(0,vertex)

    def _get_edges(self):
        edges = []
        for vertex, list in self.adjacency_list.items():
            for edge in list:
                edges.append((vertex, edge[0], edge[1]))
        return edges

    def bellman_ford(self, start):
        if start not in self.adjacency_list:
            return False

        #initialise graph
        distance = {}
        predecessor = {}

        for vertex, list in self.adjacency_list.items():
            distance[vertex] = float(inf)
            predecessor[vertex] = 0

        distance[start] = 0

        edges = self._get_edges()

        #relax edges repeatedly
        for i in range(self.n_vertices - 1):
            for u, v, w in edges:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u

        #check for negative-weight cycles
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                print("error: graph contains negative-weight cycle")

        return distance, predecessor

graph = DirectedGraph()
graph.add_vertex("a")
graph.add_vertex("b")
graph.add_vertex("c")
graph.add_vertex("d")
graph.add_vertex("e")
graph.add_vertex("f")

graph.add_edge("a", "c", 1)
graph.add_edge("a", "b", 2)
graph.add_edge("c", "d", 1)
graph.add_edge("b", "d", 1)
graph.add_edge("b", "e", 2)
graph.add_edge("e", "f", 3)

graph.print_adjacency_list()

graph.dfs("a")
graph.bfs("a")

distance, predecessor = graph.bellman_ford("a")
print(distance)
