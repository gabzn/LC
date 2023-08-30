https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def make_graph(node, parent=None):
            if parent:
                graph[node.val].add(parent.val)
                
            if node.left:
                graph[node.val].add(node.left.val)
                make_graph(node.left, node)
                
            if node.right:
                graph[node.val].add(node.right.val)
                make_graph(node.right, node)
            
        graph = defaultdict(set)
        make_graph(root)
        
        res = 0
      
        visited_nodes = set([start])        
        queue = deque([(start, 0)])
        while queue:
            LEN = len(queue)
            
            for _ in range(LEN):
                node, time = queue.popleft()
                res = time
                
                for neighbour in graph[node]:
                    if neighbour in visited_nodes:
                        continue    
                    visited_nodes.add(neighbour)
                    queue.append((neighbour, time + 1))
            
        return res
