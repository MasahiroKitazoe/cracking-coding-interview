import unittest

from node import BinaryTreeNode


def get_depth(node):
    depth = 0
    while node is not None:
        node = node.parent
        depth += 1
    return depth


def find_first_common_ancestor(one_node, the_other_node):
    if one_node.parent is None or the_other_node.parent is None:
        return None

    depth_diff = get_depth(one_node) - get_depth(the_other_node)
    upper_node = one_node if depth_diff < 0 else the_other_node
    deeper_node = one_node if depth_diff >= 0 else the_other_node

    for _ in range(abs(depth_diff)):
        deeper_node = deeper_node.parent

    while upper_node != deeper_node:
        upper_node = upper_node.parent
        deeper_node = deeper_node.parent

    return upper_node


class TestSolution7(unittest.TestCase):
    def setup_binary_tree(self):
        nodes = [BinaryTreeNode(val=i) for i in range(10)]
        nodes[0].left = nodes[1]
        nodes[0].right = nodes[2]
        nodes[1].left = nodes[3]
        nodes[1].right = nodes[4]
        nodes[1].parent = nodes[0]
        nodes[2].left = nodes[5]
        nodes[2].right = nodes[6]
        nodes[2].parent = nodes[0]
        nodes[3].left = nodes[7]
        nodes[3].right = nodes[8]
        nodes[3].parent = nodes[1]
        nodes[4].left = nodes[9]
        nodes[4].parent = nodes[1]
        nodes[5].parent = nodes[2]
        nodes[6].parent = nodes[2]
        nodes[7].parent = nodes[3]
        nodes[8].parent = nodes[3]
        nodes[9].parent = nodes[4]

        return nodes

    def test_it(self):
        tree_nodes = self.setup_binary_tree()
        common_ancestor = find_first_common_ancestor(tree_nodes[-1], tree_nodes[-2])
        assert common_ancestor == tree_nodes[1]

if __name__ == "__main__":
    unittest.main()
