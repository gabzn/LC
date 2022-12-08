https://leetcode.com/problems/odd-even-linked-list/
  
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd_ptr = head
        even_head = head.next
        even_ptr = even_head
        
        while odd_ptr.next and even_ptr.next:
            odd_ptr.next = even_ptr.next
            even_ptr.next = even_ptr.next.next
            
            odd_ptr = odd_ptr.next
            even_ptr = even_ptr.next
        
        odd_ptr.next = even_head
        return head
