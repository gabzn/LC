https://leetcode.com/problems/find-largest-value-in-each-tree-row/

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:        
        if not root:
            return []
        
        res = []
        queue = deque([root])

        while queue:
            size = len(queue)
            
            max_in_cur_level = -inf
            for _ in range(size):
                node = queue.popleft()                
                max_in_cur_level = max(max_in_cur_level, node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(max_in_cur_level)
        
        return res
