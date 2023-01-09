https://leetcode.com/problems/binary-tree-preorder-traversal/
  
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        self.preorder(root, order)
        return order
    
    def preorder(self, root, order):
        if not root:
            return
        
        order.append(root.val)
        self.preorder(root.left, order)
        self.preorder(root.right, order)
        return 
