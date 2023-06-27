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
