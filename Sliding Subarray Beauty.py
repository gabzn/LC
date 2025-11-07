https://leetcode.com/problems/sliding-subarray-beauty/

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        N = len(nums)
        
        res = [0] * (N - k + 1)
        buckets = [0] * 101

        for i, num in enumerate(nums):
            buckets[num] += 1

            left = i + 1 - k
            if left < 0:
                continue

            count = x
            # Only look at the buckets that hold negative number
            for j in range(-50, 0):
                # buckets[j] = how many j's we have at bucket[j]
                # buckets[-23] = how many -23 we have at bucket[-23]
                # If count becomes negative after subtracting the count in a bucket, 
                # we know the number in the bucket is the answer.
                count -= buckets[j]
                if count <= 0:
                    res[left] = j
                    break

            buckets[nums[left]] -= 1

        return res
____________________________________________________________________________________
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        sorted_list = SortedList()

        for i, num in enumerate(nums):
            sorted_list.add(num)

            left = i + 1 - k
            if left < 0:
                continue

            x_smallest = sorted_list[x - 1]
            if x_smallest < 0:
                res.append(x_smallest)
            else:
                res.append(0)
            
            sorted_list.remove(nums[left])

        return res
