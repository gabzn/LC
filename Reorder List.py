https://leetcode.com/problems/reorder-list/

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = 0
        order = deque()
        reverse_order = []
        
        while head:
            next_node = head.next
            head.next = None
            
            order.append(head)
            reverse_order.append(head)
            nodes += 1
            head = next_node
        
        ptr = None
        while nodes:
            if len(order) == len(reverse_order):
                if not head:
                    head = order.popleft()
                    ptr = head
                else:
                    ptr.next = order.popleft()
                    ptr = ptr.next
            else:
                ptr.next = reverse_order.pop()
                ptr = ptr.next
            
            nodes -= 1
        
        return head
