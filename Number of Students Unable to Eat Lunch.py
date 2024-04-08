https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        N = len(students)
        
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        while students:
            sandwich_preference = students.popleft()
            if sandwiches and sandwich_preference == sandwiches[0]:
                sandwiches.popleft()
            else:
                students.append(sandwich_preference)
            
            if not sandwiches or sandwiches[0] not in students:
                break
            
        return len(students)
