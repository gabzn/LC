Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


class Solution 
{
    public int maxDepth(TreeNode root) 
    {
        // Base case: when it hits null, it means it has no depth.
        if(root == null) return 0;                                   
        
        // The max depth will be either from the left side or right side.
        // We'll take the side that has deeper depth then add 1 since root itself has depth of 1. 
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}


https://leetcode.com/problems/maximum-depth-of-binary-tree/
Like most of the tree problems, recursion is probably always the approach you want to try.
