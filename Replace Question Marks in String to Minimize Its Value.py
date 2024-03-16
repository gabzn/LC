https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        counter = Counter(s)
        heap = []
        
        for char in string.ascii_lowercase:
            heappush(heap, (counter[char], char))
        
        queue = []
        for char in s:
            if char == "?":
                count, char_to_replace_question_mark = heappop(heap)
                heappush(heap, (count + 1, char_to_replace_question_mark))                
                queue.append(char_to_replace_question_mark)
        
        queue.sort()
        queue = deque(queue)
        res = []
        
        for char in s:
            if char == "?":
                res.append(queue.popleft())
            else:
                res.append(char)
        
        return ''.join(res)
