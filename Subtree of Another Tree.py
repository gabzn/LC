https://leetcode.com/problems/subtree-of-another-tree/
  
  
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root and not subRoot) or (not subRoot):
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    
    def isSameTree(self, root, subRoot):
        if not root or not subRoot:
            return not root and not subRoot
        
        # If the Null/None checks are good, we then check the values.
        if root.val != subRoot.val:
            return False
        
        # We go check the left subtrees and right subtrees.
        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
