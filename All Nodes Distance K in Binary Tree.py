https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        
        # Recursively build the undirected graph from the given binary tree.
        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur) 
        build_graph(root, None)
        
        res = []
        visited_nodes = set()
        
        stack = [(target.val, 0)]
        while stack:
            val, distance = stack.pop()
            if val in visited_nodes:
                continue
            visited_nodes.add(val)            
            
            if distance == k:
                res.append(val)
                
            for neighbour in graph[val]:
                stack.append((neighbour, distance + 1))
         
        return res
