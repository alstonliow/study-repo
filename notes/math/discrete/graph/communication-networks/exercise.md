::: {.problem #prob-mit6042f10-6-q4 origin="external" source="mit6042f10-6-q4"}
Louis Reasoner figures that, wonderful as the Beneš network may be, the butterfly network has a few advantages, namely: fewer switches, smaller diameter, and an easy way to route packets through it. So Louis designs an $N$-input/output network he modestly calls a *Reasoner-net* with the aim of combining the best features of both the butterfly and Beneš nets:

> The $i$th input switch in a Reasoner-net connects to two switches, $a_i$ and $b_i$, and likewise, the $j$th output switch has two switches, $y_j$ and $z_j$, connected to it. Then the Reasoner-net has an $N$-input Beneš network connected using the $a_i$ switches as input switches and the $y_j$ switches as its output switches. The Reasoner-net also has an $N$-input butterfly net connected using the $b_i$ switches as inputs and the $z_j$ switches as outputs.

In the Reasoner-net the minimum latency routing does not have minimum congestion. The *latency for min-congestion* (LMC) of a net is the best bound on latency achievable using routings that minimize congestion. Likewise, the *congestion for min-latency* (CML) is the best bound on congestion achievable using routings that minimize latency.

Fill in the following chart for the Reasoner-net and briefly explain your answers.

| diameter | switch size(s) | # switches | congestion | LMC | CML |
|---|---|---|---|---|---|
| | | | | | |

*Note (these notes):* The answers depend on how latency is counted; the solution counts edges from terminal to terminal, as in the textbook's table.
:::

::: {.problem #prob-mit6042f10-6-q5 origin="external" source="mit6042f10-6-q5"}
Let $B_n$ denote the butterfly network with $N = 2^n$ inputs and outputs, as defined in Notes 6.3.8. We will show that the congestion of $B_n$ is exactly $\sqrt{N}$ when $n$ is even.

Hints:

- For the butterfly network, there is a unique path from each input to each output, so the congestion is the maximum number of messages passing through a vertex for any matching of inputs to outputs.
- If $v$ is a vertex at level $i$ of the butterfly network, there is a path from exactly $2^i$ input vertices to $v$ and a path from $v$ to exactly $2^{n-i}$ output vertices.
- At which level of the butterfly network must the congestion be worst? What is the congestion at the node whose binary representation is all 0s at that level of the network?

(a) Show that the congestion of $B_n$ is at most $\sqrt{N}$ when $n$ is even.

(b) Show that the congestion achieves $\sqrt{N}$ somewhere in the network and conclude that the congestion of $B_n$ is exactly $\sqrt{N}$ when $n$ is even.

*Note (these notes):* Notes 6.3.8 refers to the 2010 course notes; the butterfly is defined in @def-butterfly.
:::
