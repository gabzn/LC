https://leetcode.com/problems/single-threaded-cpu/
  
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:        
        for index, task in enumerate(tasks):
            task.append(index)
        tasks.sort(key=lambda task: task[0], reverse=True)
        
        processing_heap, order = [], []
        
        # You don't need to set cur_time to 0 and then increment it by 1.
        # Just set cur_time to the enqueue time of the first task.
        cur_time = tasks[-1][0]
        
        # If either the heap or tasks still has more tasks to process
        while processing_heap or tasks:
            
            # If the current time >= the current enqueue time, that means the current task can be processed now.
            while tasks and cur_time >= tasks[-1][0]:
                _, processing_time, index = tasks.pop()        
                heapq.heappush(processing_heap, (processing_time, index))
                
            """
            Two scenarios could happen.
            1: If there's a task in the heap, process it by adding the processing_time to cur_time and append it to the order list.
            2: There's no tasks in the heap, meaning the next task hasn't arrived yet. We fast-forward to the next task. The reason we can't do cur_time += 1 is we don't know when the next task is going to arrive. It could arrive 1M seconds later.
            """
            if processing_heap:
                processing_time, index = heapq.heappop(processing_heap)
                cur_time += processing_time
                order.append(index)
            else:
                cur_time = tasks[-1][0]
          
        return order
