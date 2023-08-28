https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        
        res = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            LEN = len(queue)
            current_level = []
            
            for _ in range(LEN):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if left_to_right:
                res.append(current_level)
            else:
                res.append(current_level[::-1])
                        
            left_to_right = not left_to_right
            
        return res
