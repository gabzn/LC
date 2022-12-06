https://leetcode.com/problems/path-sum-ii/
  
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:        
        paths = []
        self.find_paths(root, targetSum, paths, [])
        return paths
        
    def find_paths(self, root, targetSum, paths, current_path):
        if not root:
            return
        
        # Consider all paths
        current_path.append(root.val)
        
        # But we only add the current path to the list when the leaf.val == targetSum
        if not root.left and not root.right and root.val == targetSum:
            paths.append(current_path)
            return

        self.find_paths(root.left, targetSum-root.val, paths, current_path.copy())
        self.find_paths(root.right, targetSum-root.val, paths, current_path.copy())
        
        # No good and I don't know why
        # self.find_sum(root.left, targetSum-root.val, values, value)
        # self.find_sum(root.right, targetSum-root.val, values, value)
