def hidden_message(node):
    if not node:
        return ""
    
    left=hidden_message(node.left)
    right=hidden_message(node.right)
    if node.val[0]=="i":
        sentence=left+node.val[1]+right
    elif node.val[0]=="a":
        sentence=left+right+node.val[1]
    elif node.val[0]=="b":
        sentence=node.val[1]+left+right
    else:
        sentence=""
    return sentence
