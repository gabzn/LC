https://leetcode.com/problems/find-center-of-star-graph/
  
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        We just need to look at the first 2 pairs of edges to 
        determine the center node.
        
        Find the node that shows up in both pairs.
        """
        first_pair = edges[0]
        second_pair = edges[1]
        
        for num_1 in first_pair:
            for num_2 in second_pair:
                if num_1 == num_2:
                    return num_1
