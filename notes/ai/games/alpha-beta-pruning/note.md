---
title: "Alpha-Beta Pruning"
sources: [cs221-13]
requires: [ai/games/game-trees]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 13 (alpha-beta pruning, move ordering), in our own wording. Correctness theorem and proof are our own formulation; proof written out in steps. -->

Minimax visits the whole game tree. Many subtrees cannot affect the result: if one option is known to be worth between $5$ and $100$ and another between $3$ and $5$, the first wins without computing either exactly. This *branch and bound* idea, applied to minimax, is alpha-beta pruning.

::: {#def-alpha-beta-pruning .definition name="Alpha-beta pruning"}

*Alpha-beta pruning* computes minimax values depth-first, carrying two bounds: $\alpha$, the best value the agent (max) is already guaranteed on the current path, and $\beta$, the best value the opponent (min) is already guaranteed. At a max node it raises $\alpha$ to each child's value as it is found, at a min node it lowers $\beta$, and as soon as $\alpha\ge\beta$ it stops examining the node's remaining children (it *prunes* them): play following optimal moves will never reach this node.

:::

```{=latex}
\begin{algorithm}
\caption{Alpha-beta pruning}
\begin{algorithmic}
\INPUT A state $s$ and bounds $\alpha<\beta$ (initially $-\infty,+\infty$)
\OUTPUT A value $v$ (equal to $V_{\text{minmax}}(s)$ when it lies strictly between $\alpha$ and $\beta$)
\FUNCTION{AlphaBeta}{$s,\alpha,\beta$}
    \IF{$\text{IsEnd}(s)$}
        \RETURN $\text{Utility}(s)$
    \ENDIF
    \IF{$\text{Player}(s)=\text{agent}$}
        \STATE $v\gets-\infty$
        \FOR{$a\in\text{Actions}(s)$}
            \STATE $v\gets\max(v,\textsc{AlphaBeta}(\text{Succ}(s,a),\alpha,\beta))$; \quad $\alpha\gets\max(\alpha,v)$
            \IF{$\alpha\ge\beta$} \STATE \textbf{break} \COMMENT{prune remaining children} \ENDIF
        \ENDFOR
    \ELSE
        \STATE $v\gets+\infty$
        \FOR{$a\in\text{Actions}(s)$}
            \STATE $v\gets\min(v,\textsc{AlphaBeta}(\text{Succ}(s,a),\alpha,\beta))$; \quad $\beta\gets\min(\beta,v)$
            \IF{$\alpha\ge\beta$} \STATE \textbf{break} \ENDIF
        \ENDFOR
    \ENDIF
    \RETURN $v$
\ENDFUNCTION
\end{algorithmic}
\end{algorithm}
```

::: {#thm-alpha-beta-correct .theorem name="Alpha-beta pruning is exact"}

Let $V=V_{\text{minmax}}(s)$ and let $v=\textsc{AlphaBeta}(s,\alpha,\beta)$ with $\alpha<\beta$. Then: if $\alpha<V<\beta$, $v=V$; if $V\le\alpha$, $v\le\alpha$; if $V\ge\beta$, $v\ge\beta$. In particular $\textsc{AlphaBeta}(s_{\text{start}},-\infty,+\infty)=V_{\text{minmax}}(s_{\text{start}})$.

:::

::: {.proof}

1. Induction on the height of $s$. At an end state $v=\text{Utility}(s)=V$, which satisfies all three statements.

2. Let $s$ be a max node with children $c_1,\dots,c_k$ (min nodes are symmetric, with the roles of $\alpha,\beta$ and of $\max,\min$ exchanged). Write $V_i=V_{\text{minmax}}(c_i)$, $v_i$ the value returned for $c_i$, and $\alpha_i$ the value of $\alpha$ passed to $c_i$; then $\alpha_1=\alpha$ and $\alpha_{i+1}=\max(\alpha_i,v_i)$, and the loop stops once $\alpha_{i+1}\ge\beta$.

3. Claim: $\max(\alpha_i,v_i)=\max(\alpha_i,V_i)$ as long as this is below $\beta$, and both are $\ge\beta$ otherwise. This is the induction hypothesis for $c_i$ with bounds $(\alpha_i,\beta)$: if $V_i\le\alpha_i$ then $v_i\le\alpha_i$ and both maxima equal $\alpha_i$; if $\alpha_i<V_i<\beta$ then $v_i=V_i$; if $V_i\ge\beta$ then $v_i\ge\beta$.

4. Suppose no pruning happens. Since $\alpha_{i+1}=\max(\alpha,v_1,\dots,v_i)$, step 3 and induction on $i$ give $\alpha_{i+1}=\max(\alpha,V_1,\dots,V_i)$, so $\max(\alpha,v)=\alpha_{k+1}=\max(\alpha,V)<\beta$, where $v=\max_iv_i$. If $V>\alpha$, then $\max(\alpha,v)=V>\alpha$, which forces $v=V$. If $V\le\alpha$, then $\max(\alpha,v)=\alpha$, so $v\le\alpha$.

5. Suppose the loop stops after child $i$ because $\max(\alpha_i,v_i)\ge\beta$. By step 3, $\max(\alpha_i,V_i)\ge\beta$, and $\alpha_i<\beta$ (the loop did not stop earlier), so $V_i\ge\beta$ and hence $V\ge V_i\ge\beta$. Also $v\ge v_i$ and $\max(\alpha_i,v_i)\ge\beta>\alpha_i$ give $v_i\ge\beta$, so $v\ge\beta$, as claimed.

:::

::: {#exm-alpha-beta-pruning-1 .example name="Pruning a tree"}

Let the root be a max node with three min children: the first has leaves $9,7$; the second has a leaf $6$ and two max children with leaves $3,4$ and $7,9$; the third has leaves $8,3$. Exploring left to right, the first min node is worth $7$, so $\alpha=7$ at the root. The second min node's first leaf is $6$, so its value is at most $6<7$; its two max children are pruned. The third min node sees $8$, then $3$, giving $\beta=3\le7$, and stops. The root value is $7$, after visiting $5$ of the $9$ leaves.

:::

::: {#fig-alpha-beta-pruning-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.8cm,y=1.05cm]
\node[small vertex] (r) at (4.5,0) {$7$};
\node[small vertex] (m1) at (1,-1) {$7$};
\node[small vertex] (m2) at (4.5,-1) {$\le6$};
\node[small vertex] (m3) at (8,-1) {$\le3$};
\node[lab] (l1) at (0.5,-2) {$9$}; \node[lab] (l2) at (1.5,-2) {$7$};
\node[lab] (l3) at (3,-2) {$6$};
\node[small vertex,faint] (x1) at (4.5,-2) {};
\node[small vertex,faint] (x2) at (6,-2) {};
\node[lab] (l4) at (4.1,-3) {$3$}; \node[lab] (l5) at (4.9,-3) {$4$};
\node[lab] (l6) at (5.6,-3) {$7$}; \node[lab] (l7) at (6.4,-3) {$9$};
\node[lab] (l8) at (7.5,-2) {$8$}; \node[lab] (l9) at (8.5,-2) {$3$};
\draw[hl] (r) -- (m1); \draw (r) -- (m2); \draw (r) -- (m3);
\draw (m1) -- (l1); \draw[hl] (m1) -- (l2); \draw (m2) -- (l3); \draw[faint] (m2) -- (x1); \draw[faint] (m2) -- (x2);
\draw[faint] (x1) -- (l4); \draw[faint] (x1) -- (l5); \draw[faint] (x2) -- (l6); \draw[faint] (x2) -- (l7);
\draw (m3) -- (l8); \draw (m3) -- (l9);
\node[lab,anchor=west] at (9.2,0) {max, $\alpha=7$};
\node[lab,anchor=west] at (9.2,-1) {min};
\end{tikzpicture}
\end{center}
```

Alpha-beta pruning on the tree of @exm-alpha-beta-pruning-1, children explored left to right. Faint parts are pruned; the optimal path is highlighted.

:::

::: {#rmk-alpha-beta-pruning-1 .remark name="Move ordering"}

What can be pruned depends on the order of the children. For a max root with min children $\{2,10\}$ and $\{3,5\}$, visiting the first child first gives $\alpha=2$ and the second child must be fully explored; visiting the second child first gives $\alpha=3$, and then the leaf $2$ of the other child prunes its leaf $10$. Bounds shrink fastest when the best moves come first, so in practice children of max nodes are explored in decreasing order of a heuristic such as an evaluation function (@sec-ai-games-game-evaluation-functions), and children of min nodes in increasing order. With perfect ordering, alpha-beta examines about $b^{d/2}$ instead of $b^d$ leaves of a tree with branching factor $b$ and depth $d$, so it can search twice as deep in the same time.

:::
