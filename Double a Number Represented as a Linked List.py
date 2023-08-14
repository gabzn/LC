https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

class Solution:
    
    def add_new_node_with_value(self, dummy, value):
        new_node = ListNode(val=value)
        new_node.next = dummy.next
        dummy.next = new_node
    
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        number = 0
        while head:
            number *= 10
            number += head.val
            head = head.next
        
        carry = 0
        dummy = ListNode()
        while number:

            # Get the last digit and double it
            last_digit = (number % 10) * 2 + carry
            if last_digit >= 10:
                last_digit = last_digit % 10
                carry = 1
            else:
                carry = 0
            
            # Make a new node for this number
            self.add_new_node_with_value(dummy, last_digit)
            number //= 10
          
        if carry:
            self.add_new_node_with_value(dummy, 1)

        return dummy.next if dummy.next else ListNode(val=0)
