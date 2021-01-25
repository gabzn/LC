class Solution 
{
    public int removeElement(int[] nums, int val) 
    {
        int total_appearance = 0;                              
        int appearance_times = 0;
        int j = nums.length - 1;
        
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i] == val) total_appearance++;
        }
         
        for(int i=0;i<nums.length;i++)
        {
            if(total_appearance == appearance_times) break;
            
            if(nums[i] == val)
            {
                //'j' is pointing to the last element of the array.
                //Decrement 'j' until the 'j' index is not equal to val.
                //Increment the number of times that 'val' appears.
                while(nums[j] == val && j != i) 
                {
                    j--;
                    appearance_times++;
                }
                
                //Once the 'j' index is not equal to val.
                //Swap, then decrement 'j' and increment 'appearance_times'.
                //If we don't decrement 'j', the 'j' index will be equal to 'val', then we'll increment 'appearance_times' again.
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                
                appearance_times++;
                j--;
            }
        }
        return nums.length - total_appearance; 
    }
}

//----------------------------------------------------------------------------------------------------

class Solution 
{
    public int removeElement(int[] nums, int val) 
    {
        int totalVal = 0;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i] == val) totalVal++;
        }
        
        // Handle the case when the entire array contains only val. 
        // nums = [3,3,3]        val = 3
        if(totalVal == nums.length) return 0;
        
        // currentVal holds the current number of val.
        int currentVal = totalVal;
        int frontP = 0;
        int backP = nums.length - 1;
        
        while(currentVal != 0)
        {
            // If the current val is equal to val, we check from the back of the array.
            if(nums[frontP] == val)
            {
                // If the back of the array is also equal to val, we move the backP pointer and decrement currentVal until the value is not val.
                while(nums[backP] == val)
                {
                    backP--;
                    currentVal--;
                }
                if(currentVal == 0) break;
                
                nums[frontP] = nums[backP];
                backP--;
                currentVal--;
            }
            frontP++;
        }
        
        return nums.length - totalVal; 
    }
}



