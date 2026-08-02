# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # returns height
        def dfs(node):
            if node:
                left_height = dfs(node.left)
                right_height = dfs(node.right)
            else:
                return 0
            # for each node, the diameter that passes through this node is left_height + right_height
            self.res = max(self.res, left_height + right_height)
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.res 


        


        
        
        
            