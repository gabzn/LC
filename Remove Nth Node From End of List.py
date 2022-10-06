Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        # The dummy node will point to the head which allows us to create a "previous" node
        # node_before_target will always be the node prior to the node we want to remove
        dummy = ListNode(-1, head)
        node_before_target = dummy
        runner = head
        
        # How to locate the target node?
        # We can first let runner be n unit ahead.
        for _ in range(n):
            runner = runner.next
        
        # Then we can have both node_before_target and runner move at the same time.
        while runner:
            node_before_target = node_before_target.next
            runner = runner.next
        
        # When the above while loop finishes, node_before_target is guaranteed to be in the correct position.
        node_before_target.next = node_before_target.next.next
        return dummy.next
--------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        # Create a dummy node that has next pointing to the head
        # 2 pointers, but we first move the fast by n steps
        dummy = ListNode(-1, head)
        fast = dummy
        while n:
            fast = fast.next
            n -= 1
        
        # The slow will start from the dummy. When fast.next is None, slow is guaranteed to be the node prior to the target node.
        slow = dummy
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        node_after_target = slow.next.next
        slow.next = node_after_target
        return dummy.next
