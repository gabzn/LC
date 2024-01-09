https://leetcode.com/problems/leaf-similar-trees/

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leaves):
            if not node.left and not node.right:
                leaves.append(node.val)
                return leaves
                
            if node.left:
                leaves = dfs(node.left, leaves)
            
            if node.right:
                leaves = dfs(node.right, leaves)
            
            return leaves
        
        return dfs(root1, []) == dfs(root2, [])
