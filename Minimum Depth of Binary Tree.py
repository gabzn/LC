https://leetcode.com/problems/minimum-depth-of-binary-tree/

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.find_min_depth(root)
        
    def find_min_depth(self, node):
        if not node:
            return 0
        
        # If both children are null, the current node is a leaf node
        if not node.left and not node.right:
            return 1
        
        # If one of them exists, keep going
        if not node.left:
            return 1 + self.find_min_depth(node.right)
        if not node.right:
            return 1 + self.find_min_depth(node.left)
        
        # If both of them exist, pick the one that returns the smaller ans
        return 1 + min(self.find_min_depth(node.left), self.find_min_depth(node.right))
