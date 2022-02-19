Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true
  
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

  
class Solution {
    public boolean containsDuplicate(int[] nums) {
        if(nums.length == 1) return false;
        
        HashSet<Integer> uniqueNums = new HashSet<>();
        for(int num : nums) {
            if(uniqueNums.contains(num)) return true;
            uniqueNums.add(num);
        }
        
        return false;
    }
}
