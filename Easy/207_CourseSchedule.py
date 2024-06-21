from typing import List

def canFinish( numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Create a graph using adjacency list
    graph = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    # Create a visited set to keep track of visited nodes
    visited = set()
    
    # Create a recursion stack to keep track of nodes in the current path
    recStack = set()
    
    # Helper function to check if there is a cycle in the graph
    def dfs(node):
        if node in recStack:
            return False
        if node in visited:
            return True
        
        visited.add(node)
        recStack.add(node)
        
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        
        recStack.remove(node)
        return True
    
    # Check if there is a cycle in the graph
    for node in range(numCourses):
        if not dfs(node):
            return False
    
    return True

if __name__ == "__main__":
    # Example 1
    numCourses = 2
    prerequisites = [[1, 0]]
    print(canFinish(numCourses, prerequisites))  # Output: True
    
    # Example 2
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(canFinish(numCourses, prerequisites))  # Output: False