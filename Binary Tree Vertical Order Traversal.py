https://leetcode.com/problems/binary-tree-vertical-order-traversal/

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        
        ordering = []
        queue = deque([(root, 100)])
        min_col = max_col = 100
        
        while queue:
            num_nodes_on_cur_level = len(queue)
            
            for _ in range(num_nodes_on_cur_level):
                node, col = queue.popleft()
                ordering.append((node.val, col))
                
                if node.left:
                    queue.append((node.left, col - 1))
                    min_col = min(min_col, col - 1)
                if node.right:
                    queue.append((node.right, col + 1))
                    max_col = max(max_col, col + 1)
        
        total_cols = max_col - min_col + 1
        res = [[] for _ in range(total_cols)]
        
        for val, col in ordering:
            res[col - min_col].append(val)

        return res
