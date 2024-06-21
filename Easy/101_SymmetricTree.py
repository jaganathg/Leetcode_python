
from typing import Optional

class TreeNode:
    def __init__ (self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    def isMirror(tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        return (tree1.val == tree2.val) and \
            isMirror(tree1.left, tree2.right) and \
            isMirror(tree1.right, tree2.left)
            
    return isMirror(root, root)


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)

# Non-Symmetric Tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)

print("\nSymmetric Tree")
print(isSymmetric(root1))
print(isSymmetric(root2))


# best implementation
#-----------------------------------------
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)