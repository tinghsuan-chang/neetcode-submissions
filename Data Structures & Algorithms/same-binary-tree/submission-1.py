# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and q) and (p.val != q.val): # different values
            return False
        
        if (p and not q) or (q and not p): # one node is empty but the other is not
            return False
        
        if not p and not q: # both nodes are empty
            return True
        
        # if p and q have the same value
        left_is_same = self.isSameTree(p.left, q.left)
        right_is_same = self.isSameTree(p.right, q.right)

        return left_is_same and right_is_same