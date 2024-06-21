https://leetcode.com/problems/path-sum-iii/

class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        def dfs(node, current_sum):
            if not node:
                return
            
            current_sum += node.val
            if current_sum == target:
                answer[0] += 1
            
            diff = current_sum - target
            if diff in sum_count:
                answer[0] += sum_count[diff]
            
            sum_count[current_sum] += 1
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            sum_count[current_sum] -= 1
            
        sum_count = defaultdict(int)
        answer = [0]
        dfs(root, 0)
        return answer[0]
-------------------------------------------------------------------------------------
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
    
    def dfs(self, node, target):
        if not node:
            return 0
        
        if node.val == target:
            return 1 + self.dfs(node.left, target - node.val) + self.dfs(node.right, target - node.val)
        else:
            return self.dfs(node.left, target - node.val) + self.dfs(node.right, target - node.val)
