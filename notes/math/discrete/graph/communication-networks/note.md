---
title: "Communication Networks"
sources: [mcs-10]
requires: [math/discrete/graph/directed-graphs, math/discrete/graph/bipartite-graphs]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.042J, Mathematics for Computer Science (2015), Chapter 10, in our own wording; proofs written out in steps. -->

## Routing problems

A *switching network* connects $N$ *input terminals* to $N$ *output terminals* through *switches*. It is a directed graph whose vertices are terminals and switches; we take $N=2^n$. Packets enter at the inputs and must reach prescribed outputs.

::: {#def-routing .definition name="Routing, diameter, congestion"}

1. In a *permutation routing problem* $\pi$, the packet at input $i$ must reach output $\pi(i)$, for a permutation $\pi$ of $\{0,\dots,N-1\}$. A *routing* for $\pi$ is a choice of a path from input $i$ to output $\pi(i)$ for every $i$.

2. The *diameter* of the network is the largest, over input–output pairs, of the length of a shortest path between them; it bounds the delay of a packet.

3. The *congestion* of a routing is the largest number of its paths passing through a single switch. The *congestion of the network* is the largest, over permutations $\pi$, of the least congestion of a routing for $\pi$.

:::

## Four networks

::: {#rmk-communication-networks-tree-array .remark name="Tree and array"}

1. *Complete binary tree.* The inputs and outputs sit at the leaves of a complete binary tree of switches, with $2N-1$ switches of size $3\times3$. Its diameter is $2\log_2N+2$, but for the permutation that swaps the two halves, every packet passes through the root: the congestion is $N$.

2. *Two-dimensional array.* Switches form an $N\times N$ grid; input $i$ enters row $i$ from the left, output $j$ leaves column $j$ at the bottom, and packets move right or down. It has $N^2$ switches of size $2\times2$ and diameter $2N$.

:::

::: {#prp-array-congestion .proposition name="Congestion of the array"}

The congestion of the $N$-input two-dimensional array is $2$ (for $N\ge2$).

:::

::: {.proof}

1. *At most $2$.* For any permutation $\pi$, route packet $i$ right along row $i$ to column $\pi(i)$, then down column $\pi(i)$. A switch $(i,j)$ is used by at most one packet travelling along row $i$ (the packet from input $i$) and at most one travelling down column $j$ (the packet bound for output $j$).

2. *At least $2$.* Every path from input $N-1$ starts at the bottom-left switch, and every path to output $0$ ends there (packets only move right or down). Take any permutation with $\pi(N-1)\ne0$, possible for $N\ge2$. Then two different packets, the one from input $N-1$ and the one bound for output $0$, pass through the bottom-left switch in every routing.

:::

::: {#def-butterfly .definition name="Butterfly and Beneš networks"}

The *butterfly* $F_n$ with $N=2^n$ inputs is defined recursively: $F_1$ has two input switches, each joined to both of two output switches. $F_{n+1}$ takes two copies of $F_n$ and $2^{n+1}$ new input switches; the new switches $i$ and $2^n+i$ are both joined to input switch $i$ of each copy. The *Beneš network* $B_{n+1}$ is built in the same way from two copies of $B_n$, with a new column of input switches before them and, symmetrically, a new column of output switches after them; $B_1=F_1$.

:::

::: {#prp-butterfly-size .proposition name="Size and diameter of the butterfly"}

The butterfly $F_n$ has $N(\log_2N+1)$ switches, and every input switch is joined to every output switch by a unique path with $\log_2N$ edges; with the terminals the diameter is $\log_2N+2$.

:::

::: {.proof}

1. *Switches.* $F_n$ has $n+1$ columns of $2^n$ switches each: true for $n=1$ ($2$ columns of $2$), and $F_{n+1}$ adds one column of $2^{n+1}$ switches in front of two copies of $F_n$, whose columns stack into $n+1$ columns of $2^{n+1}$. So there are $2^n(n+1)=N(\log_2N+1)$ switches.

2. *Unique paths*, by induction on $n$. For $n=1$, each input switch has one edge to each output switch. In $F_{n+1}$, an output lies in exactly one copy of $F_n$; the first step must go from the input switch to its neighbour in that copy (it has exactly one there), and from there the path is unique by the hypothesis. Its length is $1+n$.

:::

::: {#rmk-communication-networks-comparison .remark name="Comparison"}

| Network | diameter | switch size | number of switches | congestion |
|---|---|---|---|---|
| complete binary tree | $2\log_2N+2$ | $3\times3$ | $2N-1$ | $N$ |
| 2-D array | $2N$ | $2\times2$ | $N^2$ | $2$ |
| butterfly | $\log_2N+2$ | $2\times2$ | $N(\log_2N+1)$ | $\sqrt N$ or $\sqrt{N/2}$ |
| Beneš | $2\log_2N+1$ | $2\times2$ | $2N\log_2N$ | $1$ |

The butterfly's congestion is $\sqrt N$ when $n$ is even and $\sqrt{N/2}$ when $n$ is odd; we do not prove it. The Beneš network achieves the best possible congestion with few switches.

:::

::: {#thm-benes-congestion .theorem name="Beneš networks have congestion 1"}

For every permutation of the $N=2^n$ inputs of $B_n$, there is a routing in which no two paths share a switch.

:::

::: {.proof}

Induction on $n$. For $n=1$, $B_1$ joins each of its two input switches to both output switches, so either permutation of two packets can be routed through distinct switches.

For the step, let $\pi$ be a permutation for $B_{n+1}$, with $2N$ inputs, $N=2^n$. Each packet must pass through the upper or the lower copy of $B_n$; if the packets assigned to each copy form a permutation problem for that copy, the hypothesis routes them with congestion $1$ there.

1. Input switches $i$ and $i+N$ share their two neighbours (one in each copy), so their packets must go to different copies. Likewise the two packets bound for outputs $j$ and $j+N$ must arrive from different copies.

2. Build a graph on the $2N$ packets with an edge between the two packets of each input pair and between the two packets of each output pair. Every packet has degree at most $2$ (one input partner, one output partner), and following edges alternately of the two kinds, every cycle alternates input and output edges, so it has even length.

3. A graph whose cycles are all even is bipartite (@sec-math-discrete-graph-bipartite-graphs), so it has a $2$-colouring. Send the packets of one colour through the upper copy and the others through the lower copy.

4. Then each copy receives exactly one packet from each input pair and delivers exactly one to each output pair: a permutation problem for $B_n$. By the hypothesis both are routed with congestion $1$, and the new first and last columns carry one packet per switch.

:::
