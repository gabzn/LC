class Solution 
{
    public boolean validMountainArray(int[] arr) 
    {
        if(arr.length < 3) return false;    
        
        int l = 0;
        int r = arr.length - 1;
              
        for(;l<arr.length - 1;l++)
        {
            if(arr[l+1] <= arr[l]) break;
        }
        
        for(;r>0;r--)
        {
            if(arr[r-1] <= arr[r]) break;
        }
        
        return l == r && l != arr.length - 1 && r != 0;
    }
}

Input: arr = [2,1]
Output: false

Input: arr = [3,5,5]
Output: false

Input: arr = [0,3,2,1]
Output: true

Input: arr = [9,8,7,6,5,4,3,2,1,0]
Output: false

Input: arr = [0,1,2,3,4,5,6,7,8,9]
Output: false
