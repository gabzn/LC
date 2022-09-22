https://leetcode.com/problems/balanced-binary-tree/
  
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
    
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # h doesn't BEAR any meaning for the topmost root node
        h, is_balanced = self.dfs(root)
        return is_balanced
        
    # For the entire tree to be balanced in the root node perspective, we need to know
    #       If its left subtree and right subtree are balanced
    #       If the heights of 2 subtrees are off by more than 1
    def dfs(self, root):
        if not root:
            return 0, True
        
        left_height, is_left_balanced = self.dfs(root.left)
        right_height, is_right_balanced = self.dfs(root.right)
        
        # max_subtree_height doesn't BEAR any meaning for the topmost root node
        # It's only used for the subtrees to report to their root the max height between them. 
        max_subtree_height = max(left_height, right_height) + 1
        are_both_sides_balanced = is_left_balanced and is_right_balanced and abs(left_height - right_height) <= 1
        
        return max_subtree_height, are_both_sides_balanced
