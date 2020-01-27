import unittest
import random

from node import BinaryTreeNode


def _make_children(node):
    node.left = BinaryTreeNode(random.randint(1, 10))
    node.right = BinaryTreeNode(random.randint(1, 10))
    return node


def make_binary_tree(depth):
    root = BinaryTreeNode(random.randint(1, 10))
    count = 0
    target_nodes = [root]

    while count <= depth:
        next_targets = []
        for node in [_make_children(node) for node in target_nodes]:
            next_targets.append(node.left)
            next_targets.append(node.right)
        target_nodes = next_targets
        count += 1
    return root


def make_subtree(root, depth):
    for _ in range(random.randint(1, depth)):
        direction = random.choice(["left", "right"])
        if direction == "left":
            root = root.left
        else:
            root = root.right

    return root


def is_subset_tree(t1, t2):
    """t2がt1のsubtreeであるかboolで返す"""
    if t1 == t2:
        return True

    targets = [t1.left, t1.right]

    while True:
        next_targets = []
        for node in targets:
            if t2 == node:
                return True

            if node.left:
                next_targets.append(node.left)

            if node.right:
                next_targets.append(node.right)

        if not next_targets:
            return False

        targets = next_targets


class TestSolution10(unittest.TestCase):
    def test_it(self):
        t1 = make_binary_tree(depth=10)
        t2 = make_subtree(t1, 10)
        assert is_subset_tree(t1, t2) is True

    def test_subtree_does_not_exist(self):
        t1 = make_binary_tree(depth=10)
        t2 = make_binary_tree(depth=3)
        assert is_subset_tree(t1, t2) is False


if __name__ == "__main__":
    unittest.main()
