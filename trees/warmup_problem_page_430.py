"""Binary tree warmup: each function below answers the question in its docstring."""


class Node:
    """How do we store one binary-tree node (its value and its left and right children)?"""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def is_node(node: Node | None) -> bool:
    """Is this node a leaf (no children)?"""
    if not node:
        return False
    if node.left or node.right:
        return False
    else:
        return True


def children_nodes(node: Node | None) -> list:
    """What are the values of this node's immediate children (left, then right)?"""
    list1 = []
    if not node:
        return list1
    if node.left:
        list1.append(node.left.val)
    if node.right:
        list1.append(node.right.val)
    return list1


def grandchildren_nodes(node: Node | None) -> list:
    """What are the values of this node's grandchildren?"""
    list1 = []
    if not node:
        return list1
    for i in [node.left, node.right]:
        if i:
            if i.left:
                list1.append(i.left.val)
            if i.right:
                list1.append(i.right.val)
    return list1


def size_subtree(node: Node | None) -> int:
    """How many nodes are in the subtree rooted at this node?"""
    if not node:
        return 0
    return size_subtree(node.left) + size_subtree(node.right) + 1


def height_subtree(node: Node | None) -> int:
    """What is the height of the subtree rooted at this node?"""
    if not node:
        return 0
    return max(height_subtree(node.left), height_subtree(node.right)) + 1
