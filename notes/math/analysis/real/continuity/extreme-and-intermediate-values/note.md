---
title: "Extreme and Intermediate Values"
sources: [cama1-4, mit1801-2]
requires: [math/analysis/real/continuity/continuous-functions, math/analysis/real/sequences/monotone-sequences]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 4.1, in our own wording; proofs written out in steps. Merged 2026-11-20 (owner): the statements of the two theorems formerly in @sec-math-calculus-single-variable-limits-continuity (MIT 18.01, former ids thm-extreme-value and thm-intermediate-value, which had no proofs) were removed; these blocks are the single versions. Statements and proofs from the Cambridge notes; the IVT statement allows $f(a)>f(b)$ as the 18.01 version did. -->

Both theorems fail over $\mathbb Q$: $f(x)=x^2-2$ is continuous on $[0,2]\cap\mathbb Q$, negative at $0$ and positive at $2$, yet never $0$ there; and $1/(x^2-2)$ is continuous on $[0,2]\cap\mathbb Q$ but unbounded. So their proofs must use completeness, through Bolzano–Weierstrass or suprema.

::: {#thm-extreme-value-proof .theorem name="Extreme value theorem"}

If $f:[a,b]\to\mathbb R$ is continuous, then $f$ is bounded and attains its bounds: there are $x,y\in[a,b]$ with
$$f(x)=\sup_{[a,b]}f,\qquad f(y)=\inf_{[a,b]}f.$$

:::

::: {.proof}

1. *Bounded above.* If not, for each $n$ pick $x_n\in[a,b]$ with $f(x_n)\ge n$. By @thm-bolzano-weierstrass a subsequence $x_{n_k}$ converges, to some $x$, and $x\in[a,b]$ because $a\le x_{n_k}\le b$ (@lem-limit-preserves-inequality).

2. By @thm-sequential-continuity, $f(x_{n_k})\to f(x)$, so $(f(x_{n_k}))$ is bounded (@lem-convergent-bounded). But $f(x_{n_k})\ge n_k\ge k$, a contradiction.

3. *Supremum attained.* Let $C=\sup f$, which exists by step 1. For each $n$ pick $x_n$ with $C-\frac1n<f(x_n)\le C$ (possible since $C-\frac1n$ is not an upper bound).

4. Again a subsequence $x_{n_k}\to x\in[a,b]$, and $f(x_{n_k})\to f(x)$. By the sandwich rule, $f(x_{n_k})\to C$ as well. Limits are unique (@thm-limit-unique), so $f(x)=C$.

5. For the infimum apply steps 1–4 to $-f$.

:::

::: {#fig-extreme-and-intermediate-values-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.8,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.6) node[lab, above] {$y$};
\draw[emph] (0.300,1.587) -- (0.349,1.643) -- (0.397,1.697) -- (0.446,1.748) -- (0.495,1.796) -- (0.544,1.840) -- (0.593,1.881) -- (0.641,1.917) -- (0.690,1.949) -- (0.739,1.976) -- (0.787,1.999) -- (0.836,2.018) -- (0.885,2.031) -- (0.934,2.040) -- (0.983,2.044) -- (1.031,2.043) -- (1.080,2.038) -- (1.129,2.027) -- (1.177,2.013) -- (1.226,1.994) -- (1.275,1.970) -- (1.324,1.943) -- (1.373,1.912) -- (1.421,1.878) -- (1.470,1.840) -- (1.519,1.799) -- (1.568,1.756) -- (1.616,1.711) -- (1.665,1.664) -- (1.714,1.615) -- (1.763,1.566) -- (1.811,1.515) -- (1.860,1.465) -- (1.909,1.414) -- (1.958,1.364) -- (2.006,1.315) -- (2.055,1.267) -- (2.104,1.221) -- (2.153,1.176) -- (2.201,1.135) -- (2.250,1.095) -- (2.299,1.059) -- (2.348,1.027) -- (2.396,0.997) -- (2.445,0.972) -- (2.494,0.951) -- (2.542,0.934) -- (2.591,0.921) -- (2.640,0.914) -- (2.689,0.910) -- (2.738,0.912) -- (2.786,0.918) -- (2.835,0.929) -- (2.884,0.945) -- (2.933,0.966) -- (2.981,0.991) -- (3.030,1.021) -- (3.079,1.055) -- (3.127,1.093) -- (3.176,1.135) -- (3.225,1.181) -- (3.274,1.231) -- (3.322,1.283) -- (3.371,1.339) -- (3.420,1.396) -- (3.469,1.457) -- (3.518,1.518) -- (3.566,1.582) -- (3.615,1.646) -- (3.664,1.711) -- (3.712,1.777) -- (3.761,1.842) -- (3.810,1.906) -- (3.859,1.970) -- (3.908,2.032) -- (3.956,2.093) -- (4.005,2.152) -- (4.054,2.208) -- (4.103,2.262) -- (4.151,2.312) -- (4.200,2.359);
\draw[faint] (0.300,-0.06) -- (0.300,0.06); \node[lab, tick, below] at (0.300,-0.05) {$a$};\draw[faint] (4.200,-0.06) -- (4.200,0.06); \node[lab, tick, below] at (4.200,-0.05) {$b$};
\node[hl dot] at (4.200,2.359) {};\node[hl dot] at (2.698,0.910) {};\node[lab, above] at (4.200,2.359) {max}; \node[lab, below] at (2.698,0.910) {min};
\end{tikzpicture}
\end{center}
```

A continuous function on a closed bounded interval is bounded and attains its maximum and minimum. On an open interval, or for an unbounded function, this can fail.

:::

Both hypotheses are needed: $f(x)=1/x$ is continuous on $(0,1]$ but unbounded; $f(x)=x$ on $[0,1)$ is bounded but never reaches $\sup f=1$.

::: {#thm-intermediate-value-proof .theorem name="Intermediate value theorem"}

If $f:[a,b]\to\mathbb R$ is continuous and $f(a)<c<f(b)$ (or $f(a)>c>f(b)$), then $f(x)=c$ for some $x\in(a,b)$.

:::

::: {.proof}

1. Replacing $f$ by $f-c$, and by $-f$ if needed, we may assume $f(a)<0<f(b)$ and must find a zero.

2. Let $A=\{x\in[a,b]:f(x)<0\}$. It contains $a$ and is bounded above by $b$, so $s=\sup A$ exists and $a\le s\le b$.

3. *$f(s)<0$ is impossible.* Then $s\ne b$, and continuity with $\varepsilon=-f(s)$ gives $\delta>0$ such that $f(y)<0$ for all $y\in[a,b]$ with $|y-s|<\delta$. Some point $y\in(s,s+\delta)\cap[a,b]$ then lies in $A$, contradicting that $s$ is an upper bound of $A$.

4. *$f(s)>0$ is impossible.* Then $s\ne a$, and continuity gives $\delta>0$ with $f(y)>0$ for all $y\in[a,b]$ with $|y-s|<\delta$. So no point of $(s-\delta,s]$ lies in $A$, and $s-\delta$ is a smaller upper bound of $A$, a contradiction.

5. Hence $f(s)=0$, and $s\ne a,b$ because $f(a)<0<f(b)$.

:::

::: {#fig-extreme-and-intermediate-values-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.8,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.8) node[lab, above] {$y$};
\draw[emph] (0.200,0.244) -- (0.250,0.211) -- (0.300,0.182) -- (0.350,0.157) -- (0.400,0.138) -- (0.450,0.123) -- (0.500,0.115) -- (0.550,0.114) -- (0.600,0.119) -- (0.650,0.131) -- (0.700,0.150) -- (0.750,0.177) -- (0.800,0.211) -- (0.850,0.252) -- (0.900,0.300) -- (0.950,0.354) -- (1.000,0.415) -- (1.050,0.482) -- (1.100,0.554) -- (1.150,0.630) -- (1.200,0.712) -- (1.250,0.796) -- (1.300,0.883) -- (1.350,0.973) -- (1.400,1.063) -- (1.450,1.154) -- (1.500,1.245) -- (1.550,1.334) -- (1.600,1.422) -- (1.650,1.507) -- (1.700,1.588) -- (1.750,1.665) -- (1.800,1.738) -- (1.850,1.805) -- (1.900,1.867) -- (1.950,1.922) -- (2.000,1.971) -- (2.050,2.013) -- (2.100,2.047) -- (2.150,2.075) -- (2.200,2.095) -- (2.250,2.108) -- (2.300,2.114) -- (2.350,2.113) -- (2.400,2.106) -- (2.450,2.092) -- (2.500,2.073) -- (2.550,2.049) -- (2.600,2.020) -- (2.650,1.988) -- (2.700,1.952) -- (2.750,1.914) -- (2.800,1.874) -- (2.850,1.833) -- (2.900,1.792) -- (2.950,1.752) -- (3.000,1.713) -- (3.050,1.677) -- (3.100,1.643) -- (3.150,1.613) -- (3.200,1.588) -- (3.250,1.568) -- (3.300,1.553) -- (3.350,1.544) -- (3.400,1.541) -- (3.450,1.546) -- (3.500,1.557) -- (3.550,1.576) -- (3.600,1.601) -- (3.650,1.634) -- (3.700,1.674) -- (3.750,1.721) -- (3.800,1.775) -- (3.850,1.835) -- (3.900,1.901) -- (3.950,1.973) -- (4.000,2.049) -- (4.050,2.130) -- (4.100,2.214) -- (4.150,2.301) -- (4.200,2.390);
\draw[hl, dashed] (0,1.4) -- (4.6,1.4) node[lab, right] {$c$};
\draw[faint] (0.200,-0.06) -- (0.200,0.06); \node[lab, tick, below] at (0.200,-0.05) {$a$};\draw[faint] (4.200,-0.06) -- (4.200,0.06); \node[lab, tick, below] at (4.200,-0.05) {$b$};
\node[hl dot] at (1.588,1.400) {};
\draw[faint, dashed] (1.588,1.4) -- (1.588,0); \node[lab, tick, below] at (1.588,-0.05) {$\sup\{f<c\}$};
\end{tikzpicture}
\end{center}
```

Intermediate values: $f(a)<c<f(b)$ forces the graph across the level $c$, possibly several times. The proof takes the supremum of the points with $f<c$ and shows $f=c$ there.

:::

::: {#rmk-extreme-and-intermediate-values-1 .remark name="A proof by bisection"}

The intermediate value theorem can also be proved like @thm-bolzano-weierstrass. Start with $[a_0,b_0]=[a,b]$ and keep the half of the current interval on which $f$ is negative at the left end and non-negative at the right end. By @thm-nested-intervals some $x$ lies in all the intervals, and $a_n,b_n\to x$ as their lengths halve. Then $f(a_n)<0$ gives $f(x)\le0$, and $f(b_n)\ge0$ gives $f(x)\ge0$. This is the bisection method for locating roots numerically (@exm-ivt-root).

:::

::: {#fig-extreme-and-intermediate-values-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.8,0) node[lab, right] {$x$};
\draw[->, faint] (0,-1.6) -- (0,2.8) node[lab, above] {$y$};
\draw[emph] (0.200,0.244) -- (0.250,0.211) -- (0.300,0.182) -- (0.350,0.157) -- (0.400,0.138) -- (0.450,0.123) -- (0.500,0.115) -- (0.550,0.114) -- (0.600,0.119) -- (0.650,0.131) -- (0.700,0.150) -- (0.750,0.177) -- (0.800,0.211) -- (0.850,0.252) -- (0.900,0.300) -- (0.950,0.354) -- (1.000,0.415) -- (1.050,0.482) -- (1.100,0.554) -- (1.150,0.630) -- (1.200,0.712) -- (1.250,0.796) -- (1.300,0.883) -- (1.350,0.973) -- (1.400,1.063) -- (1.450,1.154) -- (1.500,1.245) -- (1.550,1.334) -- (1.600,1.422) -- (1.650,1.507) -- (1.700,1.588) -- (1.750,1.665) -- (1.800,1.738) -- (1.850,1.805) -- (1.900,1.867) -- (1.950,1.922) -- (2.000,1.971) -- (2.050,2.013) -- (2.100,2.047) -- (2.150,2.075) -- (2.200,2.095) -- (2.250,2.108) -- (2.300,2.114) -- (2.350,2.113) -- (2.400,2.106) -- (2.450,2.092) -- (2.500,2.073) -- (2.550,2.049) -- (2.600,2.020) -- (2.650,1.988) -- (2.700,1.952) -- (2.750,1.914) -- (2.800,1.874) -- (2.850,1.833) -- (2.900,1.792) -- (2.950,1.752) -- (3.000,1.713) -- (3.050,1.677) -- (3.100,1.643) -- (3.150,1.613) -- (3.200,1.588) -- (3.250,1.568) -- (3.300,1.553) -- (3.350,1.544) -- (3.400,1.541) -- (3.450,1.546) -- (3.500,1.557) -- (3.550,1.576) -- (3.600,1.601) -- (3.650,1.634) -- (3.700,1.674) -- (3.750,1.721) -- (3.800,1.775) -- (3.850,1.835) -- (3.900,1.901) -- (3.950,1.973) -- (4.000,2.049) -- (4.050,2.130) -- (4.100,2.214) -- (4.150,2.301) -- (4.200,2.390);
\draw[faint, dashed] (0,1.4) -- (4.6,1.4) node[lab, right] {$c$};
\draw[emph] (0.200,-0.30) -- (4.200,-0.30);
\draw[emph] (0.200,-0.65) -- (2.200,-0.65);
\draw[emph] (1.200,-1.00) -- (2.200,-1.00);
\draw[hl] (1.200,-1.35) -- (1.700,-1.35);
\end{tikzpicture}
\end{center}
```

Bisection: halve the interval and keep a half where $f-c$ still changes sign. The nested intervals (below the graph) close in on a point where $f=c$.

:::

## Continuous inverses

::: {#thm-continuous-inverse .theorem name="Inverse of a continuous increasing function"}

Let $f:[a,b]\to[c,d]$ be continuous and strictly increasing with $f(a)=c$ and $f(b)=d$. Then $f$ is a bijection and its inverse $g:[c,d]\to[a,b]$ is continuous (and strictly increasing).

:::

::: {.proof}

1. *Injective.* If $x<y$, then $f(x)<f(y)$, so $f(x)\ne f(y)$.

2. *Surjective.* $c$ and $d$ are values; every $y\in(c,d)$ is a value by @thm-intermediate-value-proof. So $f$ has an inverse $g$, which is strictly increasing because $f$ is.

3. *Continuous.* Let $y\in[c,d]$, $x=g(y)$ and $\varepsilon>0$. Suppose first $a<x<b$, and shrink $\varepsilon$ so that $[x-\varepsilon,x+\varepsilon]\subseteq[a,b]$. Put $u=f(x-\varepsilon)$ and $v=f(x+\varepsilon)$; then $u<y<v$.

4. Let $\delta=\min(y-u,v-y)>0$. If $|z-y|<\delta$, then $u<z<v$, so $x-\varepsilon<g(z)<x+\varepsilon$ because $g$ is increasing; that is, $|g(z)-g(y)|<\varepsilon$.

5. At an endpoint, say $x=a$ (so $y=c$), use only $v=f(a+\varepsilon)$ and $\delta=v-c$; for $x=b$ use only $u$.

:::

For example $x\mapsto x^n$ is continuous and strictly increasing on $[0,R]$ for every $R$, so the $n$-th root $x\mapsto\sqrt[n]x$ is continuous on $[0,\infty)$.
