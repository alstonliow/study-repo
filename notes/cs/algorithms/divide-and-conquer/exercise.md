::: {.problem #prob-mit6046s15-1-q2 origin="external" source="mit6046s15-1-q2"}
**Radio Frequency Assignment**

Prof. Wheeler at the Federal Communications Commission (FCC) has a huge pile of requests from radio stations in the Continental U.S. to transmit on radio frequency 88.1 FM. The FCC is happy to grant all the requests, provided that no two of the requesting locations are within Euclidean distance 1 of each other (distance 1 might mean, say, 20 miles). However, if any are within distance 1, Prof. Wheeler will get annoyed and reject the entire set of requests.

Suppose that each request for frequency 88.1 FM consists of some identifying information plus $(x,y)$ coordinates of the station location. Assume that no two requests have the same $x$ coordinate, and likewise no two have the same $y$ coordinate. The input includes two sorted lists, $L_x$ of the requests sorted by $x$ coordinate and $L_y$ of the requests sorted by $y$ coordinate.

(a) Suppose that the map is divided into a square grid, where each square has dimensions $\frac12\times\frac12$. Why must the FCC reject the set of requests if two requests are in, or on the boundary of, the same square?

(b) Design an efficient algorithm for the FCC to determine whether the pile of requests contains two that are within Euclidean distance 1 of each other; if so, the algorithm should also return an example pair. For full credit, your algorithm should run in $O(n\lg n)$ time, where $n$ is the number of requests.

*Hint:* Use divide-and-conquer, and use Part (a).

(c) Describe how to modify your solution for Part (b) to determine whether there are three requests, all within distance 1 of each other. For full credit, your algorithm should run in $O(n\lg n)$ time, where $n$ is the number of requests.
:::
