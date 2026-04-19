class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def tree_layout(root):
    coordinates_and_nodes={}
    def visit(node,r,c):
        nonlocal coordinates_and_nodes
        if not node:
            return
        if (r,c) not in coordinates_and_nodes:
            coordinates_and_nodes[(r,c)]=1
        else:
            coordinates_and_nodes[(r,c)]+=1
        if node.left:
            visit(node.left,r+1,c)
        if node.right:
            visit(node.right,r,c+1)

    visit(root,0,0)
    max1=0
    for a,b in coordinates_and_nodes:
        if coordinates_and_nodes[(a,b)]>max1:
            max1=coordinates_and_nodes[(a,b)]
    return max1


if __name__ == "__main__":
    # Problem 35.4: return maximum number of nodes stacked
    # at a single (r, c) coordinate.
    cases = [
        ("empty tree", None, 0),
        ("single node", Node("A"), 1),
        ("root with two children", Node("A", Node("B"), Node("C")), 1),
        ("left chain of three", Node("A", Node("B", Node("C"))), 1),
        (
            "right chain of three",
            Node("A", None, Node("B", None, Node("C"))),
            1,
        ),
        ("only left child of root", Node("A", Node("B")), 1),
        ("only right child of root", Node("A", None, Node("B")), 1),
        (
            "B.right and C.left both at (1,1) => max stacked 2",
            Node("A", Node("B", None, Node("D")), Node("C", Node("E"))),
            2,
        ),
        (
            "same overlap example (duplicate shape check)",
            Node("A", Node("B", None, Node("D")), Node("C", Node("E"))),
            2,
        ),
        (
            "no overlaps anywhere in a left chain => max stacked = 1",
            Node("A", Node("B", Node("C", Node("D")))),
            1,
        ),
        (
            "three nodes stacked at (1,1) => max stacked = 3",
            Node(
                "A",
                Node(
                    "B",
                    Node("D", None, Node("G")),
                    Node("E", Node("H"), None),
                ),
                Node("C", Node("F", Node("I"), None), None),
            ),
            3,
        ),
        (
            "balanced perfect tree of height 2 => max stacked = 2",
            Node(
                "A",
                Node("B", Node("D"), Node("E")),
                Node("C", Node("F"), Node("G")),
            ),
            2,
        ),
    ]

    passed = failed = errors = 0
    for name, root, expected in cases:
        try:
            got = tree_layout(root)
            if got == expected:
                print(f"{name}: got={got}, expected={expected} -> OK")
                passed += 1
            else:
                print(f"{name}: got={got}, expected={expected} -> FAIL")
                failed += 1
        except Exception as e:
            print(f"{name}: ERROR ({type(e).__name__}: {e})")
            errors += 1

    print(f"--- summary: OK={passed}, FAIL={failed}, ERROR={errors}")
