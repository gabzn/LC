class Solution 
{
    public int removeDuplicates(int[] nums) 
    {
        if(nums.length == 0) return 0;
        
        int size = 0;
        
        for(int i=1;i<nums.length;i++)
            if(nums[size] != nums[i])    
                nums[++size] = nums[i];
        
//         for(int i=1;i<nums.length;i++)
//             if(nums[size] != nums[i])
//             {
//                 size++;
//                 nums[size] = nums[i];
//             }
        
        return size+1;
    }
}
//'size' manages the return value as well as the index number.
//'size' keep track of the non-duplicate values.
//Super stupid question ngl.



//          nums[] = [  1   ,   1   ,   2  ]
//                     size     i          
//          Each iteration checks if nums[size] is equal to nums[i]; If they are equal, go to next iteration, increment i by 1 and keep 'size' unchanged. 

//          nums[] = [  1   ,   1    ,  2  ]
//                     size             i
//          nums[size] is not equal to nums[i].
//          Increment 'size' by 1 and assign nums[i] value to nums[size]

//          nums[] = [  1   ,   1    ,  2  ]
//                             size     i
//          nums[] = [  1   ,   2    ,  2  ]
//                             size     i

//          'size == 1' when the loop is finished, but the correct size should be 2. Therefore, 'return size+1'.
