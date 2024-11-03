https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

class Solution:
    def minTimeToReach(self, move_time: List[List[int]]) -> int:
        def is_valid(x, y):
            return 0 <= x < N and 0 <= y < M

        N = len(move_time)
        M = len(move_time[0])
        DIRECTIONS = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        
        time = [[inf] * M for _ in range(N)]
        time[0][0] = 0

        heap = [(0, 0, 0)]
        while heap:
            current_time, x, y = heappop(heap)
            if x == N - 1 and y == M - 1:
                return current_time
            if current_time > time[x][y]:
                continue

            for offset_x, offset_y in DIRECTIONS:
                next_x, next_y = x + offset_x, y + offset_y
                if is_valid(next_x, next_y):
                    arrival_time = max(current_time, move_time[next_x][next_y]) + 1

                    if arrival_time < time[next_x][next_y]:
                        time[next_x][next_y] = arrival_time
                        heappush(heap, (arrival_time, next_x, next_y))
