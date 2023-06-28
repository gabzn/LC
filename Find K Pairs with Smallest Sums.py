https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        LEN1, LEN2 = len(nums1), len(nums2)
        
        res, visited_pairs = [], set()
        heap = [(nums1[0] + nums2[0], 0, 0)]
        
        while heap and k:
            _, i1, i2 = heappop(heap)
            if (i1, i2) in visited_pairs:
                continue
            visited_pairs.add((i1, i2))
            
            res.append([nums1[i1], nums2[i2]])
            
            """
            We can move either i1 or i2 to the right.
            We explore both options by putting them into the heap.
            The heap will always sort pairs by their sums.
            """
            next_i1 = i1 + 1
            if next_i1 < LEN1:
                new_sum = nums1[next_i1] + nums2[i2]
                heappush(heap, (new_sum, next_i1, i2))
            
            next_i2 = i2 + 1
            if next_i2 < LEN2:
                new_sum = nums1[i1] + nums2[next_i2]
                heappush(heap, (new_sum, i1, next_i2))
            
            k -= 1
        return res
