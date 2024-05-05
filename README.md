## ``Input Size & Time Complexity``
Given the input size, what's the highest complexity of your algorithm could run?
Any algorithm runs more than the indicated range will give a **time limit exceeded** error.
```
1 - 10      -> n!   -> Permutation
1 - 20      -> 2^n  -> Combination
10 - 50     -> n^4
100 - 200   -> n^3
100 - 10000  -> n^2  -> Very common
1000 - 10^5 -> nlog(n) 
1000 - 10^7 -> n
```

## ``How to convert a char into its ascii value and the opposite``
```python
ord('a') -> 97
ord('a') - ord('a') = 0
chr(ord('a')) = 'a'
```

## ``Quick way to flatten a nested-list in Python``
```python
import itertools

to_flatten = [[1,2,3],[4,5,6],[7,8,9]]
flattened = list(itertools.chain(*lst))
flattened -> [1,2,3,4,5,6,7,8,9]
```

## ``How to implement custom str comparator``
```
https://leetcode.com/problems/largest-number/
```

## ``How to check if a char is a digit or a letter``
```python
char.isnumeric()   # checks if a char is a digit/number
char.isalpha()     # checks if a char is a letter
```

## ``How to sort an array by multiple values``
```
https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
```

## ``How to deal with tricky bounds in indexing``
```
https://leetcode.com/problems/total-cost-to-hire-k-workers/
https://leetcode.com/problems/stone-game-ii/
```

## ``DFS & BFS``
DFS uses a stack & BFS uses a queue

For graphs, there are preorder DFS, postorder DFS and topological traversals. 
```
Preorder DFS Traversal:
    1: Visit current node
    2: Visit neighbour nodes

Postorder DFS Traversal:
    1: Visit neighbour nodes
    2: Visit current node
```

Topological Traversal is just the reverse of Postorder Traversal. Postorder means visit all the children first then myself.
In the recursive dfs version, this is basically adding myself after the for loop.

```
https://leetcode.com/problems/reconstruct-itinerary/
https://www.youtube.com/watch?v=ddTC4Zovtbc
```

Kahn's algo for topo sort: 
```
    Step 1: Calculate the in-degree of all nodes
    Step 2: Put nodes with in-degree of 0 into a queue
    Step 3: Perform BFS. When going through the neighbours of those in-degree-0 nodes, decrement their in-degree by 1
        Step 3.1: If a neighbour's in-degree becomes 0, append it to queue.
    Step 4: Generally, when the queue is empty, we obtain a topo ordering. However, if a graph has cycle, we will not have a topo ordering.
            We also need to check if all nodes have in-degree of 0 to detect if there's a cycle.
            Alternatively, we can check how many nodes we have visited. If the number doesn't match the number of all nodes, there's a cycle.
```
```
https://www.youtube.com/watch?v=h3_D5MomlVs
https://leetcode.com/problems/find-eventual-safe-states/
https://leetcode.com/problems/course-schedule/
https://leetcode.com/problems/course-schedule-ii/
```

The difference between regular topo sort and Kahn's topo sort is that Kahn's topo sort must start with node with in-degree or 0.
Unlike the regular one which can stat with any node.


BFS/DFS + Binary Search:

```
https://leetcode.com/problems/path-with-minimum-effort/
https://leetcode.com/problems/find-the-safest-path-in-a-grid/
```

Multi-source BFS + (A very good explanation of MS-BFS): 
    
    https://leetcode.com/problems/as-far-from-land-as-possible/discuss/2515617/How-to-solve-multi-source-BFS-problems.-Intuition

```
https://leetcode.com/problems/find-the-safest-path-in-a-grid/
https://leetcode.com/problems/walls-and-gates/
https://leetcode.com/problems/shortest-bridge/
https://leetcode.com/problems/number-of-enclaves/
https://leetcode.com/problems/rotting-oranges/
https://leetcode.com/problems/as-far-from-land-as-possible/
https://leetcode.com/problems/map-of-highest-peak/
https://leetcode.com/problems/01-matrix/
https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
```

## ``Union Find``
Union find or disjoing set is a data structure to group data in sets. The most common way to implement union find is as below:

Union by rank:
```
    def union_by_rank(x, y):
        root_x, root_y = map(find, [x, y])
        if root_x == root_y:
            return
        if rank[root_x] < rank[root_y]:
            root[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            root[root_y] = root_x
        else:
            root[root_y] = root_x
            rank[root_x] += 1

    def find(x):
        if root[x] != x:
            root[x] = find(root[x])
        return root[x]

    root = [index for index in range(NUMBER OF NODES)]
    rank = [1 for _ in range(NUMBER OF NODES)]
```

Regular union:
```
    def union(x, y):
        root_x, root_y = map(find, [x, y])
        if root_x == root_y:
            return
        root[root_y] = root_x

    def find(x):
        if root[x] != x:
            root[x] = find(root[x])
        return root[x]
```

## ``Minimum Spanning Tree``

A Minimum Spanning Tree (MST) is a subset of a <b>`weighted undirected graph`</b> which connects all <b>`nodes`</b> with the minimal total edge cost.

There are two well-known algorithms to construct a MST:
    1. Kruskal's algorithm
    2. Prim's algorithm

Kruskal's algo uses <b>Union-Find</b> to find whether two nodes are already connected or not. The general implementation of Kruskal's algo:
```
    1: Sort the edges by their weights in ascending order.
    2: Go through the sorted edges and merge nodes into the MST if no cycles would be produced by using the Union function in Union-Find.
        2.1: Typically, the Union function would return True/False to indicate if two nodes are already connected.
        2.2: If False, that means adding the current edge would produce a cycle. Skip the current edge.
        2.3: If True, adding the current edge would not create a cycle. Use the current edge.
    3: Repeat step 2 until (NUMBER OF NODES - 1) edges are added.
```

```
https://leetcode.com/problems/min-cost-to-connect-all-points/
https://leetcode.com/problems/optimize-water-distribution-in-a-village/
```


## Single-Source Weighted Shortest Path - Dijkstra
Recall regular BFS can find the shortest path between two nodes <b>`WHEN THERE'S NO WEIGHT`</b> in the graph. When there's positive weight in the graph, we have to use Dijkstra.

```
What does single source mean? Single source means we want to know the distance from one specific node to another specific node.
Dijkstra uses a heap to find the next least-weight unvisited path. Usually, we maintain another list to compare the weights.
```

```
https://leetcode.com/problems/network-delay-time/
https://leetcode.com/problems/path-with-maximum-probability/
https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/
https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
https://leetcode.com/problems/minimum-cost-to-convert-string-i/
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/
https://leetcode.com/problems/find-edges-in-shortest-paths/
```

## ``Heap / Priority Queue``
A heap is a tree based data structure that satisfies the heap property. Trees cannot contain cycles. Therefore, heaps cannot contain cycles too.

2 types of heaps:

    Max Heap
    Min Heap

Although it's very common to see heap being binary, it's not always the case.

Priority queues are abstract data structures meaning it can be implemented by multiple data structures. The most common way is implemented using a heap.

    1: It could be implemented using just a queue. However, for each insertion, a sorting will take place to ensure the priority is correct.
    2: It could also be implemented using a heap. A heap will adjust the priority automatically using bubble up/down after each insertion.

```
A few things to learn from this one: https://leetcode.com/problems/total-cost-to-hire-k-workers/
    1: How to initialize lists with [:index] and [index:] syntax

    2: How to initialize variables if there's possibility of out of bound

    3: How to deal with double counting when dealing with pointers  

A very interesting use of heap: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
```

## All Pairs Shortest Paths - Floyd-Warsall
Recall Dijkstra is the best algorithm when we want to find the shortest distances from 1 node to all others. What if now we want to find the shortest distances from every single node to every other nodes?

Theoretically, we can run Dijkstra on every single node and let it compute the shortest distances from every single node to every others, but that'll be very expensive.

Alternatively, we can use Floyd-Warsall algorithm, which can compute the shortest distances for every single pair of nodes. 

The general idea of Floyd-Warsall is try to see if using some intermediate nodes will get us the shorter distances from <b>`i`</b> to <b>`j`</b>.

```
https://www.youtube.com/watch?v=0dTrKG5UK9k

Say we have n nodes, and we want to use Floyd-Warsall to compute the APSP.
        
    1: distances = [[math.inf if i != j else 0 for j in range(n)] for i in range(n)] where distances[i][j] denotes the shortest distance from i to j.
    2: Oftentimes, we are given some initial weights. We go through them and initialize `distances`.
    3: for k in range(n):
        for i in range(n):
         for j in range(n):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    What these nested for loops are saying is we want to know if going from i to j through k will result in a shorter distance. 
```

```
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
https://leetcode.com/problems/minimum-cost-to-convert-string-i/
https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/
```

## ``Sliding Window``
Always a good idea to think of sliding window when the problem has keywords like <b>consecutive</b>, <b>contiguous</b>, <b>subarray</b> and <b>substring</b>, and the input is a string or array.

Also, if the problem has a requirement like pick x something from the list and the ordering doesn't matter, think about sorting the list then apply sliding window.

```
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
https://leetcode.com/problems/fruit-into-baskets/
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
```

## ``Binary Search Stuff``
https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems

https://www.youtube.com/watch?v=JuDAqNyTG4g&t=483s

https://www.youtube.com/watch?v=tgVSkMA8joQ

A template for binary search for lower bound or upper bound:
```python
l, r = -1, len(nums)

while l + 1 != r:
    based on some condition:
        l = m
    else:
        r = m

return either l or r
```

```
https://leetcode.com/problems/fair-distribution-of-cookies/
https://leetcode.com/problems/divide-chocolate/
https://leetcode.com/problems/split-array-largest-sum/
https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
```

## ``DP``
Top-down (memoization) uses recursion. When try to solve a DP problem using this approach, there's usually a recursive function that does the work. Two things to think about before designing such a recursive function. 1: State variables (what we care about at the current step) and 2: what this recursive function returns. Example: if a question is asking for the max or min of performing some actions. The function can return the max or min when we are performing the i-th action where i is also the state variable.

Interval dp problems:
```
https://leetcode.com/problems/maximize-the-profit-as-the-salesman/
https://leetcode.com/problems/maximum-earnings-from-taxi/
https://leetcode.com/problems/maximum-profit-in-job-scheduling/
https://leetcode.com/problems/video-stitching/                                             (greedy/dp)
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/            (greedy/dp)
```

## ``Game Theory (Turn by turn based)``
```
https://leetcode.com/problems/predict-the-winner/
https://leetcode.com/problems/stone-game/
```

## ``Mono stack``
Next smaller or previous smaller -> Increasing stack (Becasue when you see an element that is smaller than the top element in the stack, this element is the next smaller of the top element)

Next larger or previous larger -> Decreasing stack (Becasue when you see an element that is larger than the top element in the stack, this element is the next larger of the top element)

```
https://leetcode.com/problems/sum-of-subarray-minimums/
https://leetcode.com/problems/sum-of-subarray-ranges/
```

## ``Subsequence or substring questions that needs to MOD 10**9 + 7``
```
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
```

## ``A good question to look at to count the number of pairs that needs to meet some condition like i < j``
```
https://leetcode.com/problems/number-of-good-pairs/
```

## ``Combinatorics``
```
https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
```

## ``Tree DP``
```
https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/
https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/
```

## ``Knapsack / Pick or skip``
```
https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/
https://leetcode.com/problems/minimum-number-of-coins-for-fruits/
```

## ``Something to look at later``
DP

Monotonic Queue

Monotonic Stack

Backtracking

Permutation

Combination

Prefix Sum

Greedy

Subsequences & Substrings

Top K

Simulation

Segment Tree

<s>Priority queue & Heap</s>

<s>Sliding Window</s>

<s>Binary Search</s>

<s>Union Find</s>

<s>DFS + BFS</s>
