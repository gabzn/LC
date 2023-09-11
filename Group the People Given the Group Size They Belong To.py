https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        groups = defaultdict(list)
        
        for index, group_size in enumerate(groupSizes):
            group = groups[group_size]
            group.append(index)
            
            if len(group) == group_size:
                res.append(group[:])
                del groups[group_size]
  
        return res
