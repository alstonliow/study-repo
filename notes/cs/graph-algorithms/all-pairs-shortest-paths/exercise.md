::: {.problem #prob-mit6006s20-6-q6 origin="external" source="mit6006s20-6-q6"}
**Johnson's Algorithm**

In this problem, you will implement Johnson's Algorithm to compute all-pairs shortest-path weights in a general weighted directed graph $G$, as described in Lecture 14. The input to your algorithm will be: a positive integer $n$ representing the number of vertices of your graph identified by consecutive integers $0$ to $n-1$, and a tuple $S$ of triples, where each triple $(u,v,w)$ corresponds to a directed edge from vertex $u$ to $v$ of weight $w$. Your output should be a length-$n$ tuple $D$ of length-$n$ tuples where $D[u][v]=\delta(u,v)$ for all $u,v\in\{0,\dots,n-1\}$, except when the input graph contains a negative-weight cycle when you should return `None`.

Please implement the `johnson(n, S)` function in the template code provided. Your code template contains working implementations of Bellman–Ford and Dijkstra (using a binary heap as a priority queue) modified from the recitation notes. Note that you will have to construct your own adjacency list and weight function if you would like to use this code. You can download the code template and some test cases from the website.
:::
