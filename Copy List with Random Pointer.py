https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        old_to_new_mapping = {}
        ptr = head
        new_head = dummy = None
        while ptr:
            val = ptr.val

            if not new_head:
                new_head = Node(x=val)
                dummy = new_head
            else:
                dummy.next = Node(x=val)
                dummy = dummy.next

            old_to_new_mapping[ptr] = dummy
            ptr = ptr.next

        ptr = head
        while ptr:
            if ptr.random:
                old_to_new_mapping[ptr].random = old_to_new_mapping[ptr.random]

            ptr = ptr.next

        return new_head
