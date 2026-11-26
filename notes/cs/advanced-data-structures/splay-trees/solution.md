<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6854ps-3-q1" status="draft"}
1. *Representation.* Keep the path in a splay tree whose in-order is the path order (no keys are stored; positions are implicit). Each node stores its subtree size and a *reverse bit*; a set bit at $x$ means that the subtree of $x$ is to be read mirrored. Keep a pointer from every vertex to its node.

2. *Pushing bits.* `push(x)`: if the bit of $x$ is set, swap the children of $x$, toggle the bits of both children and clear the bit of $x$. Sizes are unaffected by mirroring. Before splaying a node $x$, walk up from $x$ to the root, then call `push` on the ancestors from the root down to $x$; this costs as much as the splay and is charged to it. After `push` along the path, all bits on it are clear, so rotations can be done as usual, with sizes updated in $O(1)$ per rotation from the children's sizes.

3. *Position.* After splaying $x$, its position on the path is $1+\operatorname{size}(\text{left}(x))$.

4. *Next and Previous.* Splay $v$; then $\textsc{Next}(v)$ is the leftmost node of $v$'s right subtree (walk down, pushing bits on the way, and splay the node found), and $\textsc{Previous}(v)$ the rightmost node of the left subtree.

5. *Reverse$(v,w)$.* Find the positions of $v$ and $w$ and swap them if needed so that $v$ comes first. Split the tree into $L$ (before $v$), $M$ ($v$ through $w$) and $R$ (after $w$) with two splits (splay $v$ and cut off its left subtree; splay $w$ inside the rest and cut off its right subtree). Toggle the bit at the root of $M$. Join $L$, $M$, $R$ back (@def-splay-tree-operations).

6. *Cost.* Each operation is $O(1)$ splays, splits and joins, each $O(\log n)$ amortized by @thm-access-lemma and @thm-splay-sequence (bits and sizes do not affect the potential). Building the initial tree as a path costs $O(n)$ and its potential is at most $n\log n$, so $m$ operations cost $O((m+n)\log n)$.
:::

::: {.solution for="prob-mit6854ps-3-q2" status="draft"}
1. Choose the weights $w(i)=m_i/m$, so the total weight is $s(\text{root})=1$ and every size lies between $w(i)$ and $1$.

2. By @thm-access-lemma, one access to $i$ costs at most $3\big(\log1-\log(m_i/m)\big)+1=1+3\log(m/m_i)$ amortized. All accesses together: $\sum_im_i\big(1+3\log(m/m_i)\big)$.

3. The actual cost exceeds the amortized cost by the drop of potential $\Phi_0-\Phi_{\text{end}}$. Each rank is at most $\log1=0$ and at least $\log w(i)$, so the drop is at most $\sum_i\log(m/m_i)\le\sum_im_i\log(m/m_i)$, since $m_i\ge1$.

4. So $T=O\big(\sum_im_i(1+\log(m/m_i))\big)$.
:::
