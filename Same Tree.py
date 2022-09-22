Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # First we check if nodes are Null/None
        # Three scenarios could happen:
        #    1: both are Null/None  ->  True
        #    2: Left is Null/None but Right isn't  ->  False
        #    3: Right is Null/None but Left isn't  ->  False
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        # If the Null/None checks are good, we then check the values.
        if p.val != q.val:
            return False
        
        # We go check the left subtrees and right subtrees.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
