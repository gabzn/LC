https://leetcode.com/problems/analyze-user-website-visit-pattern/

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_to_websites = defaultdict(list)
        for user, time, webpage in sorted(zip(username, timestamp, website), key=lambda x: x[1]):
            user_to_websites[user].append(webpage)
        """
        bob: a b c d e
        
        a b c
        a b d
        """
        counter = defaultdict(int)
        for user, webpages in user_to_websites.items():
            patterns = set()
            
            # Generate every combination of size 3 for a particular user
            size = len(webpages)
            for first in range(size):
                for second in range(first + 1, size):
                    for third in range(second + 1, size):
                        pattern = (webpages[first], webpages[second], webpages[third])
                        patterns.add(pattern)
            
            for pattern in patterns:
                counter[pattern] += 1
        
        max_score = 0
        max_pattern = None
        for pattern, score in counter.items():
            if (score > max_score) or (score == max_score and pattern < max_pattern):
                max_score = score
                max_pattern = pattern

        return max_pattern
--------------------------------------------------------------------------------------------------------------
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_to_websites = defaultdict(list)
        for user, time, webpage in sorted(zip(username, timestamp, website), key=lambda x: x[1]):
            user_to_websites[user].append(webpage)
        """
        bob: a b c d e
        
        a b c
        a b d        
        """
        counter = defaultdict(int)
        for user, webpages in user_to_websites.items():
            for pattern in set(combinations(webpages, 3)):
                counter[pattern] += 1

        max_score = 0
        max_pattern = None
        for pattern, score in counter.items():
            if (score > max_score) or (score == max_score and pattern < max_pattern):
                max_score = score
                max_pattern = pattern

        return max_pattern
