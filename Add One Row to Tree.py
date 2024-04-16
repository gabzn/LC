https://leetcode.com/problems/add-one-row-to-tree/

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val, left=root)
        
        queue = deque([(root, 1)])        
        while queue:
            cur_level = -1
            
            for _ in range(len(queue)):
                node, level = queue.popleft()
                cur_level = level
                
                if cur_level == depth - 1:
                    left_child = None
                    right_child = None
                    if node.left:
                        left_child = node.left
                    if node.right:
                        right_child = node.right

                    new_left_child = TreeNode(val=val, left=left_child)
                    new_right_child = TreeNode(val=val, right=right_child)
                    node.left = new_left_child
                    node.right = new_right_child
                else:
                    if node.left:
                        queue.append((node.left, level + 1))
                    if node.right:
                        queue.append((node.right, level + 1))
            
            if cur_level == depth - 1:
                break
        
        return root
