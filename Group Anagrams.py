Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

https://leetcode.com/problems/group-anagrams/  
  
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        
        # anagrams = []
        
        # Go through each str to find the letter count
        anagram_dict = dict()
        for each_str in strs:
            letter_count = [0] * 26
            for letter in each_str:
                letter_count[ord(letter) - ord('a')] += 1
            
            letter_count_tuple = tuple(letter_count)
            
            # Use a dict to check if this combination already exists
            #     1: If it exists, that means they are anagrams and put them in a list.
            #     2: If it doesn't exist, that means it's not an anagram with any str.
            if letter_count_tuple not in anagram_dict:
                anagram_dict[letter_count_tuple] = [each_str]
            else:
                anagram_dict[letter_count_tuple].append(each_str)
        
        # for value in anagram_dict.values():
        #     anagrams.append(value)
                
        return anagram_dict.values()
