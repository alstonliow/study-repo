::: {.problem #prob-cs70hw-3-q6 origin="external" source="cs70hw-3-q6"}
**Touring Hypercube.** In the lecture, you have seen that if $G$ is a hypercube of dimension $n$, then

- The vertices of $G$ are the binary strings of length $n$.
- $u$ and $v$ are connected by an edge if they differ in exactly one bit location.

A Hamiltonian tour of a graph is a sequence of vertices $v_0, v_1, \ldots, v_k$ such that:

- Each vertex appears exactly once in the sequence.
- Each pair of consecutive vertices is connected by an edge.
- $v_0$ and $v_k$ are connected by an edge.

(a) Show that a hypercube has an Eulerian tour if and only if $n$ is even. (Hint: Euler's theorem)

(b) Show that every hypercube has a Hamiltonian tour.

*Note (these notes):* (b) is the reflected Gray code.
:::
