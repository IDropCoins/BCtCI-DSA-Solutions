def longest_aligned_chain(root):
    """Longest path of consecutive nodes whose values equal depth from the root."""
    res=0
    def visit(node,depth):
        """DFS: return aligned-chain length through this node; update outer best."""
        if not node:
            return 0
        left_chain=visit(node.left,depth+1)
        right_chain=visit(node.right,depth+1)
        current_chain=0
        if node.val==depth:
            current_chain=1+max(left_chain,right_chain)
            res=max(res,current_chain)
        return current_chain
    visit(root,0) #Trigger DFS, which updates the 'global'res
    return res