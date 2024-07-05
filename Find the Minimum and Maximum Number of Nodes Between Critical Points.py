https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []
        index = 0
        prev = -1
        min_dis = inf
        max_dis = 0
        
        while head.next:
            if prev != -1:
                if (prev < head.val > head.next.val) or (prev > head.val < head.next.val):
                    critical_points.append(index)
                    if len(critical_points) >= 2:
                        min_dis = min(min_dis, critical_points[-1] - critical_points[-2])
                        max_dis = critical_points[-1] - critical_points[0]
                    
            prev = head.val
            head = head.next
            index += 1
        
        if len(critical_points) < 2:
            return [-1, -1]
        return [min_dis, max_dis]
