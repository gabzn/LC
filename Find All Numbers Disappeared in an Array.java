Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.
  
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

class Solution 
{
    public List<Integer> findDisappearedNumbers(int[] nums) 
    {
        // Two data structures would be used to tackle this problem.
        // Since the return type must be a list, the array list is used here. Other option like linked list is also acceptable.
        // Set only contains unique number. 
        List<Integer> disappearedNums = new ArrayList<>();
        Set<Integer> set = new HashSet<>();
        
        // First add all the unique numbers into a set to filter out those are duplicated.
        for(int i : nums)
        {
            set.add(i);
        }
        
        // Loop from 1 up to and including n, check if the set contains the current i value. If not, add it to the list.
        for(int i=1;i<=nums.length;i++)
        {
            if(! set.contains(i) ) disappearedNums.add(i); 
        }
        
        return disappearedNums;
    }
} 
