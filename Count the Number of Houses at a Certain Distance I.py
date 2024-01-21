https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        def bfs(start):
            queue = deque([(start, 0)])
            visited = set([start])
            
            while queue:
                node, dis = queue.popleft()
            
                if dis != 0:
                    res[dis] += 1
                
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour, dis + 1))
            
        graph = defaultdict(list)
        
        for i in range(2, n + 1):
            graph[i].append(i-1)
            graph[i-1].append(i)
        
        if x != y:
            graph[x].append(y)
            graph[y].append(x)
        
        res = [0] * (n + 1)
        
        for i in range(1, n + 1):
            bfs(i)
        
        return res[1:]
-------------------------------------------------------------------------------------------------
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        distances = [[inf if i != j else 0 for j in range(n)] for i in range(n)]
        
        if x != y:
            distances[x - 1][y - 1] = 1
            distances[y - 1][x - 1] = 1
                  
        for i in range(2, n + 1):
            distances[i - 1][i - 2] = 1
            distances[i - 2][i - 1] = 1
        
        # Floyd-Warsall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
                                    
        res = [0] * n
        
        for dis in chain(*distances):
            if dis != 0:
                res[dis - 1] += 1
                
        return res
