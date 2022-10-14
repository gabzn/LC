https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
  
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        # 3-pointer technique
        prior_to_slow = ListNode(-1, head)
        slow, fast = head, head
        
        # After the while loop, slow is guaranteed to be pointing to the target node.
        # prior_to_slow is the node prior to the target node.
        while fast and fast.next:
            prior_to_slow = prior_to_slow.next
            slow = slow.next
            fast = fast.next.next
                
        prior_to_slow.next = slow.next
        return head
