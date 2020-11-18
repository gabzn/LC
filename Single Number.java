class Solution 
{
    //Solution using HashMap
    public int singleNumber(int[] nums) 
    {
        Map<Integer,Integer> map = new HashMap<>();   // Num = Key     Index = Value
        
        //This for-loop guarantees that when it's finished, the map will have ONLY 1 element, and it is the element that only appears once.
        for(int i=0;i<nums.length;i++) 
        {
            if(map.containsKey(nums[i])) //If the num is already in the map, remove it and don't add it to the map.
            {
                map.remove(nums[i]);
            } else                       //Otherwise, add it to the map. Num = key : Index = value. 
            {
                map.put(nums[i],i);
            }
        }                              
        
        //Find that unique num, and return it.
        for(int i=0;i<nums.length;i++)
        {
            if(map.containsKey(nums[i]))
            {
                return nums[i];
            }
        }
        return 0;
    }
    
    //Solution using HashSet
    public int singleNumber(int[] nums)
    {
        Set<Integer> set = new HashSet<>();
        
        for(int i=0;i<nums.length;i++)
        {
            if(set.contains(nums[i]))
            {
                set.remove(nums[i]);
            }
            else
            {
                set.add(nums[i]);
            }
        }
        
        Iterator<Integer> iterator = set.iterator();
        return iterator.next();
    }
    
    
}
