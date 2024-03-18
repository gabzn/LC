https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(employee_id):        
            res = graph[employee_id].importance
            for subordinate in graph[employee_id].subordinates:
                res += dfs(subordinate)
            return res
        
        graph = {}
        for employee in employees:
            graph[employee.id] = employee
        return dfs(id)
