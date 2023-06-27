https://leetcode.com/problems/populating-next-right-pointers-in-each-node

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = deque([root])
        
        while queue:
            # Use a queue to store the next-level nodes
            children = deque()
            
            # Connect all nodes on the same level
            while queue:
                node = queue.popleft()
                if queue:
                    node.next = queue[0]
                    
                if node.left:
                    children.append(node.left)
                    children.append(node.right)
            
            # Put next-level nodes back to the queue
            while children:
                queue.append(children.popleft())
            
        return root
------------------------------------------------------------------------------------------------
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        queue = deque([root])
        while queue:
            number_of_nodes_on_current_level = len(queue)
            
            # Pop out all the nodes on the current level
            # The number of pop depends on number_of_nodes_on_current_level
            while number_of_nodes_on_current_level:
                node = queue.popleft()
                
                # If there's more than 1 node in the current level, 
                # connect the current one to the next one.
                if number_of_nodes_on_current_level > 1:
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
                
                number_of_nodes_on_current_level -= 1
              
        return root
