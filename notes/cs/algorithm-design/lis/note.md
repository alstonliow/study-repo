---
title: "Longest Increasing Subsequence"
sources: [mit6006-16, mit6006r-16, mit6046r-5]
requires: [cs/algorithm-design/subproblem-design]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 16 and Recitation 16, and (stacking blocks) MIT 6.046 (Spring 2015), Recitation 5, in our own wording; examples our own (checked by computation). Split from cs/algorithm-design/subproblem-design on 2026-11-25, with stacking blocks from cs/algorithm-design/interval-subproblems as a variant (one problem per note, SPEC §8.6; owner decision 2026-11-25). -->

When the natural suffix subproblem does not combine, *constrain* it: ask for the best solution that starts at a given element.

::: {#exm-lis .example name="Longest increasing subsequence"}

Given a sequence $A$, find a longest strictly increasing subsequence. For $5,2,8,6,3,6,9,7$ one answer is $2,3,6,9$, of length $4$.

The natural subproblem "a longest increasing subsequence of $A[i:]$" does not combine well: knowing such a subsequence of $A[i+1:]$ does not tell us whether $A[i]$ can be put in front. So we *constrain* the subproblem to start at $A[i]$.

1. *Subproblems:* $x(i)$, the length of a longest increasing subsequence of $A[i:]$ that *starts with* $A[i]$, for $0\le i<|A|$.
2. *Relation:* guess the second element:
   $$x(i)=\max\bigl(\{1+x(j):i<j<|A|,\ A[j]>A[i]\}\cup\{1\}\bigr),$$
   where $1$ is the case that $A[i]$ is the last element.
3. *Order:* decreasing $i$. 4. *Base:* none needed (the option $1$ covers the end).
5. *Original:* $\max_ix(i)$ (guess the first element), with parent pointers to recover a subsequence.
6. *Time:* $|A|$ subproblems with $O(|A|)$ work each: $O(|A|^2)$. (With an augmented balanced search tree the work per subproblem drops to $O(\log|A|)$.)

:::

```{=latex}
\begin{algorithm}
\caption{Longest increasing subsequence}
\begin{algorithmic}
\INPUT A sequence $A$ of length $n\ge1$
\OUTPUT The length of a longest increasing subsequence
\FOR{$i=n-1$ down to $0$}
    \STATE $x(i)\gets1$
    \FOR{$j=i+1$ to $n-1$}
        \IF{$A[j]>A[i]$ and $1+x(j)>x(i)$}
            \STATE $x(i)\gets1+x(j)$; $\mathrm{next}(i)\gets j$ \COMMENT{parent pointer}
        \ENDIF
    \ENDFOR
\ENDFOR
\RETURN $\max_ix(i)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-subproblem-design-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.700,0.700);
\node[lab] at (0.350,0.350) {$5$};
\draw[hl cell] (0.700,0.000) rectangle (1.400,0.700);
\node[lab] at (1.050,0.350) {$2$};
\draw[cell frame] (1.400,0.000) rectangle (2.100,0.700);
\node[lab] at (1.750,0.350) {$8$};
\draw[cell frame] (2.100,0.000) rectangle (2.800,0.700);
\node[lab] at (2.450,0.350) {$6$};
\draw[hl cell] (2.800,0.000) rectangle (3.500,0.700);
\node[lab] at (3.150,0.350) {$3$};
\draw[hl cell] (3.500,0.000) rectangle (4.200,0.700);
\node[lab] at (3.850,0.350) {$6$};
\draw[hl cell] (4.200,0.000) rectangle (4.900,0.700);
\node[lab] at (4.550,0.350) {$9$};
\draw[cell frame] (4.900,0.000) rectangle (5.600,0.700);
\node[lab] at (5.250,0.350) {$7$};
\node[lab, anchor=east] at (-0.100,0.350) {$A$};
\node[lab,tick] at (0.35,-0.3) {3};
\node[lab,tick] at (1.05,-0.3) {4};
\node[lab,tick] at (1.75,-0.3) {2};
\node[lab,tick] at (2.45,-0.3) {2};
\node[lab,tick] at (3.15,-0.3) {3};
\node[lab,tick] at (3.85,-0.3) {2};
\node[lab,tick] at (4.55,-0.3) {1};
\node[lab,tick] at (5.25,-0.3) {1};
\draw[->] (1.05,0.75) to[bend left=35] (3.15,0.75);
\draw[->] (3.15,0.75) to[bend left=35] (3.85,0.75);
\draw[->] (3.85,0.75) to[bend left=35] (4.55,0.75);
\node[lab,tick, anchor=east] at (-0.1,-0.3) {$x(i)$};
\end{tikzpicture}
\end{center}
```

Longest increasing subsequence of $5,2,8,6,3,6,9,7$. Under each item is $x(i)$, the length of a longest increasing subsequence starting there, computed from right to left. The maximum, $4$, is at $2$, and following the choices (arrows) gives $2,3,6,9$.

:::

## Stacking blocks

::: {#exm-stacking-blocks .example name="Stacking blocks"}

Given boxes with dimensions $(\ell_i,w_i,h_i)$, each usable in any rotation and any number of times, build the tallest tower in which every box sits on one whose base is strictly larger in both directions. List each box in its three rotations (taking $\ell\ge w$), sort the $3n$ oriented boxes by base area, and let $x(i)$ be the tallest tower with oriented box $i$ on top: $x(i)=h_i+\max\{x(j):\ell_j>\ell_i,\ w_j>w_i\}$ (or $h_i$ alone). This is a longest path in a DAG, $O(n^2)$ time, like the longest increasing subsequence (@exm-lis).

:::

```{=latex}
\begin{algorithm}
\caption{Stacking blocks}
\begin{algorithmic}
\INPUT Boxes $(\ell_i,w_i,h_i)$, $i=1,\dots,n$
\OUTPUT The height of a tallest tower
\STATE list the $3n$ oriented boxes (each dimension once as the height, base $\ell\ge w$)
\STATE sort them by decreasing base area $\ell w$, as $b_1,\dots,b_{3n}$
\FOR{$i=1$ to $3n$}
    \STATE $x(i)\gets h_i$
    \FOR{$j=1$ to $i-1$}
        \IF{$\ell_j>\ell_i$ and $w_j>w_i$}
            \STATE $x(i)\gets\max\{x(i),\ h_i+x(j)\}$
        \ENDIF
    \ENDFOR
\ENDFOR
\RETURN $\max_ix(i)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-interval-subproblems-5}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[lab,tick] at (0.00,0.00) {$(4,3,2)$};
\node[lab,tick] at (1.30,0.00) {$12$};
\node[lab,tick] at (2.40,0.00) {$2$};
\node[lab,tick] at (0.00,-0.60) {$(4,2,3)$};
\node[lab,tick] at (1.30,-0.60) {$8$};
\node[lab,tick] at (2.40,-0.60) {$3$};
\node[lab,tick] at (0.00,-1.20) {$(3,2,4)$};
\node[lab,tick] at (1.30,-1.20) {$6$};
\node[lab,tick] at (2.40,-1.20) {$6$};
\node[lab,tick] at (0.00,0.55) {$(\ell,w,h)$};
\node[lab,tick] at (1.30,0.55) {$\ell w$};
\node[lab,tick] at (2.40,0.55) {$x(i)$};
\draw[faint] (-0.7,0.33) -- (2.8,0.33);
\draw[hl box] (3.80,-1.00) rectangle (5.20,-0.30);
\node[lab,tick,anchor=west] at (5.30,-0.65) {base $4\times3$, height $2$};
\draw[hl box] (3.98,-0.30) rectangle (5.03,1.10);
\node[lab,tick,anchor=west] at (5.12,0.40) {base $3\times2$, height $4$};
\draw[faint] (3.50,-1.0) -- (5.50,-1.0);
\end{tikzpicture}
\end{center}
```

Stacking copies of one $4\times3\times2$ box. Its three orientations, sorted by base area, with $x(i)$, the tallest tower having that orientation on top. Only the base $4\times3$ is strictly larger in both directions than the base $3\times2$, so the best tower (right) puts the box lying flat at the bottom and standing on its $3\times2$ face on top: height $2+4=6$.

:::
