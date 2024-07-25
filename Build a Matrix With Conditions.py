https://leetcode.com/problems/build-a-matrix-with-conditions/

class Solution:
    def buildMatrix(self, k: int, row_conditions: List[List[int]], col_conditions: List[List[int]]) -> List[List[int]]:
        def get_topo_ordering(conditions):
            indegrees = [0] * (k + 1)
            graph = defaultdict(list)
            for a, b in conditions:
                indegrees[b] += 1
                graph[a].append(b)
            
            queue = deque()
            for i in range(1, k + 1):
                if indegrees[i] == 0:
                    queue.append(i)
            
            topo_ordering = []
            while queue:
                node = queue.popleft()
                topo_ordering.append(node)
                
                for neighbour in graph[node]:
                    indegrees[neighbour] -= 1
                    if indegrees[neighbour] == 0:
                        queue.append(neighbour)
            return topo_ordering
        
        row_ordering = get_topo_ordering(row_conditions)
        col_ordering = get_topo_ordering(col_conditions)
        if len(row_ordering) != k or len(col_ordering) != k:
            return []
        
        row_position = {val: idx for idx, val in enumerate(row_ordering)}
        col_position = {val: idx for idx, val in enumerate(col_ordering)}
        res = [[0] * k for _ in range(k)]
        for val in row_position:
            i = row_position[val]
            j = col_position[val]
            res[i][j] = val
        return res
