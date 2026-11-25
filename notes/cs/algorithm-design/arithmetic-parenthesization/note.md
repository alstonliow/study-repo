---
title: "Arithmetic Parenthesization"
sources: [mit6006-17, mit6006r-17]
requires: [cs/algorithm-design/more-dynamic-programs]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.006 (Spring 2020), Lecture 17 and Recitation 17, in our own wording; examples our own (checked by computation); proofs written out in steps. Split from cs/algorithm-design/more-dynamic-programs on 2026-11-25 (one problem per note, SPEC §8.6). -->

Substring subproblems, expanded with two goals: the largest and the smallest value.

::: {#exm-arithmetic-parenthesization .example name="Arithmetic parenthesization"}

Given an expression $a_0\ast_1a_1\ast_2\cdots\ast_{n-1}a_{n-1}$ with integers $a_i$ (possibly negative) and operations $\ast_i\in\{+,\times\}$, place parentheses to make its value as large as possible. For $2\times(-3)+1\times(-4)$ the best is $\bigl(2\times(-3)+1\bigr)\times(-4)=20$.

Maximising each part is not enough: $(-3)\times(-3)>(-2)\times(-2)$, so a large product may need two very *negative* factors. So we expand the subproblems with both goals.

1. *Subproblems:* $x(i,j,\mathrm{opt})$, the minimum ($\mathrm{opt}=\min$) or maximum ($\mathrm{opt}=\max$) value of $a_i\ast_{i+1}\cdots\ast_{j-1}a_{j-1}$ over all parenthesizations, for $0\le i<j\le n$.
2. *Relation:* guess the operation $\ast_k$ evaluated last, and the extreme of each side:
   $$x(i,j,\mathrm{opt})=\mathrm{opt}\bigl\{x(i,k,\mathrm{opt}')\ast_kx(k,j,\mathrm{opt}''):i<k<j;\ \mathrm{opt}',\mathrm{opt}''\in\{\min,\max\}\bigr\}.$$
   This is right because the left side ranges over values in $[x(i,k,\min),x(i,k,\max)]$ and the right side over $[x(k,j,\min),x(k,j,\max)]$, and $l+r$ and $l\times r$ are linear in each argument separately, so their extremes over such a rectangle are reached at its corners.
3. *Order:* increasing $j-i$. 4. *Base:* $x(i,i+1,\mathrm{opt})=a_i$.
5. *Original:* $x(0,n,\max)$; parent pointers (two per subproblem) give the parenthesization as a binary tree.
6. *Time:* $O(n^2)$ subproblems with $O(n)$ work each: $O(n^3)$.

In the example, $x(0,4,\min)=-14$, from $2\times\bigl(-3+1\times(-4)\bigr)$.

:::

```{=latex}
\begin{algorithm}
\caption{Arithmetic parenthesization}
\begin{algorithmic}
\INPUT Integers $a_0,\dots,a_{n-1}$ and operations $\ast_1,\dots,\ast_{n-1}\in\{+,\times\}$
\OUTPUT The largest value $x(0,n,\max)$
\FOR{$i=0$ to $n-1$}
    \STATE $x(i,i+1,\min)\gets a_i$; $x(i,i+1,\max)\gets a_i$
\ENDFOR
\FOR{$\ell=2$ to $n$}
    \FOR{$i=0$ to $n-\ell$}
        \STATE $j\gets i+\ell$
        \STATE $C\gets\{x(i,k,o')\ast_kx(k,j,o''):i<k<j;\ o',o''\in\{\min,\max\}\}$
        \STATE $x(i,j,\min)\gets\min C$; $x(i,j,\max)\gets\max C$
    \ENDFOR
\ENDFOR
\RETURN $x(0,n,\max)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-more-dynamic-programs-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (1.050,1.050);
\node[lab] at (0.525,0.525) {$2,2$};
\draw[cell frame] (1.050,0.000) rectangle (2.100,1.050);
\node[lab] at (1.575,0.525) {$-6,-6$};
\draw[cell frame] (2.100,0.000) rectangle (3.150,1.050);
\node[lab] at (2.625,0.525) {$-5,-4$};
\draw[hl cell] (3.150,0.000) rectangle (4.200,1.050);
\node[lab] at (3.675,0.525) {$-14,20$};
\node[lab,tick,anchor=east] at (-0.050,0.525) {$i=0$};
\draw[cell frame] (1.050,-1.050) rectangle (2.100,0.000);
\node[lab] at (1.575,-0.525) {$-3,-3$};
\draw[cell frame] (2.100,-1.050) rectangle (3.150,0.000);
\node[lab] at (2.625,-0.525) {$-2,-2$};
\draw[cell frame] (3.150,-1.050) rectangle (4.200,0.000);
\node[lab] at (3.675,-0.525) {$-7,8$};
\node[lab,tick,anchor=east] at (-0.050,-0.525) {$i=1$};
\draw[cell frame] (2.100,-2.100) rectangle (3.150,-1.050);
\node[lab] at (2.625,-1.575) {$1,1$};
\draw[cell frame] (3.150,-2.100) rectangle (4.200,-1.050);
\node[lab] at (3.675,-1.575) {$-4,-4$};
\node[lab,tick,anchor=east] at (-0.050,-1.575) {$i=2$};
\draw[cell frame] (3.150,-3.150) rectangle (4.200,-2.100);
\node[lab] at (3.675,-2.625) {$-4,-4$};
\node[lab,tick,anchor=east] at (-0.050,-2.625) {$i=3$};
\node[lab,tick] at (0.525,1.230) {$j=1$};
\node[lab,tick] at (1.575,1.230) {$j=2$};
\node[lab,tick] at (2.625,1.230) {$j=3$};
\node[lab,tick] at (3.675,1.230) {$j=4$};
\end{tikzpicture}
\end{center}
```

The table for $2\times(-3)+1\times(-4)$: the cell $(i,j)$ holds $x(i,j,\min),x(i,j,\max)$ for $a_i\ast\cdots a_{j-1}$, filled by increasing $j-i$ from the diagonal $x(i,i+1,\cdot)=a_i$. The answer is $x(0,4,\max)=20$. It needs the *minimum* $-5$ of $2\times(-3)+1$ (cell $(0,3)$) times $-4$; the maximum of that part, $-4$, would give only $16$.

:::
