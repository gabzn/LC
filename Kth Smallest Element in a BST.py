https://leetcode.com/problems/kth-smallest-element-in-a-bst/
  
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        while True:
            # Go all the way to the left to find the smallest
            while root:
                stack.append(root)
                root = root.left
            
            # After the inner while loop, the topmost element on the 
            # stack is guaranteed to be the smallest node.
            # We move root back to the smallest node by popping the smallest from the stack.
            root = stack.pop()
            
            k -= 1
            if k == 0:
                return root.val
            
            # Before go to the next iteration which will get back to the parent of the current node,
            # we want to check if the current smallest has a right child.
            # Because if the smallest has a right child, its right child will be the second smallest.
            root = root.right
