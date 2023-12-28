https://leetcode.com/problems/merge-nodes-in-between-zeros/

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = None
        
        while head.next:
            if head.val == 0:
                head = head.next
                running_sum = 0
                
                while head and head.val != 0:
                    running_sum += head.val
                    head = head.next
                                
                if ptr == None:
                    ptr = ListNode(running_sum)
                    dummy.next = ptr
                else:
                    ptr.next = ListNode(running_sum)
                    ptr = ptr.next
                
        return dummy.next
