from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        oldNew = {}
        
        
        def dfs(node):
            if node in oldNew:
                return oldNew[node]
            copy = Node(node.val)
            oldNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        return dfs(node) if node else None


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    s = Solution()
    print(s.cloneGraph(node1))  # Output: [[2,4],[1,3],[2,4],[1,3]]
            