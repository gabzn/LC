https://leetcode.com/problems/word-break-ii/

class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> List[str]:
        def backtrack(i, cur, res):
            if i == N:
                res.append(' '.join(cur))
                return res

            for j in range(i, N):
                substr = s[i: j + 1]
                if substr in word_set:
                    cur.append(substr)
                    res = backtrack(j + 1, cur, res)
                    cur.pop()

            return res

        N = len(s)
        word_set = set(word_dict)
        return backtrack(0, [], [])
