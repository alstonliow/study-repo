<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-3-q6" status="draft"}
(a) Every vertex has degree $n$ (one neighbour per bit), and the hypercube is connected (change the differing bits one at a time). By Euler's theorem (@sec-math-discrete-graph-euler-and-hamilton) it has an Eulerian tour if and only if every degree is even, i.e. $n$ is even. (For $n=0$ the single vertex has the empty tour.)

(b) By induction on $n\ge1$.

1. *$n=1$:* the sequence $0,1$ works.

2. *Step:* let $v_0,\dots,v_k$ ($k=2^n-1$) be a Hamiltonian tour of the $n$-cube. In the $(n+1)$-cube take
   $$0v_0,\,0v_1,\,\dots,\,0v_k,\,1v_k,\,1v_{k-1},\,\dots,\,1v_0.$$

3. Every string of length $n+1$ appears once. Consecutive strings differ in one bit: within each half because consecutive $v_i$ do, and $0v_k,1v_k$ in the first bit. The last string $1v_0$ and the first $0v_0$ differ only in the first bit.
:::
