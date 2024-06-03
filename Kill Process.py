https://leetcode.com/problems/kill-process/

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children = defaultdict(list)
        for child, parent in zip(pid, ppid):
            children[parent].append(child)
        
        res = []
        stack = [kill]
        while stack:
            p = stack.pop()
            res.append(p)
            
            for child in children[p]:
                stack.append(child)
        
        return res
