from collections import deque

class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None
        
def balanceBST(root: TreeNode) -> TreeNode:
    def inorder(node: TreeNode):
        return inorder(node.left) + [node] + inorder(node.right) if node else []
    
    def buildTree(nodes: TreeNode):
        if not nodes:
            return None
        mid = len(nodes) // 2
        root = nodes[mid]
        root.left = buildTree(nodes[:mid])
        root.right = buildTree(nodes[mid+1:])
        return root
    
    return buildTree(inorder(root))

def print_bst(root: TreeNode) -> list[int]:
    if not root:
        return []
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] == None:
        result.pop()
    return result
    


if __name__=='__main__':
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.right = TreeNode(3)
    root1.right.right.right = TreeNode(4)
    
    balanced_root1 = balanceBST(root1)
    print(print_bst(balanced_root1))  # Output: [2, 1, 3, None, None, None, 4]

    # Example 2
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)

    balanced_root2 = balanceBST(root2)
    print(print_bst(balanced_root2))  # Output: [2, 1, 3]

        
        