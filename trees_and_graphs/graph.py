class GraphNode:
    def __init__(self, val, next_nodes=None):
        self.val = val
        self.next = list(next_nodes) if next_nodes else []

    def __repr__(self):
        return f"GraphNode {self.val}"


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
