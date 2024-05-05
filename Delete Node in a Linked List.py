https://leetcode.com/problems/delete-node-in-a-linked-list/

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
#         dummy = ListNode(-1)
#         dummy.next = node
        
#         while node.next:
#             node.val = node.next.val
#             dummy = dummy.next
#             node = node.next
        
#         dummy.next = None
