https://leetcode.com/problems/number-of-longest-increasing-subsequence/
https://www.youtube.com/watch?v=td8JCnqt-JI

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        LEN = len(nums)
        longest_at_index, count = [1] * LEN, [1] * LEN
        
        """
              1  3  5  4  7
          len 1  2  3  3  4     
        count 1  1  1  1  2
        """
        for r in range(LEN):
            for l in range(r):
                # We only care when the current num is larger than any previous num
                if nums[l] < nums[r]:
                    # If previous longest + 1 is greater than current longest
                    # update current longest and copy the number of count
                    if longest_at_index[l] + 1 > longest_at_index[r]:     
                        longest_at_index[r] = 1 + longest_at_index[l]
                        count[r] = count[l]                        

                    # r is pointing to 7 and l is pointing to 5
                    # len[l] + 1 > len[r] -> 3 + 1 > 1:
                    #   len[r] = 1 + len[l] -> len[r] = 1 + 3
                    #   count[r] = count[l] -> count[r] = 1
                    # ----------------------------------------------
                    # r is pointing to 7 and l is now pointing to 4
                    # len[l] + 1 == len[r] -> 3 + 1 == 4
                    #   don't update len[r]. Add count[l] to count[r]
                    elif longest_at_index[l] + 1 == longest_at_index[r]:
                        count[r] += count[l]

        res, max_length = 0, max(longest_at_index)    
        for index, length in enumerate(longest_at_index):
            if length == max_length:
                res += count[index]
        
        return res
