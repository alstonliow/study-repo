---
title: "Strassen's Matrix Multiplication"
sources: [mit6046-2, mit6046r-1]
requires: [cs/algorithms/divide-and-conquer]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 2 and Recitation 1, in our own wording; proofs written out in steps. Split from cs/algorithms/divide-and-conquer on 2026-11-25 (one algorithm per note, SPEC §8.6). -->

Multiplying two $n\times n$ matrices from the definition takes $\Theta(n^3)$ operations. Splitting each into four $\frac n2\times\frac n2$ blocks and multiplying blocks naively uses $8$ block products, $T(n)=8T(n/2)+O(n^2)=\Theta(n^3)$: no gain.

::: {#thm-strassen .theorem name="Strassen"}

Seven block products suffice, so two $n\times n$ matrices can be multiplied in $O(n^{\log_27})=O(n^{2.81})$ time.

:::

::: {.proof}

1. With $A=\begin{pmatrix}A_{11}&A_{12}\\A_{21}&A_{22}\end{pmatrix}$ and $B$ likewise, form
   $M_1=(A_{11}+A_{22})(B_{11}+B_{22})$, $M_2=(A_{21}+A_{22})B_{11}$, $M_3=A_{11}(B_{12}-B_{22})$, $M_4=A_{22}(B_{21}-B_{11})$, $M_5=(A_{11}+A_{12})B_{22}$, $M_6=(A_{21}-A_{11})(B_{11}+B_{12})$, $M_7=(A_{12}-A_{22})(B_{21}+B_{22})$.

2. Expanding shows $C_{11}=M_1+M_4-M_5+M_7$, $C_{12}=M_3+M_5$, $C_{21}=M_2+M_4$ and $C_{22}=M_1-M_2+M_3+M_6$.

3. That is $7$ products of half-size matrices and $O(n^2)$ additions: $T(n)=7T(n/2)+O(n^2)=O(n^{\log_27})$ by case 1 of the master theorem.

:::

```{=latex}
\begin{algorithm}
\caption{Strassen's algorithm}
\begin{algorithmic}
\INPUT $n\times n$ matrices $A$ and $B$, $n$ a power of $2$
\OUTPUT $C=AB$
\IF{$n=1$}
    \RETURN $(a_{11}b_{11})$
\ENDIF
\STATE split $A$ and $B$ into four $\frac n2\times\frac n2$ blocks each
\STATE compute $M_1,\dots,M_7$ as in the proof, each by a recursive call on half-size matrices
\STATE $C_{11}\gets M_1+M_4-M_5+M_7$; $C_{12}\gets M_3+M_5$
\STATE $C_{21}\gets M_2+M_4$; $C_{22}\gets M_1-M_2+M_3+M_6$
\RETURN $C$ assembled from its four blocks
\end{algorithmic}
\end{algorithm}
```

::: {#fig-divide-and-conquer-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\node[lab] at (0.275,0.275) {$1$};
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\node[lab] at (0.825,0.275) {$2$};
\draw[cell frame] (0.000,-0.550) rectangle (0.550,0.000);
\node[lab] at (0.275,-0.275) {$3$};
\draw[cell frame] (0.550,-0.550) rectangle (1.100,0.000);
\node[lab] at (0.825,-0.275) {$4$};
\node[lab,tick] at (0.55,0.85) {$A$};
\draw[cell frame] (1.600,0.000) rectangle (2.150,0.550);
\node[lab] at (1.875,0.275) {$5$};
\draw[cell frame] (2.150,0.000) rectangle (2.700,0.550);
\node[lab] at (2.425,0.275) {$6$};
\draw[cell frame] (1.600,-0.550) rectangle (2.150,0.000);
\node[lab] at (1.875,-0.275) {$7$};
\draw[cell frame] (2.150,-0.550) rectangle (2.700,0.000);
\node[lab] at (2.425,-0.275) {$8$};
\node[lab,tick] at (2.15,0.85) {$B$};
\node[lab,anchor=west] at (3.60,0.55) {$M_1=(1+4)(5+8)=65$};
\node[lab,anchor=west] at (3.60,0.13) {$M_2=(3+4)\cdot5=35$};
\node[lab,anchor=west] at (3.60,-0.29) {$M_3=1\cdot(6-8)=-2$};
\node[lab,anchor=west] at (3.60,-0.71) {$M_4=4\cdot(7-5)=8$};
\node[lab,anchor=west] at (3.60,-1.13) {$M_5=(1+2)\cdot8=24$};
\node[lab,anchor=west] at (3.60,-1.55) {$M_6=(3-1)(5+6)=22$};
\node[lab,anchor=west] at (3.60,-1.97) {$M_7=(2-4)(7+8)=-30$};
\draw[hl cell] (8.600,0.000) rectangle (9.300,0.700);
\node[lab] at (8.950,0.350) {$19$};
\draw[hl cell] (9.300,0.000) rectangle (10.000,0.700);
\node[lab] at (9.650,0.350) {$22$};
\draw[hl cell] (8.600,-0.700) rectangle (9.300,0.000);
\node[lab] at (8.950,-0.350) {$43$};
\draw[hl cell] (9.300,-0.700) rectangle (10.000,0.000);
\node[lab] at (9.650,-0.350) {$50$};
\node[lab,tick] at (9.30,0.95) {$C=AB$};
\node[lab,tick,anchor=west] at (8.00,-1.40) {$C_{11}=M_1+M_4-M_5+M_7$, $C_{12}=M_3+M_5$};
\node[lab,tick,anchor=west] at (8.00,-1.80) {$C_{21}=M_2+M_4$, $C_{22}=M_1-M_2+M_3+M_6$};
\end{tikzpicture}
\end{center}
```

Strassen's seven products on $2\times2$ matrices, where every block is a number. The products $M_1,\dots,M_7$ combine to $C=19,22;43,50$, the same as the definition gives ($1\cdot5+2\cdot7=19$, and so on), with $7$ multiplications instead of $8$. For larger $n$ the same formulas apply to $\frac n2\times\frac n2$ blocks.

:::
