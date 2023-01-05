https://leetcode.com/problems/distant-barcodes/
# Same as  https://leetcode.com/problems/reorganize-string/
  
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = collections.Counter(barcodes)
        max_heap = [(-count, barcode) for barcode, count in counter.items()]
        heapify(max_heap)
        
        res = []
        while max_heap:
            placeholder = []
            
            pop_times = min(2, len(max_heap))
            for _ in range(pop_times):
                count, barcode = heappop(max_heap)
                
                res.append(barcode)
                count += 1
                if count:
                    placeholder.append((count, barcode))
                
            for count, barcode in placeholder:
                heappush(max_heap, (count, barcode))
            
        return res
