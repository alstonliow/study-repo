---
title: "The Radon–Nikodym Theorem by Martingales"
sources: [camiii-ap-2]
requires: [math/probability/martingales/lp-and-l1-martingale-convergence]
status: draft
---

<!-- Added 2026-11-28 from Cambridge Part III Advanced Probability (lecture notes), Section 2.4, in our own wording; proofs written out in steps. -->

If $\nu(A)=\mu(f\mathbf 1_A)$ for a density $f\ge0$, then $\mu(A)=0$ forces $\nu(A)=0$. The converse needs a condition: with $\mu$ the counting measure on $\mathbb R$ and $\nu$ Lebesgue measure, $\nu\ll\mu$ but no density exists (a density would vanish at every point), because $\mu$ is not σ-finite. For probability measures the converse holds, and a martingale built from finer and finer partitions produces the density.

::: {#thm-radon-nikodym .theorem name="Radon–Nikodym theorem"}

Let $P,Q$ be probability measures on $(\Omega,\mathcal F)$. The following are equivalent:

1. $Q\ll P$: $P(A)=0\Rightarrow Q(A)=0$ for $A\in\mathcal F$.
2. For every $\varepsilon>0$ there is $\delta>0$ with $P(A)\le\delta\Rightarrow Q(A)\le\varepsilon$.
3. There is a random variable $X\ge0$ with $Q(A)=E_P[X\mathbf 1_A]$ for all $A$.

Then $X=\frac{dQ}{dP}$ is the *Radon–Nikodym derivative*. By scaling the theorem holds for finite measures, and by partitioning $\Omega$ for σ-finite ones.

:::

::: {.proof}

We treat $\mathcal F$ countably generated, $\mathcal F=\sigma(F_1,F_2,\dots)$.

1. *(3)⇒(1)* is clear.

2. *(2)⇒(3).* Let $\mathcal F_n=\sigma(F_1,\dots,F_n)$, a finite σ-algebra with atoms $A_{n,1},\dots,A_{n,m_n}$. Define $X_n=\sum_i\frac{Q(A_{n,i})}{P(A_{n,i})}\mathbf 1_{A_{n,i}}$, omitting atoms with $P(A_{n,i})=0$. Then $E_P[X_n\mathbf 1_A]=Q(A)$ for all $A\in\mathcal F_n$.

3. For $A\in\mathcal F_n\subseteq\mathcal F_{n+1}$: $E[X_{n+1}\mathbf 1_A]=Q(A)=E[X_n\mathbf 1_A]$. So $E[X_{n+1}\mid\mathcal F_n]=X_n$ and $(X_n)$ is a martingale.

4. $(X_n)$ is UI: $E[X_n]=1$, so for $\lambda>1/\delta$, $P(X_n\ge\lambda)\le1/\lambda\le\delta$, and then $E[X_n\mathbf 1_{\{X_n\ge\lambda\}}]=Q(X_n\ge\lambda)\le\varepsilon$ (this uses $\{X_n\ge\lambda\}\in\mathcal F_n$).

5. By @thm-l1-martingale-convergence, $X_n\to X$ a.s. and in $L^1$. For $A\in\bigcup_n\mathcal F_n$, $Q(A)=\lim E[X_n\mathbf 1_A]=E[X\mathbf 1_A]$. Both sides are measures on $\mathcal F$ agreeing on the generating π-system $\bigcup_n\mathcal F_n$ and on $\Omega$, so they agree on $\mathcal F$.

6. *(1)⇒(2).* Suppose (2) fails: there are $\varepsilon>0$ and $A_n$ with $Q(A_n)\ge\varepsilon$ and $P(A_n)\le2^{-n}$. Then $\sum P(A_n)<\infty$, so by Borel–Cantelli $P(\limsup A_n)=0$. But $Q(\limsup A_n)=\lim_kQ(\bigcup_{m\ge k}A_m)\ge\varepsilon$, contradicting (1).

:::

::: {#fig-radon-nikodym-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-0.2,0) -- (8.2,0);
\draw[emph] (0,1.0) .. controls (2,2.6) and (3,0.2) .. (4,1.6) .. controls (5,2.6) and (6,0.6) .. (8,1.2);
\draw[hl] (0,0.9) -- (2,0.9) -- (2,1.5) -- (4,1.5) -- (4,1.6) -- (6,1.6) -- (6,1.0) -- (8,1.0);
\foreach \x in {0,2,4,6,8} {\draw[faint] (\x,0) -- (\x,0.15);}
\node[tick] at (4,-0.35) {$\mathcal F_n$ atoms};
\node[lab, text=accent] at (6.9,2.4) {$X_n\to dQ/dP$};
\end{tikzpicture}
\end{center}
```

The martingale $X_n$ is the ratio $Q/P$ on each atom of $\mathcal F_n$: a staircase approximation of the density.

:::

::: {#rmk-radon-nikodym-1 .remark name="Merge candidate"}

@sec-math-analysis-measure-theory-lebesgue-integral states measures with a density (@prp-density-measure) but not the Radon–Nikodym theorem itself; this note is its only proof in the repository.

:::
