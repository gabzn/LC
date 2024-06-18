https://leetcode.com/problems/path-sum-ii/

class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
        if not root:
            return []
        
        return self.find_paths(root, target_sum, [], [])
        
    def find_paths(self, node, target_sum, current, res):
        current.append(node.val)
        new_target = target_sum - node.val

        if not node.left and not node.right and new_target == 0:
            res.append(current.copy())
            return res

        if node.left:
            res = self.find_paths(node.left, new_target, current, res)
            current.pop()

        if node.right:
            res = self.find_paths(node.right, new_target, current, res)
            current.pop()

        return res
----------------------------------------------------------------------------------------------------
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        return self.backtrack(root, targetSum, [], [])
    
    def backtrack(self, root, target, current, res):
        current.append(root.val)

        if not root.left and not root.right and target - root.val == 0:
            res.append(current.copy())
            return res
        
        if root.left:
            res = self.backtrack(root.left, target - root.val, current, res)
            current.pop()
            
        if root.right:
            res = self.backtrack(root.right, target - root.val, current, res)
            current.pop()
            
        return res
------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
