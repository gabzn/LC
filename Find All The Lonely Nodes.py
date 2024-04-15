https://leetcode.com/problems/find-all-the-lonely-nodes/

class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, is_lonely):
            if not node:
                return
            if is_lonely:
                res.append(node.val)
            
            if node.left and not node.right:
                dfs(node.left, True)
            if node.right and not node.left:
                dfs(node.right, True)
            if node.left and node.right:
                dfs(node.left, False)
                dfs(node.right, False)
        
        res = []
        dfs(root, False)
        return res
