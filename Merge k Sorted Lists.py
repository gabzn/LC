https://leetcode.com/problems/merge-k-sorted-lists/

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for node in lists:
            while node:
                heappush(heap, node.val)
                node = node.next
        
        head = dummy = None
        while heap:
            val = heappop(heap)
            if not head:
                head = ListNode(val)
                dummy = head
            else:
                dummy.next = ListNode(val)
                dummy = dummy.next
        
        return head
