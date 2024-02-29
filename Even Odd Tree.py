https://leetcode.com/problems/even-odd-tree/

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, 0)])
        
        while queue:
            previous_val = 0 if queue[0][1] % 2 == 0 else inf
            
            for _ in range(len(queue)):
                node, level = queue.popleft()
                
                if level % 2 == 0 and (node.val % 2 == 0 or node.val <= previous_val):
                    return False
                
                if level % 2 == 1 and (node.val % 2 == 1 or node.val >= previous_val):
                    return False
                
                previous_val = node.val
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
                    
        return True
