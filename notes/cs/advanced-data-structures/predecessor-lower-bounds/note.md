---
title: "Lower Bounds for the Static Predecessor Problem"
sources: [mit6851-13]
requires: [cs/advanced-data-structures/fusion-trees]
status: draft
---

<!-- Added 2026-11-27 from MIT 6.851 (Spring 2012), Lecture 13, in our own wording. Outline only (owner scope: brief): the round-elimination lemma is stated, not proved, and the elimination steps are summarised, not worked out. -->

Van Emde Boas trees (time $O(\log w)$) and fusion trees ($O(\log_wn)$) are optimal up to $\log\log$ factors among static structures of polynomial space.

::: {#def-colored-predecessor .definition name="Colored predecessor and the cell-probe model"}

In the *colored predecessor* problem a set $S$ of $n$ $w$-bit integers, each coloured red or blue, is stored, and a query $x$ asks for the colour of the predecessor of $x$ in $S$. A lower bound for it is a lower bound for predecessor. A static data structure of $\operatorname{poly}(n)$ words is considered (with $2^w$ words constant time is trivial). In the *cell-probe model* memory is an array of $w$-bit cells, only reads of cells (probes) are charged, and all computation is free.

:::

::: {#thm-predecessor-lower-bound .theorem name="Predecessor lower bound (Ajtai; Miltersen et al.; Beame–Fich; Pătrașcu–Thorup)"}

Any (randomised) static cell-probe data structure of $n^{O(1)}$ cells of $w$ bits for colored predecessor over $w$-bit keys and $w$-bit cells needs

$$
\Omega\!\left(\min\Bigl\{\frac{\log w}{\log\log w},\ \frac{\log n}{\log\log n}\Bigr\}\right)
$$

probes in the worst case, and in terms of both parameters the cost is $\Omega\bigl(\min\{\log_{w}n,\ \log w/\log\log n\}\bigr)$. Combined with van Emde Boas trees and fusion trees this makes $\min\{\log_wn,\log w\}$ optimal up to a $\log\log$ factor: van Emde Boas trees are optimal for $w=\operatorname{polylog}n$ and fusion trees for $\log w=\Omega(\sqrt{\log n\log\log n})$.

:::

::: {.proof}

*Outline.*

1. *Communication game.* Alice (the query) holds $x$ and Bob (the memory) holds the data structure. In each round Alice sends $a=O(\log\text{space})=O(\log n)$ bits (an address) and Bob answers with $b=w$ bits (a cell). One probe is one round (two messages), so $t$ probes give $2t$ messages. The claim to prove is that $\Omega(\min\{\log_aw,\log_bn\})$ messages are needed.

2. *Round elimination lemma.* For a function $f$ let $f^{(k)}$ be the game in which Alice holds $k$ inputs $x_1,\dots,x_k$ and Bob holds $y$, an index $i$ and $x_1,\dots,x_{i-1}$; the goal is $f(x_i,y)$. If $f^{(k)}$ has a protocol with $m$ messages, Alice speaking first, and error $\delta$, then $f$ has a protocol with $m-1$ messages, Bob first, and error $\delta+O(\sqrt{a/k})$. (Alice's first message cannot say much about the one input $x_i$ that matters, since she does not know $i$.)

3. *Eliminating Alice's message.* Cut the $w_i$-bit query into $k=\Theta(at^2)$ chunks; the elements are arranged so that they differ in chunk $i$, which Bob knows. After the elimination the key length shrinks to $w_i/k$ and the error grows by $O(1/t)$. This mirrors the way a vEB tree halves the key length.

4. *Eliminating Bob's message.* Split the $n_i$ elements into $k=\Theta(bt^2)$ groups by a prefix of $\log k$ bits; the query chooses a group. After the elimination $n_i$ shrinks to $n_i/k$ and the key length decreases by $\log k$. This mirrors a fusion-tree node.

5. *Finish.* After $2t$ eliminations the error has grown by at most $2t\cdot O(1/t)$, which can be made less than $\tfrac13$, but there are no messages left and the answer is a guess with success probability $\tfrac12$ — a contradiction. The eliminations are possible as long as the parameters $n_i$ and $w_i$ stay large, which is where $t=\Omega(\min\{\log_aw,\log_bn\})$ comes from. With $a=\Theta(\log n)$ and $b=w$ this is the stated bound.

:::

::: {#rmk-predecessor-lower-bounds-1 .remark name="History and the exact trade-off"}

Ajtai gave the first super-constant bound $\Omega(\sqrt{\log w})$ for some $n$; Miltersen recast it in communication complexity; Miltersen–Nisan–Safra–Wigderson introduced round elimination; Beame–Fich and Xiao proved the bounds above together with a matching static structure; Sen–Venkatesh strengthened the lemma. Pătrașcu and Thorup determined the whole trade-off between $n$, $w$ and the space $n2^a$: $\Theta\bigl(\min\{\log_wn,\ \log\frac{w-\log n}{a},\ \dots\}\bigr)$. The quoted statements are from the lecture; none is proved here beyond the outline.

:::
