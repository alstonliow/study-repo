---
title: "From recursive definitions to formulas"
sources: [fit1058-cn-6.6]
requires: [math/discrete/sequences/sums-and-series]
level: core
status: draft
---

<!-- Migrated from 1058note notes/chapters/06-sequences-series.tex: From recursive definitions to formulas. -->

::: {.remark name="Explore, conjecture, prove"}

To find a formula for a recursively defined sequence:

1.  **Explore**: compute the first several terms.

2.  **Conjecture**: look for a pattern and propose a formula.

3.  **Prove**: prove the formula for all $n$, usually by induction.

:::

::: {#exm-solving-recurrences-1 .example}

Let $f_1=1$, $f_n = 2f_{n-1}+1$.

**Explore**: $f_1=1$, $f_2=3$, $f_3=7$, $f_4=15$.

**Conjecture**: each term is one less than a power of $2$, so $f_n = 2^n-1$.

**Prove**: We use induction on $n$. For the base case, $2^1-1=1=f_1$. For the inductive step, assume $f_k=2^k-1$ for some $k\ge1$. Then $f_{k+1} = 2f_k+1 = 2(2^k-1)+1 = 2^{k+1}-1$. By the Principle of Mathematical Induction, $f_n=2^n-1$ for all $n\ge1$.

:::

::: {#exm-tower-of-hanoi-extra .example name="Tower of Hanoi (extra)"}

There are $n$ disks of different sizes on peg $A$, largest at the bottom. They must all be moved to peg $C$, one at a time, never placing a larger disk on a smaller one; peg $B$ may be used. Let $T_n$ be the minimum number of moves. To move the largest disk we must first move the other $n-1$ disks to $B$ ($T_{n-1}$ moves), then move the largest disk ($1$ move), then move the $n-1$ disks onto it ($T_{n-1}$ moves). So $T_1=1$ and $T_n=2T_{n-1}+1$, the same recurrence as the previous example, and hence $T_n=2^n-1$.

:::

::: {#def-linear-homogeneous-recurrence-with-constant .definition name="Linear homogeneous recurrence with constant coefficients (extra)"}

This is a recurrence
$$a_n = c_1a_{n-1}+c_2a_{n-2}+\cdots+c_ka_{n-k}, \qquad c_k \neq 0,$$
with $k$ initial terms given. Its *characteristic equation* is $x^k - c_1x^{k-1}-c_2x^{k-2}-\cdots-c_k = 0$.

:::

::: {.remark name="Why the characteristic equation (extra)"}

Trying $a_n=x^n$ in the recurrence and dividing by $x^{n-k}$ gives exactly the characteristic equation. So each root $r$ gives a solution $a_n=r^n$. Moreover, the recurrence is *linear*: any combination $\alpha a_n+\beta b_n$ of two solutions is again a solution.

:::

::: {#thm-distinct-roots .theorem name="Distinct roots case (extra)"}

If the characteristic equation has $k$ distinct roots $r_1,\dots,r_k$, then every solution has the form
$$a_n = \alpha_1 r_1^n + \alpha_2 r_2^n + \cdots + \alpha_k r_k^n$$
for constants $\alpha_1,\dots,\alpha_k$ determined by the initial terms.

:::

::: {#exm-solving-a-second-order-recurrence .example name="Solving a second-order recurrence (extra)"}

Solve $a_n = 5a_{n-1} - 6a_{n-2}$ with $a_0=1$, $a_1=4$.

The characteristic equation is $x^2-5x+6=(x-2)(x-3)=0$, with roots $2$ and $3$. So $a_n = \alpha_1 2^n + \alpha_2 3^n$. The initial terms give $\alpha_1+\alpha_2=1$ and $2\alpha_1+3\alpha_2=4$, so $\alpha_2=2$ and $\alpha_1=-1$. Hence $a_n = 2\cdot3^n-2^n$.

:::

::: {#def-linear-nonhomogeneous-recurrence-extra .definition name="Linear nonhomogeneous recurrence (extra)"}

This is a recurrence $a_n = c_1a_{n-1}+\cdots+c_ka_{n-k} + F(n)$ where $F$ is not identically $0$. Dropping $F(n)$ gives the *associated homogeneous* recurrence.

:::

::: {#prp-general-solution-shape-extra .proposition name="General solution shape (extra)"}

Every solution has the form $a_n = a_n^{(p)} + a_n^{(h)}$, where $a_n^{(p)}$ is any *one* particular solution of the nonhomogeneous recurrence and $a_n^{(h)}$ is a solution of the associated homogeneous recurrence.

:::

::: {.proof}

If $(b_n)$ is any solution, then subtracting the recurrences for $b_n$ and $a_n^{(p)}$ cancels $F(n)$. So $b_n-a_n^{(p)}$ solves the homogeneous recurrence, i.e. $b_n=a_n^{(p)}+a_n^{(h)}$.

:::

::: {#exm-worked-nonhomogeneous-example-extra .example name="Worked nonhomogeneous example (extra)"}

Solve $a_n = 3a_{n-1}+2^n$ with $a_0=1$.

The homogeneous part $a_n=3a_{n-1}$ has solutions $a_n^{(h)}=\alpha\cdot3^n$. For a particular solution try $a_n^{(p)}=A\cdot2^n$: substituting gives $A\cdot2^n = 3A\cdot2^{n-1}+2^n$, so $2A=3A+2$ and $A=-2$. Hence $a_n = \alpha\cdot3^n - 2^{n+1}$, and $a_0=1$ gives $\alpha-2=1$, so $\alpha=3$. Therefore $a_n = 3^{n+1}-2^{n+1}$.

:::

::: {#def-divide-and-conquer-recurrence-extra .definition name="Divide-and-conquer recurrence (extra)"}

An algorithm that splits a problem of size $n$ into $a$ subproblems of size $n/b$, and spends $g(n)$ extra work combining their results, has running time $f(n) = a\,f(n/b) + g(n)$.

:::

::: {#exm-merge-sort-extra .example name="Merge sort (extra)"}

Merge sort splits a list into $a=2$ halves ($b=2$) and merges them in linear time, so $f(n) = 2f(n/2)+n$.

:::

::: {#thm-master-theorem-special-case-extra .theorem name="Master theorem, special case $g(n)=cn^d$ (extra)"}

For $f(n)=af(n/b)+cn^d$ with $a\ge1$, $b>1$, $c,d\ge0$, and $n$ a power of $b$,
$$f(n) = \begin{cases}
\Theta(n^d), & a<b^d, \\
\Theta(n^d\log n), & a=b^d, \\
\Theta(n^{\log_b a}), & a>b^d.
\end{cases}$$

:::

::: {.proof name="Proof sketch"}

Let $n=b^k$. Unrolling the recurrence $k$ times gives
$$f(n) = a^kf(1) + cn^d\sum_{i=0}^{k-1}\left(\frac{a}{b^d}\right)^i.$$
The geometric sum (@sec-math-discrete-sequences-sums-and-series) behaves differently according to whether the ratio $a/b^d$ is less than, equal to, or greater than $1$, giving the three cases. Also $a^k=a^{\log_b n}=n^{\log_b a}$.

:::

::: {#exm-solving-recurrences-2 .example}

For merge sort, $a=2$, $b=2$, $d=1$, so $a=b^d$ and $f(n)=\Theta(n\log n)$.

:::

::: {#def-generating-function-extra .definition name="Generating function (extra)"}

The *generating function* of a sequence $(a_n)_{n=0}^{\infty}$ is the formal power series $G(x) = \sum_{n=0}^{\infty} a_n x^n$.

:::

::: {#exm-extra .example name="Extra"}

The sequence $1,1,1,\dots$ has generating function $\sum x^n = \dfrac{1}{1-x}$ (@sec-math-discrete-sequences-sums-and-series).

:::

::: {.remark name="Solving recurrences with generating functions (extra)"}

Multiply the recurrence by $x^n$ and sum over $n$; recognise each sum as a shifted or scaled copy of $G(x)$; solve the resulting equation for $G(x)$; then expand $G(x)$ as a power series (e.g. by partial fractions) and read off $a_n$ as the coefficient of $x^n$.

:::
