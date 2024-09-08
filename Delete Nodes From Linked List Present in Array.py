https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        
        cur = head
        prev = ListNode(next=cur)
        new_head = None
        
        while cur:
            val = cur.val
            
            if val in nums:
                prev.next = cur.next
            else:
                prev = prev.next
                if new_head == None:
                    new_head = cur

            cur = cur.next

        return new_head
