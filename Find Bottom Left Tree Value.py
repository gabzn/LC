https://leetcode.com/problems/find-bottom-left-tree-value/

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = deque([root])
        
        while queue:
            is_first = True
            for _ in range(len(queue)):
                node = queue.popleft()
                if is_first:
                    res = node.val
                    is_first = False
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
    
        return res
