https://leetcode.com/problems/validate-binary-search-tree/
  
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, -math.inf, math.inf)
        
    # The boundaries will be adjusted depends on whether we are checking the left subtree or the right subtree. 
    # The reason we change only either the min or max is because we are checking a node from its parent perspective.
    # We are asking if the current node is less than or greater than its parent node.
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
      
--------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check_if_subtrees_are_valid(root, -math.inf, math.inf)
        
    def check_if_subtrees_are_valid(self, root, lower_bound, upper_bound):
        if not root:
            return True
        
        # Check if the current node val is within the bound.
        if not lower_bound < root.val < upper_bound:
            return False
        
        return self.check_if_subtrees_are_valid(root.left, lower_bound, root.val) and self.check_if_subtrees_are_valid(root.right, root.val, upper_bound)
