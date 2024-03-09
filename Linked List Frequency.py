https://leetcode.com/problems/linked-list-frequency/

class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        counter = Counter()
    
        while head:
            counter[head.val] += 1
            head = head.next
        
        dummy = None
        for _, freq in counter.items():
            new_node = ListNode(val=freq)
            
            if dummy == None:
                dummy = new_node
                head = dummy
            else:
                dummy.next = new_node
                dummy = dummy.next
        
        return head
