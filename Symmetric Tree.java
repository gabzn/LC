class Solution 
{
    public boolean isSymmetric(TreeNode root) 
    {
        if(root == null) return true;
        return isSymmetric(root.left, root.right);
    }
    
    private boolean isSymmetric(TreeNode left, TreeNode right)
    {
        //Base cases.
        if(left == null && right == null) return true;                            // If both are null, then good.
        else if(left == null || right == null) return false;                      // If one of them is null, bad.
        
        // If none of the above is triggered, then check the vals in left and right first.
        // Then recursively call the function.
        return left.val == right.val && isSymmetric(left.left, right.right) && isSymmetric(left.right, right.left);
    }
}



Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
