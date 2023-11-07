https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        @cache
        def dp(node, divisions, parent):   
            # Return early if there is already more than 13 divs
            if divisions >= 13:
                return 0
            
            # Compute how many coins are left in current node
            coin = math.floor(coins[node] / (2 ** divisions))
            
            minus_k = coin - k                    # Collect coin on current node using the first approach
            divide_by_two = math.floor(coin / 2)  # Collect coin on current node using the second approach

            # Base case where the current node is a leaf node
            if len(graph[node]) == 1 and graph[node][0] == parent:
                return max(minus_k, divide_by_two)

            # Collect children's coins
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                
                minus_k += dp(neighbour, divisions, node)
                divide_by_two += dp(neighbour, divisions + 1, node)
                            
            return max(minus_k, divide_by_two)
        
        return dp(0, 0, -1)
