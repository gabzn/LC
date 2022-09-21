Given the root of a binary tree, invert the tree, and return its root.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Bottom-up solution
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        root.left = right
        root.right = left
        return root
      
-------------------------------------------------------------------------------------------------------------------------------------------      
 class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Top-bottom solution
        previous_left = root.left
        root.left = root.right
        root.right = previous_left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
