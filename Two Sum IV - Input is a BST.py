https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root):
            if not root:
                return False
            
            diff = k - root.val
            if diff in seen:
                return True
            seen.add(root.val)
            
            return dfs(root.left) or dfs(root.right)
        
        seen = set()
        return dfs(root)
