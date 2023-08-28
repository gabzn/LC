https://leetcode.com/problems/binary-tree-right-side-view/

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        
        res = []
        queue = deque([root])
        
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
            
            res.append(current_level[-1])
            
        return res
