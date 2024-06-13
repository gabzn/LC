https://leetcode.com/problems/median-of-two-sorted-arrays/
https://www.youtube.com/watch?v=wDBnBA82z1c

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M, N = len(nums1), len(nums2)
        if M > N:
            return self.findMedianSortedArrays(nums2, nums1)
        
        total_elements_on_the_left = (M + N + 1) // 2
        left = 0
        right = M
        
        while left <= right:
            i = (left + right) // 2
            j = total_elements_on_the_left - i

            num1_left = nums1[i - 1] if i > 0 else -inf
            num1_right = nums1[i] if i < M else inf

            num2_left = nums2[j - 1] if j  > 0 else -inf
            num2_right = nums2[j] if j < N else inf
            
            if num1_left <= num2_right and num2_left <= num1_right:
                if (M + N) % 2 == 0:
                    return (max(num1_left, num2_left) + min(num1_right, num2_right)) / 2
                else:
                    return max(num1_left, num2_left)
            

            if num1_left > num2_right:
                right = i - 1
            else:
                left = i + 1
