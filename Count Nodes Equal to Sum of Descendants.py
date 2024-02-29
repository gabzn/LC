https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left + right == node.val:
                res[0] += 1
            
            return node.val + left + right
            
        res = [0]
        dfs(root)
        return res[0]
