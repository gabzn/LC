class Solution 
{
    public int[] sortArrayByParity(int[] arr) 
    {
        int p = 0;
        
        // Two-pointer approach.
        for(int i=0;i<arr.length;i++)
        {
            // If the current value is not an even number, go to next iteration until it is an even number.
            // If it is an even number, swap it with the nums[p] and move p one unit to the right.
            
            if( (arr[i] % 2) != 0 ) continue;
            else
            {
                int temp = arr[p];
                arr[p] = arr[i];
                arr[i] = temp;
                
                p++;
            }
        }

        return arr;
    }
}


Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
