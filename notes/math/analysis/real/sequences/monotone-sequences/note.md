---
title: "Monotone Sequences and Bolzano–Weierstrass"
sources: [cama1-2]
requires: [math/analysis/real/sequences/convergence-of-sequences]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 2.3, in our own wording; proofs written out in steps. -->

The least upper bound property can be restated in terms of sequences: bounded monotone sequences converge. From this follow the nested intervals property and the Bolzano–Weierstrass theorem, the main tools for producing limits without knowing them in advance.

## Monotone sequences

::: {#def-monotone-sequence .definition name="Monotone sequence"}

$(a_n)$ is *increasing* if $a_n\le a_{n+1}$ for all $n$ and *strictly increasing* if $a_n<a_{n+1}$ for all $n$; *decreasing* and *strictly decreasing* are defined likewise. A sequence is *monotone* if it is increasing or decreasing.

:::

::: {#thm-monotone-convergence .theorem name="Monotone convergence"}

In $\mathbb R$, every increasing sequence that is bounded above converges, and its limit is
$$\lim_{n\to\infty}a_n=\sup\{a_n:n\in\mathbb N\}.$$
Likewise every decreasing sequence bounded below converges to the infimum of its terms.

:::

::: {.proof}

1. The set $\{a_n:n\in\mathbb N\}$ is non-empty and bounded above, so it has a supremum $s$ (@def-real-numbers).

2. Let $\varepsilon>0$. Since $s-\varepsilon<s$ is not an upper bound, some $a_N>s-\varepsilon$.

3. For $n\ge N$, monotonicity and the upper bound give $s-\varepsilon<a_N\le a_n\le s$, so $|a_n-s|<\varepsilon$.

4. For a decreasing sequence bounded below, apply steps 1–3 to $(-a_n)$.

:::

An ordered field is said to have the *monotone sequences property* if every increasing sequence bounded above converges. @thm-monotone-convergence says the least upper bound property implies it; the converse also holds, so either property can serve as the completeness axiom of $\mathbb R$.

::: {#thm-monotone-sequences-equivalent .theorem name="Monotone sequences property is equivalent to least upper bounds"}

In an ordered field $F$, the monotone sequences property implies

1. the Archimedean property: $1/n\to0$;
2. the least upper bound property.

:::

::: {.proof}

1. *Archimedean property.* The sequence $(1/n)$ is decreasing and bounded below by $0$, so it converges to some $\delta$, and $\delta\ge0$ by @lem-limit-preserves-inequality. If $\delta>0$, then since $1/n\to\delta$ some $N$ has $1/N<\delta+\delta=2\delta$; then for $n\ge 4N$, $1/n\le 1/(4N)<\delta/2$, so the terms stay at distance more than $\delta/2$ from $\delta$, a contradiction. Hence $\delta=0$.

2. *Least upper bounds: bisection.* Let $A$ be non-empty and bounded above. Choose $u_0$ that is not an upper bound (any number below an element of $A$) and an upper bound $v_0$. Given $u_n$ (not an upper bound) and $v_n$ (an upper bound), let $m=(u_n+v_n)/2$; if $m$ is an upper bound set $u_{n+1}=u_n$, $v_{n+1}=m$, otherwise $u_{n+1}=m$, $v_{n+1}=v_n$.

3. Then $(u_n)$ is increasing, $(v_n)$ is decreasing, $u_n\le v_n\le v_0$, and $v_n-u_n=(v_0-u_0)/2^n$. Since $0<1/2^n\le1/n$, step 1 and the sandwich rule give $v_n-u_n\to0$.

4. By the monotone sequences property $u_n\to s$ for some $s$, and then $v_n=u_n+(v_n-u_n)\to s$ as well.

5. *$s$ is an upper bound.* If some $a\in A$ had $a>s$, then since $v_n\to s$ some $v_m<a$, contradicting that $v_m$ is an upper bound.

6. *$s$ is the least.* If $t<s$, then since $u_n\to s$ some $u_m>t$; $u_m$ is not an upper bound, so neither is $t$. Hence $s=\sup A$.

:::

## Nested intervals

::: {#thm-nested-intervals .theorem name="Nested intervals property"}

If $I_1\supseteq I_2\supseteq\cdots$ are non-empty closed bounded intervals in $\mathbb R$, then
$$\bigcap_{n=1}^\infty I_n\ne\emptyset.$$

:::

::: {.proof}

1. Write $I_n=[a_n,b_n]$. Nesting gives $a_1\le a_2\le\cdots$ and $b_1\ge b_2\ge\cdots$, with $a_n\le b_n\le b_1$.

2. So $(a_n)$ is increasing and bounded above by $b_1$; by @thm-monotone-convergence it converges to $a=\sup_n a_n$, and $a_n\le a$ for every $n$.

3. Fix $n$. For every $m\ge n$, $a_m\le b_m\le b_n$, so $b_n$ is an upper bound of the $a_m$ (for $m<n$ too, since $a_m\le a_n$), hence $a\le b_n$.

4. Thus $a_n\le a\le b_n$, i.e. $a\in I_n$, for every $n$.

:::

Closedness matters: the open intervals $(0,1/n)$ are nested and non-empty, but their intersection is empty.

::: {#rmk-monotone-sequences-1 .remark name="Another proof that $\mathbb R$ is uncountable" related="thm-reals-uncountable"}

Suppose $x_1,x_2,\dots$ listed all real numbers. Choose a closed bounded interval $I_1$ not containing $x_1$, then a closed interval $I_2\subseteq I_1$ not containing $x_2$, and so on (split the current interval into three closed thirds; at least one misses $x_n$). By @thm-nested-intervals some $x$ lies in every $I_n$, so $x\ne x_n$ for all $n$: $x$ is not on the list. This avoids decimal expansions, unlike the diagonal argument of @thm-reals-uncountable.

:::

## Subsequences and Bolzano–Weierstrass

::: {#def-subsequence .definition name="Subsequence"}

A *subsequence* of $(a_n)$ is a sequence $(a_{n_k})_{k\ge1}$ with $n_1<n_2<n_3<\cdots$.

:::

For example, $(1/k^2)$ is a subsequence of $(1/n)$, with $n_k=k^2$. Since $n_k\ge k$, every subsequence of a sequence converging to $\ell$ also converges to $\ell$.

::: {#thm-bolzano-weierstrass .theorem name="Bolzano–Weierstrass theorem"}

Every bounded sequence of real numbers has a convergent subsequence.

:::

::: {.proof}

1. Let $u_0\le a_n\le v_0$ for all $n$. *Bisection:* given $[u_k,v_k]$ containing $a_n$ for infinitely many $n$, at least one of its two closed halves also does; let $[u_{k+1},v_{k+1}]$ be such a half. Then $v_k-u_k=(v_0-u_0)/2^k$.

2. By @thm-nested-intervals there is $x\in[u_k,v_k]$ for all $k$.

3. Choose indices $n_1<n_2<\cdots$ with $a_{n_k}\in[u_k,v_k]$: this is possible because $[u_k,v_k]$ contains infinitely many terms, and only finitely many indices have been used so far.

4. Let $\varepsilon>0$. By the Archimedean property choose $K$ with $(v_0-u_0)/2^K<\varepsilon$. Since $x\in[u_K,v_K]$, this interval lies in $(x-\varepsilon,x+\varepsilon)$.

5. For $k\ge K$, $a_{n_k}\in[u_k,v_k]\subseteq[u_K,v_K]\subseteq(x-\varepsilon,x+\varepsilon)$. So $a_{n_k}\to x$.

:::

::: {#exm-monotone-sequences-1 .example name="A subsequence, not the sequence"}

$a_n=(-1)^n$ is bounded and divergent (@exm-limits-3), but its subsequence of even-indexed terms is constantly $1$ and converges. Bolzano–Weierstrass promises a convergent subsequence, nothing more.

:::
