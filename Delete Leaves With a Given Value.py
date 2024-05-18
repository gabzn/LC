https://leetcode.com/problems/delete-leaves-with-a-given-value/

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node.left and not node.right:
                if node.val == target:
                    return True
                return False
            
            is_left_deleted = False if node.left else True
            if node.left:
                is_left_deleted = dfs(node.left)
            if is_left_deleted:
                node.left = None
            
            is_right_deleted = False if node.right else True
            if node.right:
                is_right_deleted = dfs(node.right)
            if is_right_deleted:
                node.right = None
            
            if is_left_deleted and is_right_deleted and node.val == target:
                return True
            
            return False
        
        res = dfs(root)
        if res:
            return None
        return root
