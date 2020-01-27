import unittest

from node import BinaryTreeNode


def find_all_sequences(node):
    sequences = []

    if not node:
        return sequences

    sequences.append(node.val)
    sequences_from_left = find_all_sequences(node.left)
    sequences_from_right = find_all_sequences(node.right)


class TestSolution7(unittest.TestCase):
    def _coonect_nodes(self, top, left, right):
        top.left = left
        top.right = right
        return top, left, right

    def setup_binary_search_tree(self):
        root = BinaryTreeNode(20)
        root, left, right = self._coonect_nodes(root, BinaryTreeNode(15), BinaryTreeNode(25))
        self._connect_nodes(left, BinaryTreeNode(10), BinaryTreeNode(18))
        self._connect_nodes(right, None, BinaryTreeNode(25))
        return root

    def test_it(self):
        root_node = self.setup_binary_search_tree()


if __name__ == "__main__":
    unittest.main()
