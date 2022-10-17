https://leetcode.com/problems/add-two-numbers-ii/
  
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
  
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Push values of each list into a stack
        stack_1, stack_2 = [], []
        while l1:
            stack_1.append(l1.val)
            l1 = l1.next
            
        while l2:
            stack_2.append(l2.val)
            l2 = l2.next
    
        # Start popping off from the stack and work our way backward    
        last_value, carry = stack_1.pop() + stack_2.pop(), 0
        if last_value >= 10:
            last_value = last_value % 10
            carry = 1
        head = ListNode(last_value)
        
        # Loop through both stacks until one of them or both are empty
        while stack_1 and stack_2:
            new_val = stack_1.pop() + stack_2.pop() + carry
            if new_val >= 10:
                new_val = new_val % 10
                carry = 1
            else:
                carry = 0
            
            # Make a new node for the current value, have its next pointing to the last node. Then move head into the new node.
            new_node = ListNode(new_val, head)
            head = new_node
        
        # These two while loops take care of the case where one list is shorter than the other one.
        while stack_1:
            new_val = stack_1.pop() + carry
            if new_val >= 10:
                new_val = new_val % 10
                carry = 1
            else:
                carry = 0            
                
            new_node = ListNode(new_val, head)
            head = new_node

        while stack_2:
            new_val = stack_2.pop() + carry
            if new_val >= 10:
                new_val = new_val % 10
                carry = 1
            else:
                carry = 0            
                
            new_node = ListNode(new_val, head)
            head = new_node
        
        # Take care of the case where the last digit is >= 10, we need to append another 1 in the front if it's >= 10.
        if carry:
            new_node = ListNode(1, head)
            head = new_node
        
        return head
