https://leetcode.com/problems/maximum-palindromes-after-operations/

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:        
        word_lens = []
        counter = Counter()
        for word in words:
            for char in word:
                counter[char] += 1
            
            word_lens.append(len(word))
        
        pairs = solos = 0
        for char, count in counter.items():
            # if char has even count, we use it in pairs unless we have no more solo to use
            pairs += (count // 2)
            solos += (count % 2)
        
        res = 0
        for word_len in sorted(word_lens):
            pairs_needed = word_len // 2
            solo_needed = word_len % 2
            
            if pairs_needed > pairs:
                break
            pairs -= pairs_needed
            
            # len is odd, we need to fill in the middle
            # if we don't have any more solos to fill the middle, break 1 pair into 2 solos
            if solo_needed > solos:
                pairs -= 1
                solos += 2
            
            solos -= solo_needed
            res += 1

        return res
