https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/description/

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpet_len: int) -> int:
        tiles.sort()
        res = 1
        left = 0
        total_cover_areas = 0

        for right, [start, end] in enumerate(tiles):
            total_cover_areas += (end - start + 1)

            # Find where the carpent left is at.
            # If carpent left doesn't cover any tiles, we move the left pointer.
            # We also subtract any previous cover area from the total
            carpent_left = end - carpet_len + 1
            while carpent_left > tiles[left][1]:
                total_cover_areas -= (tiles[left][1] - tiles[left][0] + 1)
                left += 1

            # We know carpent covers something now. 
            # It can still cover some part of the tiles from previous block.
            # Every tile left to carpent_left is now uncovered.
            uncovered_areas = max(carpent_left - tiles[left][0], 0)
            res = max(res, total_cover_areas - uncovered_areas)

        return res
