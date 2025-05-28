from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(set)

    def add_edge(self, u, v):
        self.adj_list[u].add(v)
        self.adj_list[v].add(u)

    def neighbors(self, u):
        return self.adj_list.get(u, set())

    def has_node(self, u):
        return u in self.adj_list
