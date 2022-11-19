https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        ptr, stack = head, []
        while ptr:
            # Handle the case when a node has child.
            if ptr.child:    
                if ptr.next:
                    stack.append(ptr.next)
                    ptr.next.prev = None

                ptr.next = ptr.child
                ptr.next.prev = ptr
                ptr.child = None
            
            """
            When ptr next is None, that means ptr has gone through all the nodes on the current level.
            Time to connect the previous upper level, but we need to check if there's an upper level we can connect.
                Check if the stack is empty, if it is that means there's no more upper level and we are at the end of the linked list.
            """
            if not ptr.next:
                if stack:
                    upper_level_node = stack.pop()
                    ptr.next = upper_level_node
                    ptr.next.prev = ptr
                else:
                    break
                    
            ptr = ptr.next
            
        return head 
--------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ptr, end = head, head
        stack = []
        
        # Go throught the list and explore every node that has a child.
        # 1 - 2 - 3 - 7 - 8 - 11 - 12
        while ptr:
            if ptr.child:
                # If the current node has a child and its next is not null,
                # we push its next to the stack and remove its previous ptr to the current node.
                # stack: node 4, node 9
                if ptr.next:
                    stack.append(ptr.next)
                    ptr.next.prev = None
                
                # Change the pointer next and have it pointing to the child
                # Remove ptr.child since ptr.next is now pointing to the child
                # Set the child prev to the current node
                ptr.next = ptr.child
                ptr.child = None
                ptr.next.prev = ptr
            
            ptr = ptr.next
            
            # ptr will go to None eventually, we need a pointer to the very last node in the list.
            # ptr = null, end -> 12
            if ptr:
                end = ptr
        
        # Now we've traversed 1 - 2 - 3 - 7 - 8 - 11 - 12 and end is pointing to 12.
        # We look at the stack and connect the upper levels.
        while stack:
            previous_level_nodes = stack.pop()
            
            # Connect the upper level with the current end.
            # 10 -> 9
            # 10 <- 9
            end.next = previous_level_nodes
            previous_level_nodes.prev = end
            
            # Move end to 10, then repeat.
            while end.next:
                end = end.next
    
        return head
