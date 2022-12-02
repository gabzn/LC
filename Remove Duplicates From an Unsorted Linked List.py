from collections import defaultdict
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        counts = defaultdict(int)
        
        # Get the count of each val
        cur = head
        while cur:
            counts[cur.val] += 1
            cur = cur.next
        
        # Two pointers
        dummy = ListNode(-1, head)
        prev = dummy
        cur = head
        
        # Only move prev when cur is not a duplicate.
        while cur:
            if counts[cur.val] == 1:
                cur = cur.next
                prev = prev.next
            else:
                cur_next = cur.next
                prev.next = cur_next
                
                cur = cur_next
                
        return dummy.next
