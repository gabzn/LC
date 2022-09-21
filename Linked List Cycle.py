Given head, the head of a linked list, determine if the linked list has a cycle in it.

https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        # Two pointer technique where fast will be 2-step ahead of slow.
        # If fast is only 1-step ahead, that will never find if the list has a cycle or not.
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
                
        return False
