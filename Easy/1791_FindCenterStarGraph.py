
def find_center(edges: list[list[int]]) -> int:
    return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


if __name__=='__main__':
    print(find_center([[1,2],[2,3],[4,2]]))  # Output: 2
    print(find_center([[1,2],[5,1],[1,3],[1,4]]))  # Output: 1
  