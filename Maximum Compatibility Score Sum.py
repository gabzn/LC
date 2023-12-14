https://leetcode.com/problems/maximum-compatibility-score-sum/

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:                
        def compute_score(si, mi):
            return sum([1 if sa == ma else 0 for sa, ma in zip(students[si], mentors[mi])])
        
        # Try all different possible combinations of student-mentor pairs
        def dfs(student_index, mentor_mask, score):
            if student_index == M:
                res[0] = max(res[0], score)
                return
        
            # Pair every single student with a mentor
            for mentor_index in range(M):
                if mentor_mask & (1 << mentor_index):
                    compatibility_score = compute_score(student_index, mentor_index)
                    dfs(student_index + 1, mentor_mask ^ (1 << mentor_index), score + compatibility_score)
        
        M = len(students)
        res = [0]
        dfs(0, (1 << M) - 1, 0)
        return res[0]
