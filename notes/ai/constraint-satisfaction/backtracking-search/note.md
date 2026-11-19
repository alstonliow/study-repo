---
title: "Backtracking Search, Filtering and Ordering"
sources: [cs188-4]
requires: [ai/constraint-satisfaction/constraint-satisfaction-problems]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 4 (backtracking search, forward checking, minimum remaining values, least constraining value), in our own wording; the 4-queens trace was checked by a short Python simulation. Arc consistency, the stronger filter, has its own note. -->

Plain depth-first search on the formulation of @prp-csp-search-formulation would assign all variables and only then test the constraints. Two simple ideas make it practical: assign one variable at a time, and check constraints as soon as they can be checked.

::: {#def-backtracking-search .definition name="Backtracking search"}

*Backtracking search* is depth-first search over partial assignments in which each level assigns one variable, and a value is tried only if it is consistent with the values already assigned. When a variable has no consistent value left, the search returns to the previous variable and tries its next value.

:::

```{=latex}
\begin{algorithm}
\caption{Backtracking search}
\begin{algorithmic}
\INPUT CSP, partial assignment $\alpha$ (initially empty)
\OUTPUT A solution extending $\alpha$, or failure
\FUNCTION{Backtrack}{$\alpha$}
    \IF{$\alpha$ is complete}
        \RETURN $\alpha$
    \ENDIF
    \STATE $X\gets$ an unassigned variable \COMMENT{e.g.\ by MRV}
    \FOR{each value $x\in D_X$ \COMMENT{e.g.\ in LCV order}}
        \IF{$\alpha\cup\{X=x\}$ is consistent}
            \STATE filter the domains of the unassigned variables \COMMENT{optional}
            \IF{no domain became empty}
                \STATE $r\gets$ \CALL{Backtrack}{$\alpha\cup\{X=x\}$}
                \IF{$r\ne$ failure}
                    \RETURN $r$
                \ENDIF
            \ENDIF
            \STATE undo the filtering
        \ENDIF
    \ENDFOR
    \RETURN failure
\ENDFUNCTION
\end{algorithmic}
\end{algorithm}
```

::: {#thm-backtracking-complete .theorem name="Backtracking search is complete"}

For a CSP with finitely many variables and finite domains, backtracking search returns a solution if one exists and failure otherwise. This remains true with forward checking, arc consistency (@def-ac3) or any filter that removes only values belonging to no solution extending the current assignment.

:::

::: {.proof}

1. Termination: each level tries finitely many values and the depth is at most $n$, so the search tree is finite and depth-first search visits each node once.
2. Every assignment returned is complete, and consistent because each value was checked against all earlier ones; so it is a solution.
3. Suppose a solution $\sigma$ exists. Call a node *on track* if its assignment agrees with $\sigma$. The root is on track. At an on-track node with chosen variable $X$, the value $\sigma(X)$ is consistent with the assignment (both are parts of $\sigma$), and a valid filter does not remove $\sigma(Y)$ from any domain, since $\sigma$ extends the new assignment; so no domain becomes empty and the child for $X=\sigma(X)$ is visited unless the search has already returned.
4. By step 3 an on-track node at depth $n$, which is $\sigma$, is visited unless a solution is returned earlier. Either way a solution is returned.

:::

::: {#def-forward-checking .definition name="Forward checking"}

*Forward checking* is the filter that, after $X=x$ is assigned, removes from the domain of every unassigned neighbour $Y$ of $X$ in the constraint graph the values $y$ for which $X=x,\ Y=y$ violates a constraint. The branch is abandoned as soon as some domain becomes empty.

:::

Forward checking detects a dead end one step earlier than plain backtracking, when a variable's last value is ruled out rather than when that variable's turn comes. It looks only at constraints between the new value and unassigned variables, not at constraints among unassigned variables; arc consistency (@sec-ai-constraint-satisfaction-arc-consistency) does the latter.

::: {#def-mrv-lcv .definition name="Minimum remaining values, least constraining value"}

*Minimum remaining values* (MRV) chooses as the next variable one with the fewest values left in its (filtered) domain. *Least constraining value* (LCV) tries the values of the chosen variable in increasing order of the number of values they would remove from the domains of the unassigned neighbours.

:::

The two rules pull in opposite directions on purpose. Every variable has to be assigned eventually, so MRV picks the one most likely to fail and finds a doomed branch early (it is also called *fail-first*). Only one value of a variable is needed, so LCV tries first the value most likely to leave room for a solution. LCV costs extra filtering work for each value and pays off mostly when a solution is wanted quickly; MRV almost always pays off.

::: {#exm-backtracking-four-queens .example name="Backtracking on 4-queens"}

Take @exm-n-queens-csp with $N=4$, variables in the order $Q_1,\dots,Q_4$ and values in increasing order.

- *Plain backtracking* assigns $Q_1=1$, $Q_2=3$; no row is consistent for $Q_3$, so it tries $Q_2=4$, then $Q_3=2$; no row is left for $Q_4$, and both $Q_3$ and $Q_2$ are exhausted. It returns to $Q_1=2$ and then succeeds with $Q_2=4$, $Q_3=1$, $Q_4=3$: eight assignments in all.
- *With forward checking*, $Q_1=1$ leaves the domains $Q_2\in\{3,4\}$, $Q_3\in\{2,4\}$, $Q_4\in\{2,3\}$. Then $Q_2=3$ empties the domain of $Q_3$ at once, without trying any value for $Q_3$; $Q_2=4$ leaves $Q_3\in\{2\}$, $Q_4\in\{3\}$, and $Q_3=2$ empties $Q_4$. After $Q_1=2$ the domains are $Q_2\in\{4\}$, $Q_3\in\{1,3\}$, $Q_4\in\{1,3,4\}$, and the search proceeds without a dead end.
- *With MRV* (and forward checking) the order happens to be the same here: after $Q_1=2$, the variable $Q_2$ with one value left is chosen first.

:::

::: {#fig-backtracking-search-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\draw[cell frame] (0.00,0.00) rectangle (0.38,0.38);
\draw[cell frame] (0.00,0.38) rectangle (0.38,0.76);
\draw[cell frame] (0.00,0.76) rectangle (0.38,1.14);
\draw[cell frame] (0.00,1.14) rectangle (0.38,1.52);
\draw[cell frame] (0.38,0.00) rectangle (0.76,0.38);
\draw[hl cell] (0.38,0.38) rectangle (0.76,0.76);
\draw[hl cell] (0.38,0.76) rectangle (0.76,1.14);
\draw[cell frame] (0.38,1.14) rectangle (0.76,1.52);
\draw[cell frame] (0.76,0.00) rectangle (1.14,0.38);
\draw[hl cell] (0.76,0.38) rectangle (1.14,0.76);
\draw[cell frame] (0.76,0.76) rectangle (1.14,1.14);
\draw[hl cell] (0.76,1.14) rectangle (1.14,1.52);
\draw[cell frame] (1.14,0.00) rectangle (1.52,0.38);
\draw[hl cell] (1.14,0.38) rectangle (1.52,0.76);
\draw[cell frame] (1.14,0.76) rectangle (1.52,1.14);
\draw[cell frame] (1.14,1.14) rectangle (1.52,1.52);
\node[dot] at (0.19,0.19) {};
\node[lab, tick, align=center] at (0.76,-0.32) {$Q_1=1$};
\draw[cell frame] (2.00,0.00) rectangle (2.38,0.38);
\draw[cell frame] (2.00,0.38) rectangle (2.38,0.76);
\draw[cell frame] (2.00,0.76) rectangle (2.38,1.14);
\draw[cell frame] (2.00,1.14) rectangle (2.38,1.52);
\draw[cell frame] (2.38,0.00) rectangle (2.76,0.38);
\draw[cell frame] (2.38,0.38) rectangle (2.76,0.76);
\draw[cell frame] (2.38,0.76) rectangle (2.76,1.14);
\draw[cell frame] (2.38,1.14) rectangle (2.76,1.52);
\draw[cell frame] (2.76,0.00) rectangle (3.14,0.38);
\draw[hl cell] (2.76,0.38) rectangle (3.14,0.76);
\draw[hl cell] (2.76,0.76) rectangle (3.14,1.14);
\draw[hl cell] (2.76,1.14) rectangle (3.14,1.52);
\draw[cell frame] (3.14,0.00) rectangle (3.52,0.38);
\draw[hl cell] (3.14,0.38) rectangle (3.52,0.76);
\draw[cell frame] (3.14,0.76) rectangle (3.52,1.14);
\draw[hl cell] (3.14,1.14) rectangle (3.52,1.52);
\node[dot] at (2.19,0.19) {};
\node[dot] at (2.57,0.95) {};
\node[lab, tick, align=center] at (2.76,-0.32) {$Q_2=3$\\$Q_3$ empty};
\draw[cell frame] (4.00,0.00) rectangle (4.38,0.38);
\draw[cell frame] (4.00,0.38) rectangle (4.38,0.76);
\draw[cell frame] (4.00,0.76) rectangle (4.38,1.14);
\draw[cell frame] (4.00,1.14) rectangle (4.38,1.52);
\draw[cell frame] (4.38,0.00) rectangle (4.76,0.38);
\draw[cell frame] (4.38,0.38) rectangle (4.76,0.76);
\draw[cell frame] (4.38,0.76) rectangle (4.76,1.14);
\draw[cell frame] (4.38,1.14) rectangle (4.76,1.52);
\draw[cell frame] (4.76,0.00) rectangle (5.14,0.38);
\draw[hl cell] (4.76,0.38) rectangle (5.14,0.76);
\draw[cell frame] (4.76,0.76) rectangle (5.14,1.14);
\draw[hl cell] (4.76,1.14) rectangle (5.14,1.52);
\draw[cell frame] (5.14,0.00) rectangle (5.52,0.38);
\draw[hl cell] (5.14,0.38) rectangle (5.52,0.76);
\draw[hl cell] (5.14,0.76) rectangle (5.52,1.14);
\draw[cell frame] (5.14,1.14) rectangle (5.52,1.52);
\node[dot] at (4.19,0.19) {};
\node[dot] at (4.57,1.33) {};
\node[lab, tick, align=center] at (4.76,-0.32) {$Q_2=4$};
\draw[cell frame] (6.00,0.00) rectangle (6.38,0.38);
\draw[cell frame] (6.00,0.38) rectangle (6.38,0.76);
\draw[cell frame] (6.00,0.76) rectangle (6.38,1.14);
\draw[cell frame] (6.00,1.14) rectangle (6.38,1.52);
\draw[cell frame] (6.38,0.00) rectangle (6.76,0.38);
\draw[cell frame] (6.38,0.38) rectangle (6.76,0.76);
\draw[cell frame] (6.38,0.76) rectangle (6.76,1.14);
\draw[cell frame] (6.38,1.14) rectangle (6.76,1.52);
\draw[cell frame] (6.76,0.00) rectangle (7.14,0.38);
\draw[cell frame] (6.76,0.38) rectangle (7.14,0.76);
\draw[cell frame] (6.76,0.76) rectangle (7.14,1.14);
\draw[cell frame] (6.76,1.14) rectangle (7.14,1.52);
\draw[cell frame] (7.14,0.00) rectangle (7.52,0.38);
\draw[hl cell] (7.14,0.38) rectangle (7.52,0.76);
\draw[hl cell] (7.14,0.76) rectangle (7.52,1.14);
\draw[hl cell] (7.14,1.14) rectangle (7.52,1.52);
\node[dot] at (6.19,0.19) {};
\node[dot] at (6.57,1.33) {};
\node[dot] at (6.95,0.57) {};
\node[lab, tick, align=center] at (6.76,-0.32) {$Q_3=2$\\$Q_4$ empty};
\draw[cell frame] (0.00,-2.60) rectangle (0.38,-2.22);
\draw[cell frame] (0.00,-2.22) rectangle (0.38,-1.84);
\draw[cell frame] (0.00,-1.84) rectangle (0.38,-1.46);
\draw[cell frame] (0.00,-1.46) rectangle (0.38,-1.08);
\draw[cell frame] (0.38,-2.60) rectangle (0.76,-2.22);
\draw[hl cell] (0.38,-2.22) rectangle (0.76,-1.84);
\draw[hl cell] (0.38,-1.84) rectangle (0.76,-1.46);
\draw[hl cell] (0.38,-1.46) rectangle (0.76,-1.08);
\draw[cell frame] (0.76,-2.60) rectangle (1.14,-2.22);
\draw[cell frame] (0.76,-2.22) rectangle (1.14,-1.84);
\draw[hl cell] (0.76,-1.84) rectangle (1.14,-1.46);
\draw[cell frame] (0.76,-1.46) rectangle (1.14,-1.08);
\draw[cell frame] (1.14,-2.60) rectangle (1.52,-2.22);
\draw[cell frame] (1.14,-2.22) rectangle (1.52,-1.84);
\draw[hl cell] (1.14,-1.84) rectangle (1.52,-1.46);
\draw[cell frame] (1.14,-1.46) rectangle (1.52,-1.08);
\node[dot] at (0.19,-2.03) {};
\node[lab, tick, align=center] at (0.76,-2.92) {$Q_1=2$};
\draw[cell frame] (2.00,-2.60) rectangle (2.38,-2.22);
\draw[cell frame] (2.00,-2.22) rectangle (2.38,-1.84);
\draw[cell frame] (2.00,-1.84) rectangle (2.38,-1.46);
\draw[cell frame] (2.00,-1.46) rectangle (2.38,-1.08);
\draw[cell frame] (2.38,-2.60) rectangle (2.76,-2.22);
\draw[cell frame] (2.38,-2.22) rectangle (2.76,-1.84);
\draw[cell frame] (2.38,-1.84) rectangle (2.76,-1.46);
\draw[cell frame] (2.38,-1.46) rectangle (2.76,-1.08);
\draw[cell frame] (2.76,-2.60) rectangle (3.14,-2.22);
\draw[cell frame] (2.76,-2.22) rectangle (3.14,-1.84);
\draw[hl cell] (2.76,-1.84) rectangle (3.14,-1.46);
\draw[hl cell] (2.76,-1.46) rectangle (3.14,-1.08);
\draw[cell frame] (3.14,-2.60) rectangle (3.52,-2.22);
\draw[cell frame] (3.14,-2.22) rectangle (3.52,-1.84);
\draw[hl cell] (3.14,-1.84) rectangle (3.52,-1.46);
\draw[cell frame] (3.14,-1.46) rectangle (3.52,-1.08);
\node[dot] at (2.19,-2.03) {};
\node[dot] at (2.57,-1.27) {};
\node[lab, tick, align=center] at (2.76,-2.92) {$Q_2=4$};
\draw[cell frame] (4.00,-2.60) rectangle (4.38,-2.22);
\draw[cell frame] (4.00,-2.22) rectangle (4.38,-1.84);
\draw[cell frame] (4.00,-1.84) rectangle (4.38,-1.46);
\draw[cell frame] (4.00,-1.46) rectangle (4.38,-1.08);
\draw[cell frame] (4.38,-2.60) rectangle (4.76,-2.22);
\draw[cell frame] (4.38,-2.22) rectangle (4.76,-1.84);
\draw[cell frame] (4.38,-1.84) rectangle (4.76,-1.46);
\draw[cell frame] (4.38,-1.46) rectangle (4.76,-1.08);
\draw[cell frame] (4.76,-2.60) rectangle (5.14,-2.22);
\draw[cell frame] (4.76,-2.22) rectangle (5.14,-1.84);
\draw[cell frame] (4.76,-1.84) rectangle (5.14,-1.46);
\draw[cell frame] (4.76,-1.46) rectangle (5.14,-1.08);
\draw[cell frame] (5.14,-2.60) rectangle (5.52,-2.22);
\draw[hl cell] (5.14,-2.22) rectangle (5.52,-1.84);
\draw[hl cell] (5.14,-1.84) rectangle (5.52,-1.46);
\draw[cell frame] (5.14,-1.46) rectangle (5.52,-1.08);
\node[dot] at (4.19,-2.03) {};
\node[dot] at (4.57,-1.27) {};
\node[dot] at (4.95,-2.41) {};
\node[lab, tick, align=center] at (4.76,-2.92) {$Q_3=1$};
\draw[cell frame] (6.00,-2.60) rectangle (6.38,-2.22);
\draw[cell frame] (6.00,-2.22) rectangle (6.38,-1.84);
\draw[cell frame] (6.00,-1.84) rectangle (6.38,-1.46);
\draw[cell frame] (6.00,-1.46) rectangle (6.38,-1.08);
\draw[cell frame] (6.38,-2.60) rectangle (6.76,-2.22);
\draw[cell frame] (6.38,-2.22) rectangle (6.76,-1.84);
\draw[cell frame] (6.38,-1.84) rectangle (6.76,-1.46);
\draw[cell frame] (6.38,-1.46) rectangle (6.76,-1.08);
\draw[cell frame] (6.76,-2.60) rectangle (7.14,-2.22);
\draw[cell frame] (6.76,-2.22) rectangle (7.14,-1.84);
\draw[cell frame] (6.76,-1.84) rectangle (7.14,-1.46);
\draw[cell frame] (6.76,-1.46) rectangle (7.14,-1.08);
\draw[cell frame] (7.14,-2.60) rectangle (7.52,-2.22);
\draw[cell frame] (7.14,-2.22) rectangle (7.52,-1.84);
\draw[cell frame] (7.14,-1.84) rectangle (7.52,-1.46);
\draw[cell frame] (7.14,-1.46) rectangle (7.52,-1.08);
\node[dot] at (6.19,-2.03) {};
\node[dot] at (6.57,-1.27) {};
\node[dot] at (6.95,-2.41) {};
\node[dot] at (7.33,-1.65) {};
\node[lab, tick, align=center] at (6.76,-2.92) {$Q_4=3$};
\end{tikzpicture}
\end{center}
```

Backtracking with forward checking on 4-queens (@exm-backtracking-four-queens). Columns are the variables $Q_1,\dots,Q_4$ and rows their values, row $1$ at the bottom; shaded squares are values that forward checking has removed from the unassigned columns. The first two branches end when a column has no square left; the search then returns to $Q_1=2$ and succeeds.

:::
