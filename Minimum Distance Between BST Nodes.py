https://leetcode.com/problems/minimum-distance-between-bst-nodes/
  
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        preorder = []
        self.get_preorder(root, preorder)
        
        min_difference = math.inf
        for i in range(1, len(preorder)):
            min_difference = min(min_difference, preorder[i] - preorder[i - 1])
        
        return min_difference
    
    def get_preorder(self, root, preorder):
        if not root:
            return
        
        self.get_preorder(root.left, preorder)
        preorder.append(root.val)
        self.get_preorder(root.right, preorder)    
