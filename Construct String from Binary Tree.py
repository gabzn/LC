https://leetcode.com/problems/construct-string-from-binary-tree/

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        self.find_str(root, res)
        return ''.join(res)
    
    def find_str(self, root, res):
        if not root:
            return
        
        res.append(str(root.val))
        if not root.left and not root.right:
            return
        
        # Traverse left no matter what
        res.append('(')
        self.find_str(root.left, res)
        res.append(')')
        
        # Only traverse right when there's a value
        if root.right:
            res.append('(')
            self.find_str(root.right, res)
            res.append(')')
