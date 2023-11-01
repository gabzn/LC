https://leetcode.com/problems/find-mode-in-binary-search-tree/

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        self.dfs(root, counter)
        
        mode = max(counter.values())
        return [k for k, f in counter.items() if f == mode]
        
    def dfs(self, root, counter):
        if not root:
            return
        counter[root.val] += 1
        self.dfs(root.left, counter)
        self.dfs(root.right, counter)
