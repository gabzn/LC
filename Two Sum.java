class Solution 
{
    public int[] twoSum(int[] nums, int target) 
    {
        int[] toReturn = new int[2];
        Map<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            int complement = target - nums[i];
            if(map.containsKey(complement))
            {
                toReturn[0] = i;
                toReturn[1] = map.get(complement);
            }
            map.put(nums[i],i);
        }
        return toReturn;
    }
}
