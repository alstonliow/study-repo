---
title: "coNP ⊆ IP: Arithmetization and the Sumcheck Protocol"
sources: [mit18404j-25, mit18404j-26]
requires: [cs/theory/interactive-proofs, cs/theory/branching-programs]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lectures 25 and 26, in our own wording; proofs written out in steps. -->

The prover will convince the verifier of the *number* of satisfying assignments of a formula. The number $0$ certifies unsatisfiability, so $\overline{\mathit{SAT}}$, which is coNP-complete, gets an interactive proof.

::: {#def-sharp-sat .definition name="Counting satisfying assignments"}

For a Boolean formula $\phi$ let $\#\phi$ be its number of satisfying assignments, and $\#\mathit{SAT}=\{\langle\phi,k\rangle: \#\phi=k\}$.

:::

::: {#def-arithmetize-formula .definition name="Arithmetization of a formula"}

Over a field $\mathbb F_q$, replace each part of $\phi$ by a polynomial:

$$
a\wedge b\mapsto ab,\qquad \neg a\mapsto 1-a,\qquad a\vee b\mapsto a+b-ab.
$$

The resulting polynomial $p(x_1,\dots,x_m)$ agrees with $\phi$ on $\{0,1\}^m$ ($1$ for true, $0$ for false), and its degree is at most the size $n$ of $\phi$. Hence

$$
\#\phi=\sum_{x_1,\dots,x_m\in\{0,1\}}p(x_1,\dots,x_m).
$$

:::

This is the same idea as for branching programs (@def-arithmetization-bp): extend a Boolean function to a low-degree polynomial on a large field, where two different polynomials rarely agree.

::: {#thm-sharp-sat-ip .theorem name="#SAT has an interactive proof"}

$\#\mathit{SAT}\in\mathrm{IP}$.

:::

::: {.proof}

1. Take a prime $q>2^n$ larger than the formula size cubed, so that counts are exact in $\mathbb F_q$ and $n/q$ is small. For $0\le i\le m$ define, for fixed $r_1,\dots,r_{i-1}$ chosen during the protocol,

$$
T_i(z)=\sum_{x_{i+1},\dots,x_m\in\{0,1\}}p(r_1,\dots,r_{i-1},z,x_{i+1},\dots,x_m),
$$

a polynomial in one variable of degree at most $n$. Then $T_1(0)+T_1(1)=\#\phi$.

2. *Protocol (sumcheck).* Round 1: $P$ sends the coefficients of $T_1$; $V$ checks $T_1(0)+T_1(1)=k$ and picks a random $r_1\in\mathbb F_q$. Round $i$ ($2\le i\le m$): $P$ sends $T_i$; $V$ checks $T_i(0)+T_i(1)=T_{i-1}(r_{i-1})$ and picks a random $r_i$. Finally $V$ checks $T_m(r_m)=p(r_1,\dots,r_m)$, which it computes itself. $V$ accepts iff all checks pass.

3. *Completeness.* An honest prover sends the true polynomials, and all checks pass.

4. *Soundness.* Let $k\ne\#\phi$. To pass round 1 the prover must send some $\tilde T_1\ne T_1$. If a round starts with a false polynomial $\tilde T_i\ne T_i$, then $\tilde T_i(r_i)=T_i(r_i)$ has probability at most $n/q$ (@lem-poly-roots, applied to $\tilde T_i-T_i$); otherwise the next claimed value $\tilde T_i(r_i)$ is false, and to pass the next check the prover must send a false $\tilde T_{i+1}$.

5. If the prover is never lucky, the final check compares a false $\tilde T_m(r_m)$ with the true value $p(r_1,\dots,r_m)$ and fails. So $V$ accepts with probability at most $mn/q$, which is below $\tfrac13$ by the choice of $q$.

6. $V$ runs in polynomial time: there are $m$ rounds, each polynomial has $n+1$ coefficients in $\mathbb F_q$, and evaluating $p$ at a point follows the formula.

:::

```{=latex}
\begin{algorithm}
\caption{Sumcheck verifier for $\langle\phi,k\rangle$}
\begin{algorithmic}
\INPUT formula $\phi$ with arithmetization $p(x_1,\dots,x_m)$ over $\mathbb F_q$, claimed count $k$
\STATE $v\gets k$
\FOR{$i=1$ \TO $m$}
    \STATE receive a polynomial $T_i$ of degree at most $n$ from the prover
    \STATE \textbf{if} $T_i(0)+T_i(1)\ne v$ \textbf{then} reject
    \STATE pick $r_i\in\mathbb F_q$ uniformly at random and send it; $v\gets T_i(r_i)$
\ENDFOR
\RETURN accept iff $v=p(r_1,\dots,r_m)$
\end{algorithmic}
\end{algorithm}
```

::: {#cor-conp-in-ip .corollary name="$\mathrm{coNP}\subseteq\mathrm{IP}$"}

:::

::: {.proof}

1. $\phi$ is unsatisfiable iff $\langle\phi,0\rangle\in\#\mathit{SAT}$, so $\overline{\mathit{SAT}}\in\mathrm{IP}$ by @thm-sharp-sat-ip.

2. Every $A\in\mathrm{coNP}$ has $A\le_{\mathrm p}\overline{\mathit{SAT}}$ (complement the reduction of @thm-cook-levin). The verifier applies the reduction first and then runs the protocol.

:::

::: {#exm-sumcheck .example name="A run of the protocol"}

Let $\phi=(x_1\vee x_2)\wedge\neg x_1$, so $p=(x_1+x_2-x_1x_2)(1-x_1)$ and $\#\phi=1$ (only $x_1=0,x_2=1$). Work in $\mathbb F_7$ for illustration.

1. $T_1(z)=p(z,0)+p(z,1)=z(1-z)+(1-z)=1-z^2$, and $T_1(0)+T_1(1)=1+0=1$. $V$ picks $r_1=3$; $T_1(3)=-8\equiv6$.
2. $T_2(z)=p(3,z)=(3-2z)(-2)=4z-6$, and $T_2(0)+T_2(1)=1+5=6\equiv T_1(3)$. $V$ picks $r_2=5$.
3. $T_2(5)=14\equiv0$, and $V$ computes $p(3,5)=(3+5-15)(1-3)=14\equiv0$. All checks pass.

:::

::: {#fig-conp-in-ip-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[y=0.95cm]
\node[box] (v) at (0,0.6) {$V$};
\node[hl box] (p) at (7,0.6) {$P$};
\draw[faint] (0,0.2) -- (0,-4.3); \draw[faint] (7,0.2) -- (7,-4.3);
\draw[map] (7,-0.2) -- node[lab, note, above] {$T_1(z)=1-z^2$} (0,-0.2);
\node[lab, note, anchor=east] at (-0.2,-0.2) {$T_1(0)+T_1(1)=1=k$?};
\draw[map] (0,-1.1) -- node[lab, note, above] {$r_1=3$} (7,-1.1);
\draw[map] (7,-2.0) -- node[lab, note, above] {$T_2(z)=4z-6$} (0,-2.0);
\node[lab, note, anchor=east] at (-0.2,-2.0) {$T_2(0)+T_2(1)=T_1(3)$?};
\draw[map] (0,-2.9) -- node[lab, note, above] {$r_2=5$} (7,-2.9);
\node[lab, note, anchor=east] at (-0.2,-3.8) {$T_2(5)=p(3,5)$?};
\node[lab, note] at (3.5,-3.8) {$V$ evaluates $p$ itself};
\end{tikzpicture}
\end{center}
```

The messages of @exm-sumcheck over $\mathbb F_7$. Each round the prover commits to a one-variable polynomial, and the verifier checks it against the previous claim and fixes one more variable at random.

:::
