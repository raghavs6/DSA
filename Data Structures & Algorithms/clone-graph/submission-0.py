"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
         visited = {}
         def dfs(root):
            if root is None:
                return None
            cur = root
            if cur in visited:
                return visited[cur]
            newNode = Node(cur.val)

            visited[cur] = newNode
            for n in cur.neighbors:
                newNode.neighbors.append(dfs(n))
            
            return newNode

         return dfs(node)