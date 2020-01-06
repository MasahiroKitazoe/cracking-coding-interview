import unittest

from graph import BinaryNode


def create_binary_search_tree(values):
    if not values:
        return None

    half_idx = len(values) // 2 if len(values) != 2 else 0
    root = BinaryNode(values[half_idx])
    root.left = create_binary_search_tree(values[:half_idx])
    root.right = create_binary_search_tree(values[half_idx+1:])

    return root


class TestCase(unittest.TestCase):
    def test_it(self):
        res = create_binary_search_tree([2,4,6,8,10,20])
        assert res.left.val == 4
        assert res.left.left.val == 2
        assert res.left.right.val == 6
        assert res.right.val == 10
        assert res.right.left is None
        assert res.right.right.val == 20


if __name__ == "__main__":
    unittest.main()
