https://leetcode.com/problems/sliding-subarray-beauty/

from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        N = len(nums)
        sl = SortedList()
        res = []
        left = right = negative_count = 0

        while right < N:
            # If the window size > k, move left 1 unit to the right
            if right - left + 1 > k:
                sl.remove(nums[left])
                if nums[left] < 0:
                    negative_count -= 1
                left += 1

            # Add the current num to the window
            if nums[right] < 0:
                negative_count += 1
            sl.add(nums[right])
            
            # If we have at least window size, add the xth smallest
            if right >= k - 1:
                if negative_count < x:
                    res.append(0)
                else:
                    res.append(sl[x - 1])

            right += 1

        return res
------------------------------------------------------------------------------
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        N = len(nums)
        window = defaultdict(int)
        res = []
        negative_count = 0
        left = right = 0

        while right < N:
            # If the window size > k, move left 1 unit to the right
            if right - left + 1 > k:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]

                if nums[left] < 0:
                    negative_count -= 1
                left += 1                

            # Add the current num to the window
            num = nums[right]
            if num < 0:
                negative_count += 1
            window[num] += 1
            
            # If we have at least window size, add the xth smallest
            if right >= k - 1:
                if negative_count < x:
                    res.append(0)
                else:
                    cnt = 0
                    for n, c in sorted(window.items()):
                        cnt += c
                        if cnt >= x:
                            res.append(n)
                            break

            right += 1

        return res
