https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)
        
        root = None
        for v, lst in graph.items():
            if len(lst) == 1:
                root = v
                break
        
        res = []
        stack = [(root, root)]
        while stack:
            node, parent = stack.pop()
            res.append(node)
            
            for neighbour in graph[node]:
                if neighbour != parent:
                    stack.append((neighbour, node))
                
        return res
