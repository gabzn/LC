https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        def get_words_differed_by_one(word, i):
            chars = [char for char in word]
            next_words = []
            for letter in lowercase_letters:
                if chars[i] == letter:
                    continue
                chars[i] = letter
                next_words.append(''.join(chars))
            return next_words
        
        lowercase_letters = string.ascii_lowercase
        word_set = set(word_list)
        queue = deque([(begin_word, 1)])

        while queue:
            for _ in range(len(queue)):
                cur_word, l = queue.popleft()
                if cur_word == end_word:
                    return l
                
                # Go through each char in cur_word, and change that char to all other english letters
                for i in range(len(cur_word)):
                    next_words = get_words_differed_by_one(cur_word, i)

                    for next_word in next_words:
                        if next_word in word_set:
                            queue.append((next_word, l + 1))
                            word_set.remove(next_word)

        return 0
