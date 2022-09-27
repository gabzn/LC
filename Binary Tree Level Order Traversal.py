https://leetcode.com/problems/binary-tree-level-order-traversal/
  
Very basic BFS problem! Highly recommended!

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # BFS Problem
        res = []
        queue = deque()
        queue.append(root)
        
        while queue:
            # The number of pop operation depends on how many nodes there are on the current level,
            # We can find that just be looking at the current length of the queue.
            num_of_nodes_to_pop = len(queue)
            nodes_in_cur_level = []
        
            for _ in range(num_of_nodes_to_pop):
                # We want to pop every node in the current level and store its non-null children.
                node = queue.popleft()
                nodes_in_cur_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(nodes_in_cur_level)  
        return res        
