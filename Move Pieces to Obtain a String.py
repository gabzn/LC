https://leetcode.com/problems/move-pieces-to-obtain-a-string/

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        def get_left_and_right_indices(s):
            char_indices = defaultdict(list)
            for i, char in enumerate(s):
                if char == 'L' or char == 'R':
                    char_indices[char].append(i)
            return char_indices

        if start.replace("_", "") != target.replace("_", ""):
            return False

        start_left_right_indices = get_left_and_right_indices(start)
        target_left_right_indices = get_left_and_right_indices(target)

        # Every index of L in start >= every index of L in target
        for si, ti in zip(start_left_right_indices['L'], target_left_right_indices['L']):
            if si < ti:
                return False

        # Every index of R in start <= every index of R in target
        for si, ti in zip(start_left_right_indices['R'], target_left_right_indices['R']):
            if si > ti:
                return False

        return True
