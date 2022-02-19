A happy number is a number defined by the following process:

  Starting with any positive integer, replace the number by the sum of the squares of its digits.
  Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
  Those numbers for which this process ends in 1 are happy.
    
Return true if n is a happy number, and false if not.
  
https://leetcode.com/problems/happy-number/

class Solution {
    public boolean isHappy(int n) {
        if(n == 1) return true;
        
        // seenNums is used to store all the computed sums
        // If the same sum occurs twice, it means this number will repeat forever.
        HashSet<Integer> seenNums = new HashSet<>();
        
        while(n != 1) {
            int sum = 0;
            
            while(n != 0) {
                int digit = (n % 10) * (n % 10);
                sum = sum + digit;
                n = n / 10;
            }
            
            if(seenNums.contains(sum)) return false;
            seenNums.add(sum);
            n = sum;
        }
        
        return true;
    }
}
