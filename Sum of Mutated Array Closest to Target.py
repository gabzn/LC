https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def find_sum_when_val_is_mid(mid):
            # first idx that is <= mid
            i = bisect_left(arr, mid)
            if i == 0:
                return len(pref) * mid
            else:
                return pref[i - 1] + ((len(pref) - i) * mid)
                    
        arr.sort()    
        
        pref = [arr[0]]
        for num in arr[1:]:
            pref.append(pref[-1] + num)
                
        left, right = 0, max(arr) + 1
        while left + 1 != right:
            mid = (left + right) // 2
            sum_when_val_is_mid = find_sum_when_val_is_mid(mid)    

            if sum_when_val_is_mid == target:
                return mid
            
            if sum_when_val_is_mid < target:
                left = mid
            else:
                right = mid
            
        left_sum = find_sum_when_val_is_mid(left)
        right_sum = find_sum_when_val_is_mid(right)
        return left if abs(left_sum - target) <= abs(right_sum - target) else right
