# class for creating binary tree (that has key(node), left(node), right(node)) 
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    
    return node

def tree_to_tuple(node):
    if isinstance(node, TreeNode):
        if node.left is None and node.right is None:
            return node.key
        
        return (
            tree_to_tuple(node.left),
            node.key,
            tree_to_tuple(node.right)
        )
    else:
        return node

if __name__ == '__main__':    
    tree_tuple_str = input()
    tree_tuple = eval(tree_tuple_str)
    tree2 = parse_tuple(tree_tuple)
    print(tree_to_tuple(tree2))
