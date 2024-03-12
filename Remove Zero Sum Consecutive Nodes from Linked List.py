https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        previous_prefix_sum = set([0])
        running_sum = 0
        
        ptr = head
        while ptr:
            lst.append(ptr.val)
            running_sum += ptr.val
            
            # If a prefix sum occurs more than twice, there's a subarray in between that sums up to 0
            if running_sum in previous_prefix_sum:
                to_reach = running_sum
                to_reach -= lst.pop()
                
                # Pop val from the lst until the same running_sum is reached again
                while to_reach != running_sum:
                    previous_prefix_sum.remove(to_reach)
                    to_reach -= lst.pop()
            else:
                previous_prefix_sum.add(running_sum)
                
            ptr = ptr.next
        
        head = dummy = None
        for val in lst:
            if not head:
                head = ListNode(val)
                dummy = head
            else:
                dummy.next = ListNode(val)
                dummy = dummy.next
        
        return head
