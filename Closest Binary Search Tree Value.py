https://leetcode.com/problems/closest-binary-search-tree-value/
  
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
                           
            if root.val > target:
                root = root.left
            else:
                root = root.right
                
        return res
