https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        remaining_nodes = n
        res = 0
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited_nodes = set()
        for node in range(n):
            if node in visited_nodes:
                continue
            
            num_nodes_in_current_component = 1
            
            visited_nodes.add(node)
            stack = [node]
            while stack:
                cur_node = stack.pop()
                
                for next_node in graph[cur_node]:
                    if next_node in visited_nodes:
                        continue
                    
                    visited_nodes.add(next_node)
                    stack.append(next_node)
                    num_nodes_in_current_component += 1
                    
            remaining_nodes -= num_nodes_in_current_component
            res += num_nodes_in_current_component * (remaining_nodes)
            
        return res
