https://leetcode.com/problems/remove-nodes-from-linked-list/

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        while head:
            val = head.val
            while stack and stack[-1] < val:
                stack.pop()
            stack.append(val)
            head = head.next

        dummy = None
        for val in stack:
            if not head:
                head = ListNode(val)
                dummy = head
            else:
                dummy.next = ListNode(val)
                dummy = dummy.next
        
        return head
