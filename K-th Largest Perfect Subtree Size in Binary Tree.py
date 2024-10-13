https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if not node.left and not node.right:
                res.append(1)
                return 1

            left = right = 0

            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)

            if left == right and left != 0:
                res.append(left + right + 1)
                return left +right + 1

            return 0

        res = []
        dfs(root)
        res.sort(reverse=True)
        return res[k - 1] if len(res) >= k else -1
