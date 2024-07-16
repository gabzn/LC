https://leetcode.com/problems/find-distance-in-a-binary-tree/

class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def dfs(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            dfs(node.left, node)
            dfs(node.right, node)
        
        def find(x, y):
            queue = deque([(x, 0)])
            visited = set([x])
            
            while queue:
                node, d = queue.popleft()
                if node == y:
                    return d
                
                for n in graph[node]:
                    if n not in visited:
                        visited.add(n)
                        queue.append((n, d + 1))
        
        graph = defaultdict(list)
        dfs(root, None)        
        return find(p, q)
