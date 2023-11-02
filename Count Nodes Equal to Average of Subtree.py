https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node.left and not node.right:
                res[0] += 1
                return 1, node.val
            
            total_nodes = 1
            subtree_sum = node.val
            
            if node.left:
                nodes, sub_sum = dfs(node.left)
                
                total_nodes += nodes
                subtree_sum += sub_sum
            
            if node.right:
                nodes, sub_sum = dfs(node.right)
                
                total_nodes += nodes
                subtree_sum += sub_sum
            
            if subtree_sum // total_nodes == node.val:
                res[0] += 1
            
            return total_nodes, subtree_sum
        
        res = [0]
        dfs(root)
        return res[0]
