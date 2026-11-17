<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-10-q1" status="draft"}
(a) *No algorithm exists.* As in @thm-no-symmetric-leader: all processes start in the same state, and by induction on the rounds they stay in the same state, since each sends the same messages on its left and right ports and, by the symmetry of the ring, receives the same messages. When one outputs LEADER, all do.

(b) Work in *phases* of $n$ rounds. In each phase every process picks a number uniformly from $\{1,\dots,r\}$ and sends it clockwise; for $n-1$ rounds every process forwards what it receives. After the phase every process knows the whole cyclic list of numbers (in the same order relative to itself), so all reach the same verdict: if the maximum occurs exactly once, its owner outputs LEADER and the algorithm stops; otherwise a new phase starts. At most one leader is ever elected, because all processes see the same list. A phase fails only if two processes draw the same maximum, with probability at most $\binom n2\frac1r<\frac{n^2}{2r}$; with $r=\lceil n^2\rceil$ a phase succeeds with probability at least $\frac12$, so a leader is elected with probability $1$, and within $\lceil\lg\frac1\varepsilon\rceil$ phases with probability at least $1-\varepsilon$. Each phase takes $n$ rounds and $n^2$ messages (of $O(\lg n)$ bits): $O(n\lg\frac1\varepsilon)$ time and $O(n^2\lg\frac1\varepsilon)$ messages with probability $1-\varepsilon$. (Alternatively one phase with $r=\lceil n^2/(2\varepsilon)\rceil$.)

(c) *No algorithm exists.* Suppose an algorithm works for all ring sizes. In a ring of size $n$ it elects a leader with probability $1$, so some finite execution $\alpha$ in which a leader is elected has positive probability; let $\alpha$ use $t$ rounds and fix the coin results $c_1,\dots,c_n$ of the processes in it. In a ring of size $2n$, with positive probability process $i$ and process $i+n$ both draw the coin results $c_i$. Then, by induction on the rounds, process $i$ and process $i+n$ behave exactly like process $i$ in $\alpha$: each sees the same messages from neighbours that behave like its neighbours in $\alpha$. So after $t$ rounds two processes output LEADER, which happens with positive probability, contradicting property (a).
:::

::: {.solution for="prob-mit6046s15-10-q2" status="draft"}
(a) The tree is built in phases $\ell=1,2,\dots$; at the start of phase $\ell$ the tree contains exactly the nodes at distance less than $\ell$, each knowing its parent and children.

1. *Broadcast:* $v_0$ sends *ready* down the tree; each node forwards it to its children.
2. *Search:* a node at depth $\ell-1$ (a leaf of the current tree) that receives *ready* sends *search* to all its neighbours except its parent.
3. *Answer:* a node not yet in the tree that receives its *first* search sets its parent to the sender, answers *parent(true)*, and answers *parent(false)* to any later search; a node already in the tree answers *parent(false)*.
4. *Convergecast:* a frontier node, after all its answers have arrived, records its new children and sends *done* to its parent, saying whether it found any; an inner node sends *done* once all its children have, combining the flags.
5. When $v_0$ receives *done* from all children, it starts phase $\ell+1$ if any new node was found, and stops otherwise.

*Correctness:* by induction on $\ell$. All searches of phase $\ell$ come from nodes at distance exactly $\ell-1$, and a node joins in phase $\ell$ only if it is adjacent to such a node and was not in the tree, that is, exactly when its distance is $\ell$. So every parent is set once and is a correct BFS parent: no corrections are ever needed.

(b) *Time:* phase $\ell$ is a broadcast down and a convergecast up a tree of depth $\ell$, plus one search-and-answer exchange, $O(\ell\,d)$ with message delay at most $d$. Over $\mathrm{diam}$ phases, $O(\mathrm{diam}^2d)$. *Messages:* each phase sends *ready* and *done* once along each tree edge, $O(n)$ per phase and $O(n\cdot\mathrm{diam})$ in total; each node sends *search* once to each neighbour and gets one answer each, $O(E)$ in total. So $O(E+n\cdot\mathrm{diam})$ messages, compared with $O(nE)$ messages and $O(\mathrm{diam}\cdot n\cdot d)$ time for the correcting algorithm: far fewer messages, and faster whenever $\mathrm{diam}=o(n)$.
:::
