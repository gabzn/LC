https://leetcode.com/problems/palindrome-linked-list/

O(N) time + O(1) space where N is the number of nodes.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        # Reverse the right half of the list.
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        right_half_head = None
        while slow:
            next_node = slow.next
            slow.next = right_half_head
            
            right_half_head = slow
            slow = next_node
        
        # Start from head again and compare the left half and the right half.
        slow = head
        while slow and right_half_head:
            if slow.val != right_half_head.val:
                return False
            
            slow = slow.next
            right_half_head = right_half_head.next
            
        return True
 ------------------------------------------------------------------------------------------------------------------------------------
O(N) time + O(N) space where N is the number of nodes.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
            
        l, r = 0, len(stack) - 1
        while l <= r:
            if stack[l] != stack[r]:
                return False
            l += 1
            r -= 1
            
        return True
