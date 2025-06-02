from dataclasses import dataclass
import unittest

class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = BST(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = BST(key)
            else:
                self.right.insert(key)


@dataclass
class Lab8:
    def LCA(self, root: BST, key_1: int, key_2: int) -> int:
        current = root
        while current:
            if key_1 > current.key and key_2 > current.key:
                current = current.right
            elif key_1 < current.key and key_2 < current.key:
                current = current.left
            else:
                return current.key
        return -1

# Unit tests
class TestLab4(unittest.TestCase):
    def setUp(self):
        self.lab8 = Lab8()

    def test_lca(self):
        bst = BST(key=6)
        for key in [2, 8, 0, 4, 7, 9, 3, 5]:
            bst.insert(key)
        self.assertEqual(self.lab8.LCA(bst, 3, 5), 4)
        self.assertEqual(self.lab8.LCA(bst, 2, 8), 6)
        self.assertEqual(self.lab8.LCA(bst, 2, 4), 2)

    def test_lca_one(self):
        bst = BST(key=6)
        bst.insert(2)
        bst.insert(8)
        self.assertEqual(self.lab8.LCA(bst, 6, 6), 6)

    def test_lca_two(self):
        bst = BST(key=6)
        bst.insert(2)
        bst.insert(8)
        self.assertEqual(self.lab8.LCA(bst, 6, 2), 6)

    def test_lca_left(self):
        bst = BST(key=6)
        for key in [2, 8, 0, 4, 7, 9, 3, 5]:
            bst.insert(key)
        self.assertEqual(self.lab8.LCA(bst, 0, 5), 2)

    def test_lca_right(self):
        bst = BST(key=6)
        for key in [2, 8, 0, 4, 7, 9, 3, 5]:
            bst.insert(key)
        self.assertEqual(self.lab8.LCA(bst, 7, 9), 8)

    def test_lca_same_node(self):
        bst = BST(key=6)
        for key in [2, 8, 0, 4, 7, 9, 3, 5]:
            bst.insert(key)
        self.assertEqual(self.lab8.LCA(bst, 3, 3), 3)

    def test_lca_symmetric(self):
        bst = BST(key=6)
        for key in [2, 8, 0, 4, 7, 9, 3, 5]:
            bst.insert(key)
        self.assertEqual(self.lab8.LCA(bst, 0, 9), 6)

if __name__ == "__main__":
    unittest.main()

