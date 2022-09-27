https://leetcode.com/problems/binary-tree-right-side-view/
  
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
  
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # BFS Problem
        res = []
        queue = deque()
        queue.append(root)
        
        while queue:
            # num_of_nodes_to_pop tells us how many pop operations we need to do which is equal to the number of nodes in the current level.
            # We need to pop every single node on the current level and store its non-null children.
            num_of_nodes_to_pop = len(queue)
            
            # Right side view means the rightmost node in the current level which is the last node in the queue.
            rightmost_node = queue[-1]
            res.append(rightmost_node.val)
            
            for _ in range(num_of_nodes_to_pop):    
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
