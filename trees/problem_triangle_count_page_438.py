class Node:
    def __init__(self,val,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right 

def triangle_count(root:Node,total_triangles=0):
    if not root:
        return 0

    left_side=triangle_count(root.left,0)
    right_side=triangle_count(root.right,0)
    lefts=0
    rights=0    

    def count_left(root):
        if not root:
            return
        nonlocal lefts
        lefts+=1
        count_left(root.left)
    def count_right(root):
        if not root:
            return
        nonlocal rights
        rights+=1
        count_right(root.right)
    count_left(root.left)
    count_right(root.right)
    total_triangles += left_side+right_side+min(lefts,rights)
    return total_triangles


if __name__ == "__main__":
    # Test 1:
    #         P
    #       /   \
    #      L     R
    #     /       \
    #   LL         RR
    # Expected (same-depth left-only vs right-only): 2
    root1 = Node("P", Node("L", Node("LL", None, None), None), Node("R", None, Node("RR", None, None)))

    # Test 2:
    #      A
    #     / \
    #    B   C
    # Expected: 1
    root2 = Node("A", Node("B", None, None), Node("C", None, None))

    tests = [
        ("Test 1", root1, 2),
        ("Test 2", root2, 1),
    ]

    for name, root, expected in tests:
        got = triangle_count(root, 0)
        print(f"{name}: got={got}, expected={expected}")
