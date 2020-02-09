import unittest

from graph import GraphNode, Graph


def create_graph(projects, dependencies):
    nodes = {}
    for project_val in projects:
        node = GraphNode(project_val)
        nodes[node.val] = node

    for node_val_parent, node_val_child in dependencies:
        node_child = nodes.get(node_val_child)
        nodes[node_val_parent].next.append(nodes[node_val_child])

    return Graph(nodes.values())


def find_compilable_order(nodes, compiled_nodes):
    # 全nodeがcompileされたら、成功
    if not nodes:
        return [node.val for node in compiled_nodes]

    depended_nodes = set()
    for node in nodes:
        for next_node in node.next:
            depended_nodes.add(next_node)
    non_depended_nodes = [node for node in nodes if node not in depended_nodes]

    # compileされていないnodeがあり、なおかつこれ以上compileできない場合はエラー
    if not non_depended_nodes:
        return "error"

    return find_compilable_order(list(depended_nodes), compiled_nodes + list(non_depended_nodes))


def find_build_order(projects, dependencies):
    graph = create_graph(projects, dependencies)
    return find_compilable_order(graph.nodes, [])


class TestSolution7(unittest.TestCase):
    def test_it(self):
        res = find_build_order(
            projects=["a", "b", "c", "d", "e", "f"],
            dependencies=[("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
        )
        assert res == ["e", "f", "a", "b", "d", "c"]

if __name__ == "__main__":
    unittest.main()
