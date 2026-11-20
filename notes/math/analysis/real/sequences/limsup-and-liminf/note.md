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

Both limits exist. Let $b_n=\sup_{m\ge n}a_m$: the supremum is taken over fewer terms as $n$ grows, so $(b_n)$ is decreasing, and $b_n\ge a_n$ is bounded below by any lower bound of $(a_n)$. By @thm-monotone-convergence, $(b_n)$ converges. The same argument applies to $\inf_{m\ge n}a_m$, which increases. Always $\liminf a_n\le\limsup a_n$, since $\inf_{m\ge n}a_m\le\sup_{m\ge n}a_m$ for every $n$.

::: {#exm-limsup-liminf-1 .example}

Let $a_{2k-1}=1+\frac1k$ and $a_{2k}=-\frac1k$, i.e. $2,-1,\frac32,-\frac12,\frac43,-\frac13,\dots$. The odd terms decrease to $1$ and the even terms increase to $0$. For every $n$, $\sup_{m\ge n}a_m$ is the first odd-indexed term from $n$ on, which tends to $1$; and $\inf_{m\ge n}a_m$ is the first even-indexed term from $n$ on, which tends to $0$. So $\limsup a_n=1$ and $\liminf a_n=0$, and the sequence diverges.

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
