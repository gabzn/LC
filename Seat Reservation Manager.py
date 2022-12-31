https://leetcode.com/problems/seat-reservation-manager/
  
class SeatManager:

    def __init__(self, n: int):
        self.heap = [index + 1 for index in range(n)]

    def reserve(self) -> int:
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
