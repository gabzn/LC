https://leetcode.com/problems/largest-palindromic-number/

class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = Counter(num)
        max_odd_digit = max([int(d) for d, c in counter.items() if c % 2 == 1] + [-1])
        
        queue = deque()
        if max_odd_digit != -1:
            queue.append(str(max_odd_digit))
            counter[str(max_odd_digit)] -= 1

        for d, c in sorted(counter.items()):
            for _ in range(c // 2):
                queue.appendleft(d)
                queue.append(d)

        res = ''.join(queue).lstrip('0').rstrip('0')
        return res if res else '0'
