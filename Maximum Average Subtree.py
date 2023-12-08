https://leetcode.com/problems/maximum-average-subtree/

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        answer = [0]
        self.dfs(root, answer)
        return answer[0]
    
    def dfs(self, root, answer):
        if not root.left and not root.right:
            answer[0] = max(answer[0], root.val)
            return root.val, 1

        total = root.val
        count = 1
        
        if root.left:
            left_sum, left_count = self.dfs(root.left, answer)
            total += left_sum
            count += left_count
        
        if root.right:
            right_sum, right_count = self.dfs(root.right, answer)
            total += right_sum
            count += right_count      
        
        answer[0] = max(answer[0], total / count)
        return total, count
