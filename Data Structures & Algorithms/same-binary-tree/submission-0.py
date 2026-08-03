# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(node1, node2):
            if self.res is False:
                return

            if (node1 and node2) and (node1.val != node2.val):
                self.res = False
            elif node1 and node2: # node1 and node2 have same value
                dfs(node1.left, node2.left)
                dfs(node1.right, node2.right)
            elif node1 or node2: # one node is empty and the other is not
                self.res = False
            else: # node1 and node2 are both empty 
                return
        
        dfs(p, q)
        return self.res
            
        
                