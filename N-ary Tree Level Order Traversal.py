https://leetcode.com/problems/n-ary-tree-level-order-traversal/

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])        
        
        while queue:
            num_nodes_on_current_level = len(queue)
            all_nodes_on_current_level = []
            
            while num_nodes_on_current_level:
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
                    
                all_nodes_on_current_level.append(node.val)
                num_nodes_on_current_level -= 1
                
            res.append(all_nodes_on_current_level)
    
        return res
