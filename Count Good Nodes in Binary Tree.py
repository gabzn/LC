https://leetcode.com/problems/count-good-nodes-in-binary-tree/
  
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree. 
The problem statement is very confusing.

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 1
        
        # We want to keep track of the max we've seen so far so we can compare if the next node is a good node or not.
        # Starting from the topmost root node, the val of root will be the max we've seen so far.
        return 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val)
        
    def dfs(self, root, cur_max):
        if not root:
            return 0
        
        # If the current root is greater than the previous max, we know this current root is a good node.
        # So before we go into its children, we set the previous max to the value of this node.
        # To DENOTE the current node is a good node, return 1 + the # of good nodes on its left and right.
        if root.val >= cur_max:
            cur_max = root.val
            return 1 + self.dfs(root.left, cur_max) + self.dfs(root.right, cur_max)
        
        # This means the current node is NOT a good node, to DENOTE it's not a good node, simply return the # of good nodes on its left and right. 
        return self.dfs(root.left, cur_max) + self.dfs(root.right, cur_max)
