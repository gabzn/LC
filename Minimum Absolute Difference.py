https://leetcode.com/problems/minimum-absolute-difference/
  
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        answer = []
        min_abs_difference = math.inf
        
        # First go throught arr to find the minimum absolute difference.
        for ind in range(1, len(arr)):
            min_abs_difference = min(min_abs_difference, arr[ind]-arr[ind-1])
        
        # Append pairs that have MAD/
        for ind in range(1, len(arr)):
            if arr[ind]-arr[ind-1] == min_abs_difference:
                # pair = [arr[ind-1], arr[ind]]
                # answer.append(pair)
                answer.append([arr[ind-1], arr[ind]])
        
        return answer

---------------------------------------------------------------------------------------------------------
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        answer = []
        min_abs_difference = math.inf
        
        for ind in range(1, len(arr)):
            difference = arr[ind] - arr[ind-1]
            
            # If the current difference is the min_abs_difference, 
            # append the current pair to answer and go to next the iteration.
            if min_abs_difference == difference:
                answer.append([arr[ind-1], arr[ind]])
                continue
            
            # If the current difference is smaller,
            # drop all the previous pairs, append the current pair 
            # and set min_abs_difference to the new min.
            if min_abs_difference > difference:
                answer = [[arr[ind-1], arr[ind]]]        
                min_abs_difference = difference
        
        return answer
