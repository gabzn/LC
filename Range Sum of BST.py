https://leetcode.com/problems/range-sum-of-bst/
  
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        if low <= root.val <= high:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        
        return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
