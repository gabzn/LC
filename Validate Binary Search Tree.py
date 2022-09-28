https://leetcode.com/problems/validate-binary-search-tree/
  
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.validate(root, -math.inf, math.inf)
        
    # The boundaries will be adjusted depends on whether we are checking the left subtree or the right subtree. 
    def validate(self, root, min_boundary, max_boundary):
        if not root:
            return True
        
        # If we are checking the LEFT subtree of a root,
        #       Everything on the left has to be less than the root, the current root val becomes the max boundary for its left child.
        
        # If we are checking the RIGHT subtree of a root,
        #       Everything on the right has to be greater than the root, the current root val becomes the min boundary for its right child.
        if root.val <= min_boundary or root.val >= max_boundary:
            return False
        return self.validate(root.left, min_boundary, root.val) and self.validate(root.right, root.val, max_boundary)
