class Solution 
{
    public int singleNumber(int[] nums) 
    {
        Map<Integer,Integer> map = new HashMap<>();
        
        for(int i=0;i<nums.length;i++)
        {
            if(map.containsKey(nums[i]))
            {
                map.remove(nums[i]);
            } else 
            {
                map.put(nums[i],i);
            }
        }
        
        for(int i=0;i<nums.length;i++)
        {
            if(map.containsKey(nums[i]))
            {
                return nums[i];
            }
        }
        return 0;
    }
}
