from sys import setrecursionlimit
setrecursionlimit(1000000)

class Node:
    def __init__(self,item, pos_x):
        self.item = item
        self.pos_x = pos_x
        self.left = None
        self.right = None
        
def preorder(root):
    result = []
    result.append(root.item)
    if root.left:
        result += preorder(root.left)
    if root.right:
        result += preorder(root.right)
    return result

def postorder(root):
    result = []
    if root.left:
        result += postorder(root.left)
    if root.right:
        result += postorder(root.right)
    result.append(root.item)
    return result

def tree_make(root, node):
    
    if node.pos_x < root.pos_x:
        if not root.left:
            root.left = node
        else:
            tree_make(root.left, node)
    else:
        if not root.right:
            root.right = node
        else:
            tree_make(root.right, node)
            

def solution(nodeinfo):
    
    new_nodeinfo = []
    for idx, each in enumerate(nodeinfo):
        new_nodeinfo.append([idx+1,each[0], each[1]])
    
    new_nodeinfo.sort(key=lambda x:(-x[2],x[1]))
    
    root = Node(new_nodeinfo[0][0], new_nodeinfo[0][1])
    
    for each in new_nodeinfo[1:]:
        
        current = Node(each[0], each[1])
        tree_make(root,current)
        
    result1 = preorder(root)
    result2 = postorder(root)
    
    return [result1, result2]
    
    
    
    
    