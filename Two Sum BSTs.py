https://leetcode.com/problems/two-sum-bsts/

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        """"
        Convert both trees into lists and do 2-sum on them.
        Find the differences from the first list.
        If any of the differences exists in the second list, return True
        Runtime: O(N + M)
        Space: O(N + M)
        """"
        list1, list2 = [], []
        self.inorder(root1, list1)
        self.inorder(root2, list2)
        
        differences = {}
        for val in list1:
            difference = target - val
            differences[difference] = val
        
        for val in list2:
            if val in differences:
                return True
        
        return False

    def inorder(self, root, order):
        if not root:
            return
        self.inorder(root.left, order)
        order.append(root.val)
        self.inorder(root.right, order)
---------------------------------------------------------------------------------------------------
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        """""
        Brute-force approach is to explore all the combinations
        Runtime: O(N * M)
        Space: O(N * M)
        """""
        if not root1 or not root2:
            return False
        if root1.val + root2.val == target:
            return True
        return self.twoSumBSTs(root1, root2.left, target) or self.twoSumBSTs(root1, root2.right, target) or 
                self.twoSumBSTs(root1.left, root2, target) or self.twoSumBSTs(root1.right, root2, target)
