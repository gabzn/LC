https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        counter_sorted_by_freq = sorted(counter.items(), key=lambda p: p[1])
        
        for num, count in counter_sorted_by_freq:
            t = min(count, k)
            
            count -= t
            if count == 0:
                del counter[num]
                
            k -= t
            if k == 0:
                break
            
        return len(counter)
