class Solution 
{
    public int[] replaceElements(int[] arr) 
    {
        
        // Assume the last element is the max, then change the last element to -1.
        int curMax = arr[arr.length - 1];
        arr[arr.length - 1] = -1;
        
        
        // Loop through the array starting from the second element from the end.
        for(int i=arr.length-2;i>=0;i--)
        {
            // If the current index is greater than curMax.
            // First, change current index to curMax,
            // Then, change curMax to current index.
            if(arr[i] > curMax)
            {
                int temp = arr[i];
                arr[i] = curMax;
                curMax = temp;
            }
            
            // Otherwise, just change the current index to curMax and have curMax unchanged.
            else    arr[i] = curMax;
        }
        return arr;
    }
}

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
