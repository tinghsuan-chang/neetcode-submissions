"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        copied = {} # OG node : copied node

        copied[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in copied:
                    copied[nei] = Node(nei.val)
                    q.append(nei)
                copied[cur].neighbors.append(copied[nei])
        
        return copied[node]

# Time: O(V+E), V: number of vertices, E: number of edges
# Space: O(V)