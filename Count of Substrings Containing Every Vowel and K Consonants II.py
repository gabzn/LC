https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:        
        def count(t):        
            v_count = defaultdict(int)
            c_count = 0
            left = res = 0

            for right in range(N):
                char = word[right]
                if char in VOWELS:
                    v_count[char] += 1
                else:
                    c_count += 1

                while len(v_count) == 5 and c_count >= t:
                    char = word[left]
                    if char in VOWELS:
                        v_count[char] -= 1
                        if v_count[char] == 0:
                            del v_count[char]
                    else:
                        c_count -= 1
                    
                    left += 1
                
                res += left

            return res

        N = len(word)
        VOWELS = ['a', 'e', 'i', 'o', 'u']
        
        #  (at least 30) - (at least 31) = exactly 30
        return count(k) - count(k + 1)
