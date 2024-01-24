https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def is_palindromic(counter):
                has_only_one_odd = False
                
                for _, count in counter.items():
                    if count % 2 == 1:
                        if has_only_one_odd:
                            return False
                        has_only_one_odd = True            
                
                return True
        
        def dfs(node, counter):
            if node:
                counter[node.val] += 1
                
                if not node.left and not node.right:
                    if is_palindromic(counter):
                        res[0] += 1
                
                dfs(node.left, counter)
                dfs(node.right, counter)
                counter[node.val] -= 1                
                            
        res = [0]
        dfs(root, Counter())
        return res[0]
