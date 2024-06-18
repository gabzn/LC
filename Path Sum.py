https://leetcode.com/problems/path-sum/

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, target_sum)]
        
        while stack:
            node, target = stack.pop()
            new_target = target - node.val
            if not node.left and not node.right and new_target == 0:
                return True
            
            if node.left:
                stack.append((node.left, new_target))
            if node.right:
                stack.append((node.right, new_target))
        
        return False
-----------------------------------------------------------------------------------------
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
