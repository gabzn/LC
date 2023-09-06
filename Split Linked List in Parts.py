https://leetcode.com/problems/split-linked-list-in-parts/
https://www.youtube.com/watch?v=Fev38Ys6LHw

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        total_nodes, ptr = 0, head
        while ptr:
            total_nodes += 1
            ptr = ptr.next
        
        res, prev = [], ListNode()
        nodes_in_each_part, extra_nodes = divmod(total_nodes, k)
        
        for _ in range(k):
            res.append(head)
            
            for _ in range(nodes_in_each_part):
                if head:
                    prev = head
                    head = head.next
                
            if extra_nodes:
                prev = head
                head = head.next
                extra_nodes -= 1
            
            prev.next = None
        
        return res
