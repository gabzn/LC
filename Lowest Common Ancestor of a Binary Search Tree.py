https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
  
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 
  “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
  (where we allow a node to be a descendant of itself).”
  
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If either p or q is root, return root
        if root.val == p.val or root.val == q.val:
            return root
        
        # If both are the direct children of a root node, return the current root node
#         if (root.left == p.val and root.right == q.val) or (root.left == q.val and root.right == p.val):
#             return root
        
        # If both are not in the same subtree and have different parents, return the current root node
        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
            return root
        
        # If both are in the same subtree but have different parents, return their shared root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
