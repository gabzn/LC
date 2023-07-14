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

If the max size is 10^4, n^2 is the max you can do.
If the max size is 10^5, n^2 solution will not pass. The max you can do is nlog(n).
```

## ``How to convert a char into its ascii value and the opposite``
```
ord('a') -> 97
ord('a') - ord('a') = 0
chr(ord('a')) = 'a'
```

## ``How to check if a char is a digit or a letter``
char.isnumeric()   -> checks if a char is a digit/number

char.isalpha()    -> checks if a char is a letter

## ``How to sort an array by multiple values``
https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

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

Topological Traversal is just the reverse of Postorder Traversal. Postorder means visit all the children first then myself.
In the recursive dfs version, this is basically adding myself after the for loop.

    https://leetcode.com/problems/reconstruct-itinerary/
    https://www.youtube.com/watch?v=ddTC4Zovtbc

Kahn's algo for topo sort: 
    Step 1: Calculate the in-degree of all nodes
    Step 2: Put nodes with in-degree of 0 into a queue
    Step 3: Perform BFS. When going through the neighbours of those in-degree-0 nodes, decrement their in-degree by 1
        Step 3.1: If a neighbour's in-degree becomes 0, append it to queue.
    Step 4: Generally, when the queue is empty, we obtain a topo ordering. However, if a graph has cycle, we will not have a topo ordering.
            We also need to check if all nodes have in-degree of 0 to detect if there's a cycle.
            Alternatively, we can check how many nodes we have visited. If the number doesn't match the number of all nodes, there's a cycle.

    https://www.youtube.com/watch?v=h3_D5MomlVs
    https://leetcode.com/problems/find-eventual-safe-states/
    https://leetcode.com/problems/course-schedule/
    https://leetcode.com/problems/course-schedule-ii/

The difference between regular topo sort and Kahn's topo sort is that Kahn's topo sort must start with node with in-degree or 0.
Unlike the regular one which can stat with any node.
```

## ``Union Find & Minimum Spanning Tree``
Union find or disjoing set is a data structure to group data in sets. The most common way to implement union find is as below:
```
    def union(x, y):
        root_x, root_y = map(find, [x, y])
        if root_x == root_y:
            return
        root[root_y] = root_x

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

    https://leetcode.com/problems/min-cost-to-connect-all-points/
    https://leetcode.com/problems/optimize-water-distribution-in-a-village/
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

## ``Sliding Window``
Always a good idea to think of sliding window when the problem has keywords like <b>consecutive</b>, <b>contiguous</b>, <b>subarray</b> and <b>substring</b>, and the input is a string or array.

Also, if the problem has a requirement like pick x something from the list and the ordering doesn't matter, think about sorting the list then apply sliding window.

https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

https://leetcode.com/problems/fruit-into-baskets/

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

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

## ``DP``
Top-down (memoization) uses recursion. When try to solve a DP problem using this approach, there's usually a recursive function that does the work. Two things to think about before designing such a recursive function. 1: State variables (what we care about at the current step) and 2: what this recursive function returns. Example: if a question is asking for the max or min of performing some actions. The function can return the max or min when we are performing the i-th action where i is also the state variable.

Bottom-up (Tabulation) uses iteration. More 

## ``Something to look at later``
DFS + BFS

Union Find

Segment Tree

Prefix Sum

Matrix

Greedy

Subsequences & Substrings

Monotonic Queue

Top K

<s>Priority queue & Heap</s>

<s>Backtracking</s>

<s>Sliding Window</s>

<s>Binary Search</s>

<s>DP</s>
