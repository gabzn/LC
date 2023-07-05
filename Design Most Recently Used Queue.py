https://leetcode.com/problems/design-most-recently-used-queue/

class MRUQueue:

    def __init__(self, n: int):
        self.list = [num for num in range(1, n + 1)]
        
    def fetch(self, k: int) -> int:
        target = self.list.pop(k-1)
        self.list.append(target)
        return target
