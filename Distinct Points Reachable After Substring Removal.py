https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/description/

DIRECTIONS = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}

class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        distinct = set()
        x = y = 0
        for i in range(len(s)):
            dx, dy = DIRECTIONS[s[i]]
            x += dx
            y += dy

            left = i + 1 - k
            if left < 0:
                continue

            distinct.add((x, y))
            
            dx, dy = DIRECTIONS[s[left]]
            x -= dx
            y -= dy

        return len(distinct)
___________________________________________________________________
class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        N = len(s)
        DIRECTIONS = {
            'U': (0, 1),
            'D': (0, -1),
            'L': (-1, 0),
            'R': (1, 0)
        }

        pref = [(0, 0)] * (N + 1)
        for i, char in enumerate(s):
            (x, y) = DIRECTIONS[char]
            pref[i + 1] = (pref[i][0] + x, pref[i][1] + y)

        distinct = set()
        for i in range(N):
            # If we have a valid window, we try removing all the steps in the window.
            if i + 1 >= k:
                final_x, final_y = pref[-1]
                window_x, window_y = pref[i + 1][0] - pref[i - k + 1][0], pref[i + 1][1] - pref[i - k + 1][1]

                final_cord = (final_x - window_x, final_y - window_y)
                distinct.add(final_cord)

        return len(distinct)
