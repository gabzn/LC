https://leetcode.com/problems/reverse-linked-list-ii/

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        counter = 1
        
        prev, cur = None, head
        # Find the start
        while counter != left:
            prev = cur
            cur = cur.next
            counter += 1
        
        # Start reversing all nodes up to and including right
        conn, tail = prev, cur
        while counter <= right:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            
            counter += 1
        
        # conn and tail will be used at the end to fix connections
        if conn:
            conn.next = prev
        else:
            head = prev
        
        tail.next = cur
        return head
