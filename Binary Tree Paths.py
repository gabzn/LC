Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
  
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root.left and not root.right:
            return [f'{root.val}']
        
        path, paths = '', []
        self.dfs(root, paths, path)
        return paths
    
    def dfs(self, root, paths, path):
        path = path + f'{root.val}'
        
        # Check if the current node is a leaf node which is also the base case
        # We only append path to paths when the current node is a leaf node.
        if not root.left and not root.right:
            paths.append(path)
            return
        
        # If it gets here, that means the current node is not a leaf node.
        # We check its children, left or right or both.
        # The reason we don't append path to paths is becasue the current node is not a leaf node,
        # the path, as of right now, IS INCOMPLETE.
        if root.left:
            self.dfs(root.left, paths, path + '->')
        if root.right:
            self.dfs(root.right, paths, path + '->')
