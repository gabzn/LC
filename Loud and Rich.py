https://leetcode.com/problems/loud-and-rich/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        answer = [_ for _ in range(N)]
        
        graph, indegrees = defaultdict(list), [0] * N
        for a, b in richer:
            graph[a].append(b)
            indegrees[b] += 1
        
        queue = deque()
        for idx, degree in enumerate(indegrees):
            if degree == 0:
                queue.append(idx)
        
        while queue:
            rich_person = queue.popleft()
            
            for poor_person in graph[rich_person]:    
                
                if quiet[answer[poor_person]] >= quiet[answer[rich_person]]:
                    answer[poor_person] = answer[rich_person]
                
                indegrees[poor_person] -= 1
                if indegrees[poor_person] == 0:
                    queue.append(poor_person)                

        return answer
