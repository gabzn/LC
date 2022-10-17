https://leetcode.com/problems/add-two-numbers/
  
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head_val, carry = l1.val + l2.val, 0
        l1 = l1.next
        l2 = l2.next
        
        "Set up the new head"
        if new_head_val >= 10:
            new_head_val = new_head_val % 10
            carry = 1
        head = ListNode(new_head_val)
        ptr = head
        
        """
        Loop through both lists and add the numbers.
        If the sum is >= 10, get the remainder and set carry to 1 for next iteration.
        """
        while l1 and l2:
            new_val = l1.val + l2.val + carry
            
            if new_val >= 10:
                new_val = new_val % 10
                carry = 1
            else:
                carry = 0
                
            ptr.next = ListNode(new_val)
            ptr = ptr.next
            l1 = l1.next
            l2 = l2.next
        
        '''
        Take care of the case where one list is shorter than the other one.
        Loop through the longer list.
        '''
        while l1:
            new_val = l1.val + carry
            
            if new_val >= 10:
                new_val = new_val % 10
                carry = 1
            else:
                carry = 0
                
            ptr.next = ListNode(new_val)
            ptr = ptr.next     
            l1 = l1.next

        while l2:
            new_val = l2.val + carry
            
            if new_val >= 10:
                new_val = new_val % 10
                carry = 1
            else:
                carry = 0
                
            ptr.next = ListNode(new_val)
            ptr = ptr.next          
            l2 = l2.next
        
        # Last case where the last digit is >= 10, and thus we have a carry.
        if carry:
            ptr.next = ListNode(1)
        
        return head
