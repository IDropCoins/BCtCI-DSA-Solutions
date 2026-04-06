"""DFS traversals: each function below answers the question in its docstring."""


class Node:
    """How do we store one binary-tree node (value and left and right children)?"""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: Node | None) -> None:
    """In what order do we visit nodes if we print the root before its subtrees (root, then left, then right)?"""
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


def inorder(root: Node | None) -> None:
    """In what order do we visit nodes if we print after the left subtree and before the right (left, root, right)?"""
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def postorder(root: Node | None) -> None:
    """In what order do we visit nodes if we print the root after both subtrees (left, right, root)?"""
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
