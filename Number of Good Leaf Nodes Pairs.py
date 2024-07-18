https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            if not node.left and not node.right:
                leaves.append(node)
            build_graph(node.left, node)
            build_graph(node.right, node)
        
        def dfs(node, prev, step):
            if not node.left and not node.right and step != 0 and step <= distance:
                res[0] += 1
                return
            if step > distance:
                return
            for n in graph[node]:
                if n != prev:
                    dfs(n, node, step + 1)
            
        graph = defaultdict(list)
        leaves = []
        build_graph(root, None)
        
        res = [0]
        
        for leaf in leaves:
            dfs(leaf, leaf, 0)
        
        return res[0] // 2
