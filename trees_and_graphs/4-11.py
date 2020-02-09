import random
import unittest

from node import BinaryTreeNode


class BinarySearchTree:
    def __init__(self, values):
        self.root = self._make_binary_search_tree(sorted(values))

    def _make_binary_search_tree(self, values):
        if not values:
            return None

        center_idx = len(values) // 2
        root = BinaryTreeNode(values[center_idx], size=len(values))
        root.left = self._make_binary_search_tree(values[:center_idx])
        root.right = self._make_binary_search_tree(values[center_idx + 1:])
        return root

    def insert(self, val):
        node = self.root
        insert_node = BinaryTreeNode(val)
        while True:
            node.size += 1
            if insert_node.val > node.val:
                if not node.right:
                    node.right = insert_node
                    break

                # 現時点でのnodeとその右のnodeの間にinsert_nodeのvalが入りうる
                if node.val < insert_node.val < node.right.val:
                    # 右のnodeの左がNoneであれば、insert_nodeはそこにfitする（node.right.leftにinsert_nodeが入る）
                    if not node.right.left:
                        node = node.right
                        continue

                    # 右のnodeの左にnodeが存在していて、insert_node < node.right.left < node.rightの場合、引き続き探索が必要
                    if node.right.left.val > insert_node.val:
                        node = node.right
                        continue

                    # 右のnodeの左にnodeが存在していて、insert_node < node.right.left < node.rightの場合、node.right.leftの位置にinsert
                    node.right.size += 1
                    insert_node.size = node.right.left.size + 1
                    insert_node.left = node.right.left
                    node.right.left = insert_node
                    break

                node = node.right
            else:
                if not node.left:
                    node.left = insert_node
                    break

                # 現時点でのnodeとその左のnodeの間にinsert_nodeのvalが入りうる
                if node.left.val < insert_node.val < node.val:
                    # 左のnodeの右がNoneであれば、insert_nodeはそこにfitする（node.left.rightにinsert_nodeが入る）
                    if not node.left.right:
                        node = node.left
                        continue

                    # 左のnodeの右にnodeが存在していて、node.left < node.left.right < insert_nodeの場合、引き続き探索が必要
                    if node.left.right.val < insert_node.val:
                        node = node.left
                        continue

                    # 左のnodeの右にnodeが存在していて、node.left < insert_node < node.left.rightの場合、node.left.rightの位置にinsert
                    node.left.size += 1
                    insert_node.size = node.left.right.size + 1
                    insert_node.right = node.left.right
                    node.left.right = insert_node
                    break

                node = node.left

    def find(self, val):
        return self._find_node(val, self.root)

    def _find_node(self, val, node):
        if not node:
            return None

        if val == node.val:
            return node
        elif val > node.val:
            return self._find_node(val, node.right)
        else:
            return self._find_node(val, node.left)

    def delete(self, val):
        pass

    def get_random_node(self):
        return self._get_ith_node(random.choice([i for i in range(1, self.size + 1)]))

    def _get_ith_node(self, i):
        return


class TestSolution11(unittest.TestCase):
    def test_it(self):
        bst = BinarySearchTree(values=[i for i in range(1, 14, 2)])
        # rootに正しく値が入っている
        assert bst.root.val == 7

        # 左側が正しい
        assert bst.root.left.val == 3
        assert bst.root.left.left.val == 1
        assert bst.root.left.right.val == 5

        # 右側が正しい
        assert bst.root.right.val == 11
        assert bst.root.right.left.val == 9
        assert bst.root.right.right.val == 13

        # insertが正しく動くこと
        bst.insert(6)
        assert bst.root.left.val == 3
        assert bst.root.left.right.val == 5
        assert bst.root.left.right.right.val == 6

        bst.insert(4)
        assert bst.root.left.right.val == 4
        assert bst.root.left.right.right.val == 5
        assert bst.root.left.right.right.right.val == 6

        # findが正しく動くこと
        assert bst.find(4).val == 4
        assert bst.find(2) is None

        # deleteが正しく動くこと
        # bst.delete(4)
        # assert bst.root.left.right.val == 5
        # assert bst.root.left.right.right == 6

        # get_random_nodeが正しく動くこと
        # assert bst.get_random_node() in [1, 3, 5, 6, 7, 9, 11, 13]


if __name__ == "__main__":
    unittest.main()
