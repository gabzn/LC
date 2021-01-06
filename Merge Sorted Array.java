class Solution 
{
    public void merge(int[] nums1, int m, int[] nums2, int n)
    {
        
        //Both pointers point to the last non-zero element of the array.
        int n1p = m-1;
        int n2p = n-1;
        
        //p1 points to the last element in nums1.
        int p1 = m + n - 1;
        
        //Loop starts from the back of the arrays.
        while(n1p >= 0 && n2p >= 0)
        { 
            if(nums2[n2p] > nums1[n1p])    nums1[p1] = nums2[n2p--];
            else nums1[p1] = nums1[n1p--];
                
            p1--;
        }
        
        //Cases where n1p reaches the head of the array, and n2p does not.
        //We will just need to copy over elements in nums2 into nums1 directly.
        while(n2p >= 0)
        {
            nums1[p1--] = nums2[n2p--];
        }
    }
}

//Start swapping from the end of the arrays.
//If current n2p is greater than current n1p, copy n2p into p1 and decrement n2p.
//If current n2p is less than current n1p, copy n1p into p1 and decrement n1p.
//Decrement p1 when either case is finished.

nums1 = [1, 2, 3, 0, 0, 0]
               ^        ^
              n1p       p1

nums2 = [2, 5, 6]
               ^
              n2p
--------------------------------------
nums1 = [1, 2, 3, 0, 0, 6]
               ^     ^
              n1p    p1

nums2 = [2, 5, 6]
            ^
           n2p
---------------------------------------
nums1 = [1, 2, 3, 0, 5, 6]
               ^  ^
              n1p p1

nums2 = [2, 5, 6]
         ^
        n2p
---------------------------------------
nums1 = [1, 2, 3, 3, 5, 6]
            ^  ^
           n1p p1

nums2 = [2, 5, 6]
         ^
        n2p
----------------------------------------
nums1 = [1, 2, 2, 3, 5, 6]
         ^  ^
        n1p p1

nums2 = [2, 5, 6]
       ^
      n2p
----------------------------------------
n2p reaches 0. While loop condition fails. Exits.
  
              
              
        
