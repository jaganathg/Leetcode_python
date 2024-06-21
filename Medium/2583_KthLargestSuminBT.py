from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def kthLargest(self, root: Optional[TreeNode], k: int) -> int:
        
        queue = deque([root])
        res_list = list()
            
        while queue:
            level_size = len(queue)
            sum = 0
            for i in range(level_size):
                current_node = queue.popleft()
                sum += current_node.val
                
                if current_node.left:
                    queue.append(current_node.left)
                
                if current_node.right:
                    queue.append(current_node.right)
                    
            res_list.append(sum)
            
        if k > len(res_list):
            return -1
            
        res_list.sort(reverse=True)
        
        
        
        return res_list[k-1]
            
            
                    
           
        
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(8)
    root.right = TreeNode(9)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(6)
    k = 2
    print(Solution().kthLargest(root, k))  # Output: 4
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    k = 1
    print(Solution().kthLargest(root, k))  # Output: 4
    
    