https://leetcode.com/problems/binary-tree-level-order-traversal/
  
Very basic BFS problem! Highly recommended!

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque()
        queue.append(root)
        
        while queue:
            # We use a list to store all the nodes in the current level
            # The number of pop depends on how many nodes there are on the current level,
            # We can find that just be looking at the current length of the queue.
            nodes_in_cur_level = []
            num_of_nodes_to_pop = len(queue)
            
            for num in range(num_of_nodes_to_pop):
                # We want to pop every node in the current level and store its children.
                node = queue.popleft()
                nodes_in_cur_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(nodes_in_cur_level)  
        return res        
