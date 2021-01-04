// A classic dynamic programming problem.

// Approach without using memoization.
class Solution 
{
    int solution = 0;
    public int climbStairs(int n) 
    {
        if(n==0) return 1;
        if(n<0) return 0;
        
        solution = climbStairs(n-1) + climbStairs(n-2);
        
        return solution;
    }
}



// Approach with memoization. (Using array)
class Solution 
{
    public int climbStairs(int n) 
    {
        int[] array = new int[n+1];   //The reason the size has to be 'n+1' is because the range is from (0 to n) instead of (1 to n).
        array[0] = 1;
        array[1] = 1;
        
        for(int i=2;i<n+1;i++)
        {
            array[i] = array[i-1] + array[i-2];
        }
        
        return array[n];
    }
}
