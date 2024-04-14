https://leetcode.com/problems/sum-of-left-leaves/

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left_child):
            if not node.left and not node.right and is_left_child:
                return node.val
            
            res = 0
            if node.left:
                res += dfs(node.left, True)
            if node.right:
                res += dfs(node.right, False)
            
            return res
        
        return dfs(root, False)
