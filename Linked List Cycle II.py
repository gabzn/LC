https://leetcode.com/problems/linked-list-cycle-ii/
  
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). 
It is -1 if there is no cycle. Note that pos is not passed as a parameter.

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        # We first find the intersection.
        # The intersection tells us 2 things:
        #       1: There's a cycle
        #       2: We can find the node that starts the cycle by starting a new ptr.
        slow, fast = head, head
        intersection_node = None
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                intersection_node = slow
                break
        
        if not intersection_node:
            return None
        
        # If it gets here, that means there's a cycle. Now find the start of the cycle by having another ptr from the start and loop until they meet.
        slow = head
        while slow != intersection_node:
            slow = slow.next
            intersection_node = intersection_node.next  
        return slow
