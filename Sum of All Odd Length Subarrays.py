https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
  
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        LEN = len(arr)
        
        # Computer the prefix sum inplace
        for ind in range(1, LEN):
            arr[ind] += arr[ind-1]
		
		# The initial value of res is the total sum since every num itself has a length of 1
        res = arr[-1]
        
        # Get the sums of all odd-length subarrays 
        odd_len = 3
        max_odd_len = LEN if LEN % 2 == 1 else LEN - 1
        while odd_len <= max_odd_len:
            
            for left_ind in range(LEN):
                right_ind = left_ind + (odd_len - 1)
                
                if right_ind >= LEN:
                    break
                
                if left_ind == 0:
                    res += arr[right_ind]
                else:
                    res += arr[right_ind] - arr[left_ind-1]
            
            odd_len += 2
        
        return res
