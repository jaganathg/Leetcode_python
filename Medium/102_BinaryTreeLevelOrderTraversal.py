from typing import Optional, List
from collections import deque

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
       
        
        while queue:
            level = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
            
        return res
    
    
if __name__ == "__main__":
    s = solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.levelOrder(root))  # Output: [[3],[9,20],[15,7]]
        
        