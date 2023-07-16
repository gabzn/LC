https://leetcode.com/problems/alien-dictionary/
https://www.youtube.com/watch?v=tN6YETIiaqw

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        res, indegrees = [], [0] * 26
        queue = deque()
        adj_list = dict()
        
        # Initialize the dict with chars in words
        for word in words:
            for char in word:
                adj_list[char] = set()
                
        # Build the adj list and indegrees
        for index in range(1, len(words)):
            word1, word2 = words[index - 1], words[index]
            is_different, char1, char2 = self.return_first_different_chars_if_true(word1, word2)
            
            if is_different:
                if char2 not in adj_list[char1]:
                    adj_list[char1].add(char2)
                    indegrees[ord(char2) - ord('a')] += 1
            else:
                if len(word1) > len(word2):
                    return ""
                
        # Put chars that have indegree of 0 into the queue
        for char in adj_list:
            if indegrees[ord(char) - ord('a')] == 0:
                queue.append(char)
        
        # Perform Khan's algorithm to get topo ordering
        while queue:
            char = queue.popleft()
            res.append(char)
            
            for neighbour in adj_list[char]:
                indegrees[ord(neighbour) - ord('a')] -= 1
                if indegrees[ord(neighbour) - ord('a')] == 0:
                    queue.append(neighbour)
        
        return ''.join(res) if len(res) == len(adj_list) else ''
        
    def return_first_different_chars_if_true(self, word1, word2):
        length = min(len(word1), len(word2))
        
        for index in range(length):
            char1, char2 = word1[index], word2[index]
            if char1 != char2:
                return True, char1, char2
        
        return False, None, None
