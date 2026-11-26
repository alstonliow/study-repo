::: {.problem #prob-mit6854ps-1-q1 origin="external" source="mit6854ps-1-q1"}
Show a sequence of operations that can lead to a Fibonacci heap on $n$ elements which is a chain.
:::

::: {.problem #prob-mit6854ps-1-q2 origin="external" source="mit6854ps-1-q2"}
Suppose that Fibonacci heaps were modified so that a node is marked after losing $k-1$ children (as opposed to just one child in the original setting), and thus a node is cut after losing $k$ children.

(a) Assuming that $k$ is a constant, show that this will improve the amortized cost of decrease key (to a better constant) while it will increase the amortized cost of delete-min (by a constant factor). You may need to change the potential function for the analysis.

(b) Could one take $k$ growing with $n$ and still have logarithmic ranks for every node?
:::
