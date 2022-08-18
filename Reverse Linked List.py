# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 3 pointers approach
        prev, new_head, next_node = None, head, head.next
        while next_node:
            new_head.next = prev
            prev = new_head
            new_head = next_node
            
            next_node = next_node.next
        
        new_head.next = prev
        return new_head
