import unittest

from graph import Graph, Node


def depth_first_search(root, target_node):
    if root == target_node:
        return True

    root.visited = True

    for node in root.children:
        if depth_first_search(node, target_node):
            return True

    return False


def is_route_exists(node, node_another):
    return depth_first_search(node, node_another) or depth_first_search(node_another, node)


class TestCase(unittest.TestCase):
    # UNDIRECTED_GRAPH_PATHS = {
    #     0: [1, 4, 5],
    #     1: [3, 4],
    #     2: [1],
    #     3: [2, 4],
    #     4: [],
    #     5: []
    # }
    DIRECTED_GRAPH_PATHS = {
        0: [1, 4, 5],
        1: [3, 4],
        2: [],
        3: [2],
        4: [],
        5: []
    }
    DIRECTED_LOOP_GRAPH_PATH = {
        0: [1, 4, 5],
        1: [3, 4],
        2: [],
        3: [0, 2],
        4: [],
        5: []
    }

    def setUp(self):
        nodes = {val: Node(val, []) for val in range(6)}
        for node_val, node in nodes.items():
            for node_key in self.DIRECTED_GRAPH_PATHS[node_val]:
                nodes[node_val].children.append(nodes[node_key])
        return Graph(sorted(nodes.values(), key=lambda x: x.val))

    def setUpLoop(self):
        nodes = {val: Node(val, []) for val in range(6)}
        for node_val, node in nodes.items():
            for node_key in self.DIRECTED_LOOP_GRAPH_PATHS[node_val]:
                nodes[node_val].children.append(nodes[node_key])
        return Graph(sorted(nodes.values(), key=lambda x: x.val))

    def test_path_found(self):
        graph = self.setUp()
        res = is_route_exists(graph.nodes[0], graph.nodes[2])
        assert res is True

    def test_path_not_found(self):
        graph = self.setUp()
        res = is_route_exists(graph.nodes[2], graph.nodes[5])
        assert res is False

    def test_loop_path(self):
        graph = self.setUpLoop()
        res = is_route_exists(graph.nodes[0], graph.nodes[2])
        assert res is True


if __name__ == "__main__":
    unittest.main()
