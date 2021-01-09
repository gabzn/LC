Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class Solution 
{
    public boolean isSameTree(TreeNode p, TreeNode q) 
    {
        // Base case: when both nodes are null, they must be equal. Assuming both root nodes are null.
        if(p == null && q == null) return true;
        
        // If either one of them is not null, but the other one is null. They cannot be identical.
        if(p == null && q != null) return false;
        if(p != null && q == null) return false;
        
        // If both nodes are not null, but their vals are different. They cannot be the same trees.
        if(p.val != q.val) return false;
        
        return (isSameTree(p.left,q.left) && isSameTree(p.right,q.right));
    }
}

https://leetcode.com/problems/same-tree/
