---
title: "Measure Zero and Lebesgue's Criterion"
sources: [camib-at-a3]
requires: [math/analysis/real/integration/integrable-functions, math/analysis/real/continuity/compactness-of-closed-intervals]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Analysis II (Michaelmas 2015 lecture notes), Section 3.3 (non-examinable). The source states Lebesgue's theorem without proof; the proof here, via oscillation, is our own write-up of the standard argument, in steps. Kept because it prepares measure theory. -->

Continuous and monotone functions are integrable (@sec-math-analysis-real-integration-integrable-functions), and so are bounded functions with finitely many discontinuities. Lebesgue's criterion says exactly how large the set of discontinuities may be: it must be negligible in the following sense.

::: {#def-measure-zero .definition name="Set of measure zero"}

A set $A\subseteq\mathbb R$ has *measure zero* if for every $\varepsilon>0$ there are countably many (or finitely many) open intervals $I_1,I_2,\dots$ with
$$A\subseteq\bigcup_jI_j\qquad\text{and}\qquad\sum_j|I_j|<\varepsilon,$$
where $|I|$ is the length of the interval $I$.

:::

::: {#prp-measure-zero-examples .proposition name="Sets of measure zero"}

1. Every countable set has measure zero.
2. A countable union of sets of measure zero has measure zero.
3. An interval $[a,b]$ with $a<b$ does not have measure zero.

:::

::: {.proof}

1. Let $A=\{a_1,a_2,\dots\}$ and $\varepsilon>0$. The intervals $I_j=\bigl(a_j-\frac{\varepsilon}{2^{j+2}},a_j+\frac{\varepsilon}{2^{j+2}}\bigr)$ cover $A$ and have total length $\sum_j\frac\varepsilon{2^{j+1}}=\frac\varepsilon2<\varepsilon$.

2. Let $A=\bigcup_kA_k$ with each $A_k$ of measure zero. Cover $A_k$ by intervals of total length less than $\frac\varepsilon{2^k}$. All these intervals together are countably many, cover $A$, and have total length less than $\sum_k\frac\varepsilon{2^k}=\varepsilon$.

3. Suppose $[a,b]$ is covered by open intervals $I_j$ with $\sum|I_j|<b-a$. By @thm-heine-borel-interval finitely many, $I_1,\dots,I_n$ say, already cover $[a,b]$. A finite union of intervals covering $[a,b]$ has total length at least $b-a$ (induct on $n$: the interval containing $a$ reaches some point $c>a$, and the others must cover $[c,b]$ if $c\le b$). This contradicts $\sum_{j\le n}|I_j|<b-a$.

:::

::: {#exm-cantor-set-measure-zero .example name="The Cantor set"}

Start from $C_0=[0,1]$ and obtain $C_{n+1}$ by removing the open middle third of each interval of $C_n$. Then $C_n$ is a union of $2^n$ closed intervals of length $3^{-n}$, of total length $(\frac23)^n\to0$. The Cantor set $C=\bigcap_nC_n$ lies in every $C_n$; slightly enlarging the intervals of $C_n$ to open ones shows that $C$ has measure zero. Yet $C$ is uncountable (its points are the numbers with a ternary expansion using only the digits $0$ and $2$), so part 1 of @prp-measure-zero-examples does not cover all measure-zero sets.

:::

## Oscillation

::: {#def-oscillation .definition name="Oscillation"}

Let $f:[a,b]\to\mathbb R$ be bounded. The *oscillation* of $f$ on a set $S\subseteq[a,b]$ is $\omega_f(S)=\sup_Sf-\inf_Sf$, and the oscillation of $f$ at a point $x$ is
$$\omega_f(x)=\inf_{\delta>0}\omega_f\bigl((x-\delta,x+\delta)\cap[a,b]\bigr).$$

:::

Directly from the definitions, $f$ is continuous at $x$ if and only if $\omega_f(x)=0$. So the set $D_f$ of discontinuities of $f$ is $\bigcup_{m\ge1}D_{1/m}$, where $D_\eta=\{x:\omega_f(x)\ge\eta\}$.

::: {#lem-oscillation-set-closed .lemma name="Large oscillation is a closed condition"}

For every $\eta>0$, if $x\in[a,b]\setminus D_\eta$ then some open interval around $x$ misses $D_\eta$. Consequently every cover of $D_\eta$ by open intervals has a finite subcover.

:::

::: {.proof}

1. If $\omega_f(x)<\eta$, there is $\delta>0$ with $\omega_f(J)<\eta$ for $J=(x-\delta,x+\delta)\cap[a,b]$. Every $y\in(x-\delta,x+\delta)$ has a smaller interval around it inside $(x-\delta,x+\delta)$, on which the oscillation is at most $\omega_f(J)$. So $\omega_f(y)<\eta$.

2. Let $\mathcal I$ cover $D_\eta$ by open intervals. Add, for each $x\in[a,b]\setminus D_\eta$, an open interval around $x$ missing $D_\eta$ (step 1). Together they cover $[a,b]$, so by @thm-heine-borel-interval finitely many do. Discarding the added intervals, which contain no point of $D_\eta$, leaves finitely many members of $\mathcal I$ covering $D_\eta$.

:::

## Lebesgue's criterion

::: {#thm-lebesgue-criterion .theorem name="Lebesgue's criterion for Riemann integrability"}

A bounded function $f:[a,b]\to\mathbb R$ is Riemann integrable if and only if its set of discontinuities
$$D_f=\{x\in[a,b]:f\text{ is not continuous at }x\}$$
has measure zero.

:::

::: {.proof}

Let $|f|\le M$ with $M>0$, and use @thm-riemann-criterion throughout.

1. *Integrable implies $D_{\eta}$ has measure zero.* Fix $\eta>0$ and $\varepsilon>0$, and take a dissection $a=x_0<\dots<x_n=b$ with $U-L<\frac{\eta\varepsilon}2$. If $x\in D_\eta$ lies in the open interval $(x_{i-1},x_i)$, then $M_i-m_i\ge\omega_f(x)\ge\eta$. The total length of such subintervals is therefore at most $\frac{U-L}\eta<\frac\varepsilon2$. Every other point of $D_\eta$ is one of the finitely many $x_i$. Enlarging each of these subintervals slightly to an open interval and covering each $x_i$ by a short open interval gives a cover of $D_\eta$ of total length less than $\varepsilon$.

2. *Integrable implies $D_f$ has measure zero.* $D_f=\bigcup_mD_{1/m}$, a countable union of sets of measure zero by step 1, so part 2 of @prp-measure-zero-examples applies.

3. *Conversely, cover the bad set.* Suppose $D_f$ has measure zero and let $\varepsilon>0$. Put $\eta=\frac\varepsilon{2(b-a)}$. Since $D_\eta\subseteq D_f$, cover $D_\eta$ by open intervals of total length less than $\frac\varepsilon{4M}$; by @lem-oscillation-set-closed finitely many, $I_1,\dots,I_k$, suffice.

4. *Cover the good set.* Let $K=[a,b]\setminus(I_1\cup\dots\cup I_k)$. Each $x\in K$ has $\omega_f(x)<\eta$, so there is an open interval $J_x\ni x$ whose closure $\overline{J_x}$ satisfies $\omega_f(\overline{J_x}\cap[a,b])<\eta$ (take half of a suitable $\delta$). The $I_j$ and the $J_x$ cover $[a,b]$; by @thm-heine-borel-interval finitely many $J_{x_1},\dots,J_{x_l}$ together with $I_1,\dots,I_k$ do.

5. *The dissection.* Let $D$ consist of $a$, $b$ and all endpoints of $I_1,\dots,I_k,J_{x_1},\dots,J_{x_l}$ lying in $[a,b]$. Take a subinterval $[u,v]$ of $D$. Its interior contains no endpoint, so for each of the finitely many intervals it lies either inside or outside it. If $(u,v)$ lies inside some $I_j$, call $[u,v]$ *bad*; otherwise $(u,v)\subseteq K$, so it lies inside some $J_{x_i}$ and $\omega_f([u,v])<\eta$; call it *good*.

6. *Estimate.* Assign each bad subinterval to one $I_j$ containing its interior; those assigned to $I_j$ do not overlap, so their total length is at most $|I_j|$. Hence
$$U_D(f)-L_D(f)\le\sum_{\text{bad}}2M(v-u)+\sum_{\text{good}}\eta(v-u)<2M\cdot\frac\varepsilon{4M}+\eta(b-a)=\varepsilon.$$
By @thm-riemann-criterion, $f$ is integrable.

:::

::: {#cor-lebesgue-criterion-consequences .corollary name="Consequences"}

Let $f,g:[a,b]\to\mathbb R$ be Riemann integrable.

1. If $\varphi:[A,B]\to\mathbb R$ is continuous and $f([a,b])\subseteq[A,B]$, then $\varphi\circ f$ is integrable.
2. $fg$, $|f|$, $\max(f,g)$ and $\min(f,g)$ are integrable.
3. A uniform limit of integrable functions is integrable.

:::

::: {.proof}

1. $\varphi\circ f$ is bounded, and it is continuous wherever $f$ is, so $D_{\varphi\circ f}\subseteq D_f$. A subset of a measure-zero set has measure zero.

2. Each of these is bounded and continuous wherever both $f$ and $g$ are, so its discontinuities lie in $D_f\cup D_g$, of measure zero by @prp-measure-zero-examples.

3. If $f_n\to f$ uniformly, $f$ is continuous wherever all $f_n$ are (@thm-uniform-limit-continuous), so $D_f\subseteq\bigcup_nD_{f_n}$; $f$ is bounded as in @thm-uniform-limit-integral, which proves this part directly.

:::

::: {#rmk-lebesgue-criterion-1 .remark name="Towards measure theory"}

The definition of measure zero is the first step of Lebesgue measure: the outer measure of $A$ is the infimum of $\sum|I_j|$ over all countable covers of $A$ by open intervals, and measure zero means outer measure $0$. @exm-dirichlet-function is discontinuous everywhere, so @thm-lebesgue-criterion confirms it is not Riemann integrable; the Lebesgue integral will integrate it (to $0$), because $\mathbb Q\cap[0,1]$ has measure zero.

:::
