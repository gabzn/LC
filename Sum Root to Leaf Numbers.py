https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sum_numbers(root, 0)
    
    def sum_numbers(self, node, cur_sum):
        if not node:
            return 0
        
        cur_sum *= 10
        cur_sum += node.val
        
        if not node.left and not node.right:
            return cur_sum
        
        return self.sum_numbers(node.left, cur_sum) + self.sum_numbers(node.right, cur_sum)
