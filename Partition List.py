https://leetcode.com/problems/partition-list/

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than_x, greater_or_equal_x = [], []
        
        index = 0
        while head:
            if head.val < x:
                heappush(less_than_x, (index, head.val))
            else:
                heappush(greater_or_equal_x, (index, head.val))
            
            head = head.next
            index += 1
        
        ptr = ListNode()
        dummy = ptr
        
        while less_than_x:
            _, val = heappop(less_than_x)
            dummy.next = ListNode(val)
            dummy = dummy.next
        
        while greater_or_equal_x:
            _, val = heappop(greater_or_equal_x)
            dummy.next = ListNode(val)
            dummy = dummy.next
        
        return ptr.next
---------------------------------------------------------------------------------------------
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_for_less_than = less_than = ListNode()
        dummy_for_greater_or_equal = greater_or_equal = ListNode()
        
        while head:
            val = head.val
            
            if val < x:
                less_than.next = head
                less_than = less_than.next
            else:
                greater_or_equal.next = head
                greater_or_equal = greater_or_equal.next
            
            head = head.next
        
        greater_or_equal.next = None
        less_than.next = dummy_for_greater_or_equal.next
        
        return dummy_for_less_than.next
