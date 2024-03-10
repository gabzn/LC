https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        def generate_sub_strings(idx, string):
            LEN = len(string)
            for i in range(LEN):
                sub_string = ''
                for j in range(i, LEN):
                    sub_string += string[j]
                    sub_strings[idx].append(sub_string)
                        
        N = len(arr)
        
        # Generate all substrings for a given string and sort all substrings based on length
        sub_strings = [[] for _ in range(N)]
        for index, string in enumerate(arr):
            generate_sub_strings(index, string)
            sub_strings[index].sort(key=lambda p: (len(p), p))
        
        # For each string, store all substrings of other strings
        sub_strings_in_others = [set() for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                    
                for sub_string in sub_strings[j]:
                    sub_strings_in_others[i].add(sub_string)
        
        # Go through each substring of a string, and if that substring doesn't exist in others, it's an answer
        res = ["" for _ in range(N)]
        for index, sub_string in enumerate(sub_strings):
            for sub in sub_string:
                if sub not in sub_strings_in_others[index]:
                    res[index] = sub
                    break
                    
        return res
