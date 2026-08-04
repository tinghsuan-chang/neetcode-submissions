# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if root and self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    def isSameTree(self, p, q):
        if (p and q) and (p.val != q.val):
            return False
            
        if (p and not q) or (q and not p):
            return False
            
        if not p and not q:
            return True
            
        left_is_same = self.isSameTree(p.left, q.left)
        right_is_same = self.isSameTree(p.right, q.right)

        return left_is_same and right_is_same
        
            

