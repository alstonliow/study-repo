---
title: "Distributed Algorithms"
sources: [mit6046-19, mit6046-20, mit6046r-10]
requires: [cs/graph-algorithms/bellman-ford, cs/algorithm-design/randomized-algorithms]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lectures 19-20 and Recitation 10, in our own wording; proofs written out in steps. -->

In a *distributed* system, many processes, each knowing only its own part of the input, cooperate by sending messages along the edges of a network. We measure *time* (rounds) and *communication* (messages), not the work of one machine.

## Synchronous networks

::: {#def-synchronous-model .definition name="Synchronous network model"}

The network is a connected undirected graph $G=(V,E)$ with a process at each vertex, which knows only its neighbours' ports, not the whole graph. Computation proceeds in *rounds*: in each round every process sends messages to some neighbours, then receives the messages sent to it, then changes state. *Time* is the number of rounds and *communication* the total number of messages.

:::

### Leader election

The task is for exactly one process to output "leader". The basic obstacle is symmetry.

::: {#thm-no-symmetric-leader .theorem name="Identical processes cannot elect a leader"}

In a complete graph on $n\ge2$ vertices, with ports numbered consistently, there is no algorithm in which all processes are deterministic and start in the same state that is guaranteed to elect a leader.

:::

::: {.proof}

1. By induction on the round $r$, all processes are in the same state after $r$ rounds: in the same state they send the same message on each port, by symmetry they receive the same messages, and they make the same state change.

2. Since the algorithm succeeds, some process eventually outputs "leader"; at that moment all processes are in the same state, so all of them do. That contradicts "exactly one".

:::

Symmetry is broken by *unique identifiers* (UIDs): in a complete graph, every process sends its UID to all others, and the one with the largest UID becomes leader, in $1$ round with $n^2$ messages. Without UIDs, *randomness* helps: each process picks a number from $\{1,\dots,r\}$ at random and the unique maximum, if there is one, wins; if the maximum is not unique, try again. With $r=\lceil n^2/(2\varepsilon)\rceil$ the numbers are all distinct with probability at least $1-\varepsilon$ (by the union bound over the $\binom n2$ pairs).

### Maximal independent set

::: {#def-luby-mis .definition name="Luby's algorithm"}

The goal is a *maximal independent set* (MIS): independent, and no vertex can be added. In each phase every *active* process picks a random number and sends it to its active neighbours; a process whose number is larger than all its neighbours' joins the MIS and tells its neighbours, who then leave (they will not join). Processes that joined or left become inactive. Repeat until no process is active.

:::

::: {#thm-luby .theorem name="Luby's algorithm"}

The output is a maximal independent set. With high probability the algorithm ends after $O(\log n)$ phases.

:::

::: {.proof}

1. *Independent:* two neighbours cannot both have the larger number, and a neighbour of a process that joins becomes inactive in the same phase.

2. *Maximal:* a process stops being active only by joining, or by having a neighbour join.

3. *Speed (sketch):* one shows that each phase removes, in expectation, at least half of the remaining edges. Then after $4\log_2n$ phases the expected number of edges left is at most $n^2/n^4<1/n$, so by Markov's inequality the algorithm has finished with probability at least $1-1/n$.

:::

### Breadth-first spanning tree

::: {#def-distributed-bfs .definition name="Synchronous BFS"}

A distinguished process $i_0$ starts by marking itself and sending a "search" message to its neighbours. Every process that receives "search" for the first time marks itself, chooses one of the senders as its parent, and in the next round sends "search" to its neighbours.

:::

::: {#fig-distributed-algorithms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (v0) at (0,0) {$v_0$};
\node[lab,tick] at (0,-0.45) {round 0};
\node[small vertex] (a) at (1.5,0.9) {$a$};
\node[lab,tick] at (1.5,1.35) {round 1};
\node[small vertex] (b) at (1.5,-0.9) {$b$};
\node[lab,tick] at (1.5,-1.35) {round 1};
\node[small vertex] (c) at (3,0.9) {$c$};
\node[lab,tick] at (3,1.35) {round 2};
\node[small vertex] (d) at (3,-0.9) {$d$};
\node[lab,tick] at (3,-1.35) {round 2};
\node[small vertex] (e) at (4.5,0) {$e$};
\node[lab,tick] at (4.5,-0.45) {round 3};
\draw[->, hl] (v0) -- (a);
\draw[->, hl] (v0) -- (b);
\draw[faint] (a) -- (b);
\draw[->, hl] (a) -- (c);
\draw[->, hl] (b) -- (d);
\draw[faint] (c) -- (d);
\draw[->, hl] (c) -- (e);
\draw[faint] (d) -- (e);
\end{tikzpicture}
\end{center}
```

Synchronous BFS from $v_0$: a process is reached in the round equal to its distance from $v_0$ and picks a sender as parent (highlighted). After $\mathrm{diam}(G)=3$ rounds every process has a parent on a shortest path.

:::

By induction on $d$, after round $d$ exactly the processes at distance at most $d$ from $i_0$ are marked, and each process at distance $d$ has a parent at distance $d-1$. So the parent pointers form a BFS tree after $\mathrm{diam}(G)$ rounds, using $O(|E|)$ messages (each process sends once to each neighbour). To let $i_0$ know that the tree is finished, children report back to parents (*convergecast*): a process reports "done" once all its children have; this doubles the time and adds $O(|V|)$ messages.

With edge weights, the same scheme with relaxations is distributed *Bellman–Ford*: every process keeps an estimate $d(v)$ of its distance to $i_0$ and, whenever it improves, sends it to its neighbours, who relax (@def-relaxation). After $|V|-1$ rounds every estimate is exact (as in @thm-bellman-ford), and the parents form a shortest-path tree.

## Asynchronous networks

::: {#def-asynchronous-model .definition name="Asynchronous network model"}

In an *asynchronous* network, processes and communication channels proceed at arbitrary, unknown speeds: every message is delivered eventually, but in an order and at times chosen by an adversary. Time is measured assuming each message takes at most one unit, to get worst-case bounds.

:::

Running the BFS algorithm above asynchronously still produces a spanning tree, but not necessarily a *BFS* tree: a message along a long path can arrive before one along a short path. The fix is relaxation, as in Bellman–Ford: each process keeps its best known distance and parent, and *changes* them (forwarding the new distance) whenever a shorter one arrives. The final tree is correct, but the number of messages can be much larger, because estimates may change many times; for weighted shortest paths the worst case is exponential in $|V|$. Termination is detected by convergecast that is restarted whenever a process changes its parent.
