https://leetcode.com/problems/binary-search-tree-iterator/

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.current = root
        
    def next(self) -> int:
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left
        
        node = self.stack.pop()
        val = node.val
        self.current = node.right
        return val
        
    def hasNext(self) -> bool:
        return self.stack or self.current
