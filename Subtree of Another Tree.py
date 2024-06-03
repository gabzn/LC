https://leetcode.com/problems/subtree-of-another-tree/

class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.is_same_tree(root, sub_root):
            return True
        return self.isSubtree(root.left, sub_root) or self.isSubtree(root.right, sub_root)
    
    def is_same_tree(self, root, sub_root):
        if not root and not sub_root:
            return True
        if not root or not sub_root:
            return False
        if root.val != sub_root.val:
            return False
        return self.is_same_tree(root.left, sub_root.left) and self.is_same_tree(root.right, sub_root.right)
