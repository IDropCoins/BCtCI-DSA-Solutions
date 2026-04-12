"""Tree with parent pointers: each function below answers the question in its docstring."""


class Node:
    """How do we store a node when we must walk upward (id, parent, left, right)?"""

    def __init__(self, id, parent=None, left=None, right=None):
        self.id = id
        self.parent = parent
        self.left = left
        self.right = right


def is_root(node: Node | None) -> bool:
    """Is this node the root of its tree (it has no parent)?"""
    if not node:
        return False
    return node.parent is None


def find_ancestors_id(node: Node | None) -> list[int]:
    """What are the ids of this node's ancestors, from its parent up to the root?"""
    list1: list[int] = []
    if not node:
        return list1
    while node.parent:
        list1.append(node.parent.id)
        node = node.parent
    return list1


def find_lca(node1: Node | None, node2: Node | None) -> int | None:
    """What is the id of the deepest common proper ancestor of these two nodes (strict: not counting a node as its own ancestor)?"""
    if not node1 or not node2:
        return None
    list1 = find_ancestors_id(node1)
    list2 = find_ancestors_id(node2)
    ids2 = set(list2)
    for aid in list1:
        if aid in ids2:
            return aid
    return None


def find_lca_inclusive(node1: Node | None, node2: Node | None) -> int | None:
    """What is the id of the lowest common ancestor of these two nodes (non-strict: a node is an ancestor of itself)?"""
    if not node1 or not node2:
        return None
    if node1 is node2 or node1.id == node2.id:
        return node1.id
    list1 = find_ancestors_id(node1)
    list2 = find_ancestors_id(node2)
    ids1 = set(list1)
    ids2 = set(list2)
    if node1.id in ids2:
        return node1.id
    if node2.id in ids1:
        return node2.id
    for aid in list1:
        if aid in ids2:
            return aid
    return None

def distance_between_nodes(node1: Node | None, node2: Node | None) -> int | None:
    """How many edges are on the path between these two nodes (0 if the same node)?"""
    if not node1 or not node2:
        return None
    if node1 is node2 or node1.id == node2.id:
        return 0
    list1 = find_ancestors_id(node1)
    list2 = find_ancestors_id(node2)
    ids1 = set(list1)
    ids2 = set(list2)
    if node1.id in ids2:
        return list2.index(node1.id) + 1
    if node2.id in ids1:
        return list1.index(node2.id) + 1
    for aid in list1:
        if aid in ids2:
            return list1.index(aid) + list2.index(aid) + 2
    return None