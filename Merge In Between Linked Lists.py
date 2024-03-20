https://leetcode.com/problems/merge-in-between-linked-lists/

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:        
        distance = b - a + 1
        
        node_before_a = list1
        node_b = list1
        
        while distance:
            node_b = node_b.next
            distance -= 1
            b -= 1
            
        while b:
            node_b = node_b.next
            node_before_a = node_before_a.next
            b -= 1
        
        list_2_last_node = list2
        while list_2_last_node.next:
            list_2_last_node = list_2_last_node.next
        
        node_before_a.next = list2
        list_2_last_node.next = node_b.next
        return list1
