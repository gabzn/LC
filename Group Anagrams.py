Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

https://leetcode.com/problems/group-anagrams/  
  
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        
        anagram_dict = defaultdict(list)
        
        for s in strs:
            letter_count = [0] * 26
            
            # Find the letter count of each str, then use a dict to hash it.
            # If the same letter count already showed up, that means this str is an anagram with something else.
            for letter in s:
                letter_index = ord(letter) - ord('a')
                letter_count[letter_index] += 1
            
            # Since list is not hashable, we convert it to either a string or tuple to hash it.
            # Since defaultdict initializes empty lists for us, we don't need to do the if-statement here.
            letter_count_hashable = tuple(letter_count)
            anagram_dict[letter_count_hashable].append(s)
        
        return anagram_dict.values()
