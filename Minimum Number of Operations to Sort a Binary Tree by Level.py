https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        res = 0

        queue = deque([root])
        while queue:
            current_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            indices = {num: i for i, num in enumerate(current_level)}
            current_level_sorted = sorted(current_level)
            
            for i in range(len(current_level)):
                c = current_level[i]
                s = current_level_sorted[i]
                
                # c is in s position. Find s in current_level and swap them.
                if c != s:
                    s_index_in_current_level = indices[s]
                    current_level[i], current_level[s_index_in_current_level] = current_level[s_index_in_current_level], current_level[i]
                    indices[c] = s_index_in_current_level
                    indices[s] = i
                    res += 1

        return res
