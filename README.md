## ``Input Size & Time Complexity``
Given the input size, what's the highest complexity of your algorithm could run?
Any algorithm runs more than the indicated range will give a **time limit exceeded** error.

1 - 10      -> n!   -> Permutation

1 - 20      -> 2^n  -> Combination

10 - 50     -> n^4

100 - 200   -> n^3

100 - 10000  -> n^2  -> Very common

1000 - 10^5 -> nlog(n) 

1000 - 10^7 -> n

If the max size is 10^4, n^2 is the max you can do.

If the max size is 10^5, n^2 solution will not pass. The max you can do is nlog(n).

## ``How to convert a char into its ascii value and the opposite``
ord('a') -> 97

ord('a') - ord('a') = 0

chr(ord('a')) = 'a'


## ``How to check if a char is a digit or a letter``
char.isnumeric()   -> checks if a char is a digit/number

char.isalpha()    -> checks if a char is a letter

## ``How to sort an array by multiple values``
https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

## ``DFS & BFS``
DFS uses a stack

BFS uses a queue

## ``Heap``
A heap is a tree based data structure that satisfies the heap property.

2 types of heaps:

    Max Heap
    
    Min Heap

Although it's very common to see heap being binary, it's not always the case.

Trees cannot contain cycles. So, heaps cannot contain cycles too.

## ``Priority Queue``
Priority queues are abstract data structures meaning it can be implemented by multiple data structures.

1: It could be implemented using just a queue. However, for each insertion, a sorting will take place to ensure the priority is correct.

2: It could also be implemented using a heap. A heap will adjust the priority automatically using bubble up/down after each insertion.

## ``Sliding Window``
Always a good idea to think of sliding window when the problem has keywords like <b>consecutive</b>, <b>contiguous</b>, <b>subarray</b> and <b>substring</b>, and the input is a string or array.

Also, if the problem has a requirement like pick x something from the list and the ordering doesn't matter, think about sorting the list then apply sliding window.

https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

https://leetcode.com/problems/fruit-into-baskets/

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

## ``Binary Search Stuff``
https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems

## ``Something to look at later``
<s>Priority queue & Heap</s>

<s>Backtracking</s>

<s>Union Find</s>

Sliding Window

Matrix

Binary Search

DFS + BFS

Greedy

DP - Jump game

Segment Tree

Prefix Sum

Subsequences & Substrings

Monotonic Queue
