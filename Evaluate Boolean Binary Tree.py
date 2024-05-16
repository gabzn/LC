https://leetcode.com/problems/evaluate-boolean-binary-tree/

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node.left and not node.right:
                return node.val
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            res = None
            if node.val == 2:
                res = left or right
            else:
                res = left and right
            return res
        
        return dfs(root)
