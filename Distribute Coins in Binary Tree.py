https://leetcode.com/problems/distribute-coins-in-binary-tree/

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            # Check how many coins left & right children can provide or need
            left_needed = dfs(node.left)
            right_needed = dfs(node.right)
            
            moves[0] += (abs(left_needed) + abs(right_needed))
            
            # If I have extra coins, I give them to my parent
            return left_needed + right_needed + (node.val - 1)
            
        moves = [0]
        dfs(root)
        return moves[0]
