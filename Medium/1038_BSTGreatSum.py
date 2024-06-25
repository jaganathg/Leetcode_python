

class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None
        
def bstToGst(root: TreeNode) -> TreeNode:
    total = 0
    
    def convert(node: TreeNode):
        nonlocal total
        if not node:
            return
        convert(node.right)
        total += node.val
        node.val = total
        convert(node.left)
        
    convert(root)
    return root


if __name__=="__main__":
    
    root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    print(bstToGst(root))