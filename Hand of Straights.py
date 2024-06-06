https://leetcode.com/problems/hand-of-straights/

class Solution:
    def isNStraightHand(self, hand: List[int], size: int) -> bool:
        N = len(hand)

        if N % size > 0:
            return False

        counter = Counter(hand)
        heap = list(counter.keys())
        heapify(heap)

        while heap:
            start = heap[0]

            for x in range(start, start + size):
                if counter[x] == 0:
                    return False

                counter[x] -= 1
                if counter[x] == 0:
                    if x != heap[0]:
                        return False

                    heappop(heap)

        return True
