https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        graph = self.make_graph(edges)
        leaves = []
        
        # Start with all the leaf nodes
        for node, neighbours in graph.items():
            if len(neighbours) == 1:
                leaves.append(node)
        
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            
            while leaves:
                leaf = leaves.pop()
                
                for neighbour in graph[leaf]:
                    graph[neighbour].remove(leaf)
                    
                    # Refer to line 11, this means the neighbour also becomes a leaf node.
                    if len(graph[neighbour]) == 1:
                        new_leaves.append(neighbour)
            
            leaves = new_leaves      
        return leaves
    
    def make_graph(self, edges):
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        return graph
