---
title: "Limit Superior and Limit Inferior"
sources: [cama1-2]
requires: [math/analysis/real/sequences/monotone-sequences]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 2.5, in our own wording; proofs written out in steps. -->

Every bounded sequence has an eventual largest and smallest value in a limiting sense, even when it does not converge. These two numbers are used constantly later, for example in the root test and in measure theory.

::: {#def-limsup-liminf .definition name="Limit superior and limit inferior"}

For a bounded sequence $(a_n)$,
$$\limsup_{n\to\infty}a_n=\lim_{n\to\infty}\Bigl(\sup_{m\ge n}a_m\Bigr),\qquad \liminf_{n\to\infty}a_n=\lim_{n\to\infty}\Bigl(\inf_{m\ge n}a_m\Bigr).$$

:::

::: {#fig-limsup-and-liminf-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (6.6,0) node[lab, right] {$n$};
\draw[->, faint] (0,-0.2) -- (0,2.4) node[lab, above] {};
\node[dot] at (0.300,1.867) {};
\node[dot] at (0.600,1.306) {};
\node[dot] at (0.900,0.680) {};
\node[dot] at (1.200,0.654) {};
\node[dot] at (1.500,1.074) {};
\node[dot] at (1.800,1.307) {};
\node[dot] at (2.100,1.089) {};
\node[dot] at (2.400,0.786) {};
\node[dot] at (2.700,0.816) {};
\node[dot] at (3.000,1.095) {};
\node[dot] at (3.300,1.211) {};
\node[dot] at (3.600,1.022) {};
\node[dot] at (3.900,0.821) {};
\node[dot] at (4.200,0.888) {};
\node[dot] at (4.500,1.107) {};
\node[dot] at (4.800,1.158) {};
\node[dot] at (5.100,0.982) {};
\node[dot] at (5.400,0.843) {};
\node[dot] at (5.700,0.935) {};
\node[dot] at (6.000,1.114) {};
\draw[hl] (0.300,1.867) -- (0.600,1.307) -- (0.900,1.307) -- (1.200,1.307) -- (1.500,1.307) -- (1.800,1.307) -- (2.100,1.211) -- (2.400,1.211) -- (2.700,1.211) -- (3.000,1.211) -- (3.300,1.211) -- (3.600,1.158) -- (3.900,1.158) -- (4.200,1.158) -- (4.500,1.158) -- (4.800,1.158) -- (5.100,1.120) -- (5.400,1.120) -- (5.700,1.120) -- (6.000,1.120);
\draw[hl] (0.300,0.654) -- (0.600,0.654) -- (0.900,0.654) -- (1.200,0.654) -- (1.500,0.786) -- (1.800,0.786) -- (2.100,0.786) -- (2.400,0.786) -- (2.700,0.816) -- (3.000,0.821) -- (3.300,0.821) -- (3.600,0.821) -- (3.900,0.821) -- (4.200,0.843) -- (4.500,0.843) -- (4.800,0.843) -- (5.100,0.843) -- (5.400,0.843) -- (5.700,0.863) -- (6.000,0.863);
\node[lab, right] at (6.1,1.25) {$\sup_{m\ge n}a_m$}; \node[lab, right] at (6.1,0.8) {$\inf_{m\ge n}a_m$};
\end{tikzpicture}
\end{center}
```

The tail supremum can only fall and the tail infimum can only rise as $n$ grows, so both have limits: $\limsup a_n$ and $\liminf a_n$.

:::

Both limits exist. Let $b_n=\sup_{m\ge n}a_m$: the supremum is taken over fewer terms as $n$ grows, so $(b_n)$ is decreasing, and $b_n\ge a_n$ is bounded below by any lower bound of $(a_n)$. By @thm-monotone-convergence, $(b_n)$ converges. The same argument applies to $\inf_{m\ge n}a_m$, which increases. Always $\liminf a_n\le\limsup a_n$, since $\inf_{m\ge n}a_m\le\sup_{m\ge n}a_m$ for every $n$.

::: {#exm-limsup-liminf-1 .example}

Let $a_{2k-1}=1+\frac1k$ and $a_{2k}=-\frac1k$, i.e. $2,-1,\frac32,-\frac12,\frac43,-\frac13,\dots$. The odd terms decrease to $1$ and the even terms increase to $0$. For every $n$, $\sup_{m\ge n}a_m$ is the first odd-indexed term from $n$ on, which tends to $1$; and $\inf_{m\ge n}a_m$ is the first even-indexed term from $n$ on, which tends to $0$. So $\limsup a_n=1$ and $\liminf a_n=0$, and the sequence diverges.

:::

::: {#fig-limsup-and-liminf-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (6.6,0) node[lab, right] {$n$};
\draw[->, faint] (0,-0.2) -- (0,4.4) node[lab, above] {};
\node[dot] at (0.360,4.100) {};
\node[dot] at (0.720,0.200) {};
\node[dot] at (1.080,3.450) {};
\node[dot] at (1.440,0.850) {};
\node[dot] at (1.800,3.233) {};
\node[dot] at (2.160,1.067) {};
\node[dot] at (2.520,3.125) {};
\node[dot] at (2.880,1.175) {};
\node[dot] at (3.240,3.060) {};
\node[dot] at (3.600,1.240) {};
\node[dot] at (3.960,3.017) {};
\node[dot] at (4.320,1.283) {};
\node[dot] at (4.680,2.986) {};
\node[dot] at (5.040,1.314) {};
\node[dot] at (5.400,2.963) {};
\node[dot] at (5.760,1.337) {};
\draw[hl] (0.180,4.100) -- (0.540,4.100); \draw[hl] (0.540,3.450) -- (0.900,3.450); \draw[hl] (0.900,3.450) -- (1.260,3.450); \draw[hl] (1.260,3.233) -- (1.620,3.233); \draw[hl] (1.620,3.233) -- (1.980,3.233); \draw[hl] (1.980,3.125) -- (2.340,3.125); \draw[hl] (2.340,3.125) -- (2.700,3.125); \draw[hl] (2.700,3.060) -- (3.060,3.060); \draw[hl] (3.060,3.060) -- (3.420,3.060); \draw[hl] (3.420,3.017) -- (3.780,3.017); \draw[hl] (3.780,3.017) -- (4.140,3.017); \draw[hl] (4.140,2.986) -- (4.500,2.986); \draw[hl] (4.500,2.986) -- (4.860,2.986); \draw[hl] (4.860,2.963) -- (5.220,2.963); \draw[hl] (5.220,2.963) -- (5.580,2.963); \draw[hl] (5.580,2.944) -- (5.940,2.944);
\draw[hl] (0.180,0.200) -- (0.540,0.200); \draw[hl] (0.540,0.200) -- (0.900,0.200); \draw[hl] (0.900,0.850) -- (1.260,0.850); \draw[hl] (1.260,0.850) -- (1.620,0.850); \draw[hl] (1.620,1.067) -- (1.980,1.067); \draw[hl] (1.980,1.067) -- (2.340,1.067); \draw[hl] (2.340,1.175) -- (2.700,1.175); \draw[hl] (2.700,1.175) -- (3.060,1.175); \draw[hl] (3.060,1.240) -- (3.420,1.240); \draw[hl] (3.420,1.240) -- (3.780,1.240); \draw[hl] (3.780,1.283) -- (4.140,1.283); \draw[hl] (4.140,1.283) -- (4.500,1.283); \draw[hl] (4.500,1.314) -- (4.860,1.314); \draw[hl] (4.860,1.314) -- (5.220,1.314); \draw[hl] (5.220,1.337) -- (5.580,1.337); \draw[hl] (5.580,1.337) -- (5.940,1.337);
\draw[faint, dashed] (0,2.80) -- (6.2,2.80) node[lab, right] {$\limsup=1$};
\draw[faint, dashed] (0,1.50) -- (6.2,1.50) node[lab, right] {$\liminf=0$};
\end{tikzpicture}
\end{center}
```

The sequence of the example with the tail suprema $\sup_{m\ge n}a_m$ (upper steps) decreasing to $1$ and the tail infima $\inf_{m\ge n}a_m$ (lower steps) increasing to $0$. They differ, so $(a_n)$ diverges.

:::

::: {#thm-limsup-liminf-convergence .theorem name="Convergence through limsup and liminf"}

For a bounded sequence $(a_n)$,
$$a_n\to a \iff \limsup_{n\to\infty}a_n=\liminf_{n\to\infty}a_n=a.$$

:::

::: {.proof}

1. ($\Rightarrow$) Let $\varepsilon>0$. There is $n$ with $a-\varepsilon<a_m<a+\varepsilon$ for all $m\ge n$.

2. Then $a-\varepsilon\le\inf_{m\ge k}a_m\le\sup_{m\ge k}a_m\le a+\varepsilon$ for every $k\ge n$, and passing to the limit (@lem-limit-preserves-inequality) gives $a-\varepsilon\le\liminf a_n\le\limsup a_n\le a+\varepsilon$. As $\varepsilon$ is arbitrary, both equal $a$.

3. ($\Leftarrow$) Let $\varepsilon>0$. Since $\inf_{m\ge n}a_m\to a$ and $\sup_{m\ge n}a_m\to a$, there is $n$ with $\inf_{m\ge n}a_m>a-\varepsilon$ and $\sup_{m\ge n}a_m<a+\varepsilon$.

4. Then every $m\ge n$ satisfies $a-\varepsilon<a_m<a+\varepsilon$, i.e. $|a_m-a|<\varepsilon$.

:::

::: {#fig-limsup-and-liminf-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (6.6,0) node[lab, right] {$n$};
\draw[->, faint] (0,-0.2) -- (0,2.4) node[lab, above] {};
\node[dot] at (0.300,1.867) {};
\node[dot] at (0.600,1.306) {};
\node[dot] at (0.900,0.680) {};
\node[dot] at (1.200,0.654) {};
\node[dot] at (1.500,1.074) {};
\node[dot] at (1.800,1.307) {};
\node[dot] at (2.100,1.089) {};
\node[dot] at (2.400,0.786) {};
\node[dot] at (2.700,0.816) {};
\node[dot] at (3.000,1.095) {};
\node[dot] at (3.300,1.211) {};
\node[dot] at (3.600,1.022) {};
\node[dot] at (3.900,0.821) {};
\node[dot] at (4.200,0.888) {};
\node[dot] at (4.500,1.107) {};
\node[dot] at (4.800,1.158) {};
\node[dot] at (5.100,0.982) {};
\node[dot] at (5.400,0.843) {};
\node[dot] at (5.700,0.935) {};
\node[dot] at (6.000,1.114) {};
\fill[tintA] (0.300,1.867) -- (0.600,1.307) -- (0.900,1.307) -- (1.200,1.307) -- (1.500,1.307) -- (1.800,1.307) -- (2.100,1.211) -- (2.400,1.211) -- (2.700,1.211) -- (3.000,1.211) -- (3.300,1.211) -- (3.600,1.158) -- (3.900,1.158) -- (4.200,1.158) -- (4.500,1.158) -- (4.800,1.158) -- (5.100,1.120) -- (5.400,1.120) -- (5.700,1.120) -- (6.000,1.120) -- (6.000,0.863) -- (5.700,0.863) -- (5.400,0.843) -- (5.100,0.843) -- (4.800,0.843) -- (4.500,0.843) -- (4.200,0.843) -- (3.900,0.821) -- (3.600,0.821) -- (3.300,0.821) -- (3.000,0.821) -- (2.700,0.816) -- (2.400,0.786) -- (2.100,0.786) -- (1.800,0.786) -- (1.500,0.786) -- (1.200,0.654) -- (0.900,0.654) -- (0.600,0.654) -- (0.300,0.654) -- cycle;
\draw[faint, dashed] (0,1) -- (6.3,1) node[lab, right] {$a$};
\end{tikzpicture}
\end{center}
```

$a_n\to a$ exactly when $\limsup a_n=\liminf a_n=a$: the region between the tail supremum and tail infimum (shaded) pinches down to the single value $a$.

:::
