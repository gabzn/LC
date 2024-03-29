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
----------------------------------------------------------------------------------------
 class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        
        return prev
 ------------------------------------------------------------------------------------------
 class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return new_head
