https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
https://www.youtube.com/watch?v=CVLuS92R_os

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return node, -inf
            
            if not node.left and not node.right:
                return node, 1
            
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)
            
            if left_depth == right_depth:
                return node, left_depth + 1
            
            if left_depth > right_depth:
                return left_node, left_depth + 1
            
            return right_node, right_depth + 1
        
        return dfs(root)[0]
