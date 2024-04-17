https://leetcode.com/problems/smallest-string-starting-from-leaf/

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, current_str):
            if not node.left and not node.right:
                current_str = chr(ord('a') + node.val) + current_str
                
                if not res[0] or res[0] > current_str:
                    res[0] = current_str                    
            
            current_str = chr(ord('a') + node.val) + current_str
            if node.left:
                dfs(node.left, current_str)
            if node.right:
                dfs(node.right, current_str)
        
        res = [""]
        dfs(root, "")
        return res[0]
