https://leetcode.com/problems/binary-tree-postorder-traversal/
  
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorder(root, [])
    
    def postorder(self, root, res):
        if not root:
            return res
        
        res = self.postorder(root.left, res)
        res = self.postorder(root.right, res)
        res.append(root.val)
        return res
