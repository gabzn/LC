class Solution 
{
    public boolean hasPathSum(TreeNode root, int targetSum) 
    {
       if(root == null) return false;
       
       //Each recursive call, we subctract the current value from the sum and pass it in for the new sum.
       if(targetSum == root.val && root.left == null && root.right == null) return true;
       
       return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val);
    }
}


Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.   <----------- This defines one of the base cases.  (root.left == null && root.right == null)


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

5 ---> 4 ---> 11 ---> 2 


                                                5
                                               /  \
                                              4     8
                                             /     / \
                                            11    13  4
                                           /  \        \
                                          7    2        1
