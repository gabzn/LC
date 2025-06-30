https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        running_sum = 0

        for i, num in enumerate(arr):
            # Update
            running_sum += num

            # Check for length
            if i + 1 - k < 0:
                continue
            
            # Attemp to update result if criteria met
            avg = running_sum // k
            if avg >= threshold:
                res += 1
            
            # Remove leftmost num
            running_sum -= arr[i + 1 - k]

        return res
