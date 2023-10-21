https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        children = set()
        
        for idx in range(n):
            left = leftChild[idx]
            right = rightChild[idx]
            
            if left != -1:
                children.add(left)
            
            if right != -1:
                children.add(right)
        
        if len(children) != n - 1:
            return False
        
        # Find the root node. The root node will not be in the children set.
        root = -1
        for node in range(n):
            if node not in children:
                root = node
                break
        
        # Do a dfs to visit all nodes
        visited_nodes = set()
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node in visited_nodes:
                return False
            visited_nodes.add(node)
            
            if leftChild[node] != -1:
                stack.append(leftChild[node])
            
            if rightChild[node] != -1:
                stack.append(rightChild[node])
                
        return len(visited_nodes) == n
