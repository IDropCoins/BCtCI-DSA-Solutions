class Node:
    def __init__(self,val,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right

def invert_tree(root):
    if not root:
        return None
    left=invert_tree(root.left)
    right=invert_tree(root.right)
    root.left=right
    root.right=left
    return root


if __name__ == "__main__":
    # Test 1:
    #        4
    #      /   \
    #     2     7
    #    / \   / \
    #   1   3 6   9
    # After invert: 4's children swap; each subtree inverted.
    n1 = Node(1, None, None)
    n3 = Node(3, None, None)
    n6 = Node(6, None, None)
    n9 = Node(9, None, None)
    n2 = Node(2, n1, n3)
    n7 = Node(7, n6, n9)
    root1 = Node(4, n2, n7)
    invert_tree(root1)
    assert root1.left.val == 7 and root1.right.val == 2
    assert root1.left.left.val == 9 and root1.left.right.val == 6
    assert root1.right.left.val == 3 and root1.right.right.val == 1

    # Test 2: empty tree
    assert invert_tree(None) is None

    print("ok")
