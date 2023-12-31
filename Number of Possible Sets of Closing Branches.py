https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

class Solution:
    def numberOfSets(self, n: int, max_distance: int, roads: List[List[int]]) -> int:
        """
        Go through every combination of open and closed branches
        If the current combination is 101, we want to know if closing branch 1 and keeping branch 0 and 2 open is a valid solution
        """        
        def is_good_subset(mask):
            distances = [[math.inf if i != j else 0 for j in range(n)] for i in range(n)]
            
            # Copy the distances for branches that we keep open
            for start in range(n):
                if mask & (1 << start):
                    for end in range(n):
                        if mask & (1 << end):
                            distances[start][end] = matrix[start][end]
            
            # Floyd-Warsall
            for through in range(n):
                for start in range(n):
                    for end in range(n):
                        distances[start][end] = min(distances[start][end], distances[start][through] + distances[through][end])
            
            # Check the open stores to see if their distances are more than max_distance
            for start in range(n):
                if mask & (1 << start):
                    for end in range(n):
                        if mask & (1 << end) and distances[start][end] > max_distance:
                            return False
                            
            return True       
        
        matrix = [[math.inf if i != j else 0 for j in range(n)] for i in range(n)]
        for u, v, w in roads:
            matrix[u][v] = min(matrix[u][v], w)
            matrix[v][u] = min(matrix[v][u], w)                
        
        res = 0
        for mask in range(1 << n):
            if is_good_subset(mask):
                res += 1
        
        return res
