https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        res = []
        in_degree, safe_nodes = [0 for _ in range(N)], [False for _ in range(N)]
        queue, adjacency_list = deque(), defaultdict(list)
        
        """
        The intuition is we want to start from the safe nodes
        and perform topo sort on the safe nodes
        
        Safe nodes have no outgoing edges. We can reverse that by thinking
        all incoming edges are actually the outgoing edges.
        """
        # Compute the reverse in-degree of all nodes
        for from_node, edge in enumerate(graph):
            for to_node in edge:
                in_degree[from_node] += 1
                adjacency_list[to_node].append(from_node)
                
        # Put all nodes with in-degree of 0 into the queue
        for node, degree in enumerate(in_degree):
            if degree == 0:
                queue.append(node)
        
        # Begin Khan's topo sort
        while queue:
            node = queue.popleft()
            safe_nodes[node] = True
            
            for neighbour in adjacency_list[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        
        for node, is_safe in enumerate(safe_nodes):
            if is_safe:
                res.append(node)
                
        return res
