---
title: "Big-O notation"
sources: [fit1058-cn-6.9]
requires: [math/discrete/logic/propositional/representing-statements, math/discrete/sequences/sums-and-series]
status: draft
---

<!-- Migrated from 1058note notes/chapters/06-sequences-series.tex: Big-O notation. -->

::: {#def-big-o .definition name="Big-O"}

For a nonnegative sequence $(a_n)$ and a function $f:\mathbb{N}\to\mathbb{R}$,
$$a_n = O(f(n)) \iff \exists c,N\ \forall n\ge N\quad a_n \le c\cdot f(n).$$

:::

::: {.remark name="Meaning"}

$a_n=O(f(n))$ says that, from some point on, $a_n$ is at most a constant multiple of $f(n)$: $f$ is an upper bound on the growth of $(a_n)$, ignoring constant factors and small $n$. This is the Big-O Game of Exercise 6.11.

:::

::: {#exm-big-o-1 .example}

Let $t_n = 100n+10n^2+2n+\log n$. For $n\ge10$, each of $100n$, $10n^2$, $2n$, $\log n$ is at most $2^n$, so $t_n \le 4\cdot2^n$ for $n\ge10$. Hence $t_n = O(2^n)$. (In fact $t_n=O(n^2)$, a much better bound.)

:::

::: {.remark name="Constant factors don't matter"}

$t_n=O(2^n)$, $t_n=O(4\cdot2^n)$ and $t_n=O(0.001\cdot2^n)$ are all true, since the constant $c$ can absorb any constant factor. So we just write $O(2^n)$.

:::

::: {.remark name="Exponential bases do matter"}

$t_n=O(3^n)$ is also true but looser. However $2^n=O(1.9^n)$ is *false*: $2^n/1.9^n=(2/1.9)^n\to\infty$, so no constant $c$ works. Unlike constant factors, different exponential bases are not interchangeable.

:::

::: {#def-big-omega-big-theta-extra .definition name="Big-Omega, Big-Theta (extra)"}

$f(n)=\Omega(g(n))$ if $\exists c>0,N\ \forall n\ge N\ f(n)\ge c\,g(n)$ (a lower bound). $f(n)=\Theta(g(n))$ if both $f(n)=O(g(n))$ and $f(n)=\Omega(g(n))$ (matching upper and lower bounds).

:::

::: {.remark name="Tight bounds (extra)"}

$O$ alone only gives an upper bound: $n=O(n^2)$ is true but loose. $\Theta$ pins down the growth rate up to constants: $t_n=\Theta(n^2)$, but $t_n$ is not $\Theta(2^n)$.

:::

::: {#def-time-complexity-of-an-algorithm .definition name="Time complexity of an algorithm (extra)"}

An algorithm has *worst-case time complexity* $O(g(n))$ if, on every input of size $n$, it performs $O(g(n))$ operations.

:::

::: {#exm-linear-search-extra .example name="Linear search (extra)"}

To search a list of $n$ items for a target, compare with each item in turn until it is found or the list ends. In the worst case (target absent or last) this takes $n$ comparisons, $\Theta(n)$; in the best case (target first) it takes $1$. If the target is present and equally likely to be in each position, the average is $\frac{1+2+\cdots+n}{n}=\frac{n+1}{2}=\Theta(n)$ comparisons (@sec-math-discrete-sequences-sums-and-series).

:::

::: {#def-polynomial-time-extra .definition name="Polynomial time (extra)"}

An algorithm is *polynomial-time* if its worst-case complexity is $O(n^k)$ for some fixed $k$; such algorithms are regarded as *tractable*. Complexities like $O(2^n)$ or $O(n!)$ are *intractable*: they become infeasible even for modest $n$.

:::

::: {#exm-why-the-distinction-matters-extra .example name="Why the distinction matters (extra)"}

At $10^9$ operations per second and $n=100$, an $n^3$ algorithm ($10^6$ operations) takes a millisecond, while a $2^n$ algorithm ($2^{100}\approx10^{30}$ operations) takes far longer than the age of the universe. No hardware speed-up closes a gap like that.

:::

::: {#def-classes-p-and-np-extra .definition name="Classes P and NP (extra)"}

$P$ is the class of decision problems solvable by a polynomial-time algorithm. $NP$ is the class of decision problems whose “yes” answers have a certificate that can be *checked* in polynomial time, even if a certificate may be hard to *find*.

:::

::: {.remark name="P vs.\ NP (extra)"}

$P\subseteq NP$, since a polynomial-time solver can also check answers. Whether $P=NP$, i.e. whether every problem whose solutions are easy to check is also easy to solve, is the most famous open problem in computer science. For example, SAT (@sec-math-discrete-logic-propositional-representing-statements) is in $NP$: a proposed truth assignment is checked quickly by evaluating the formula, but no polynomial-time algorithm is known for finding one.

:::

::: {#def-np-hard-np-complete-extra .definition name="NP-hard, NP-complete (extra)"}

A problem $H$ is *NP-hard* if every $L\in NP$ is polynomial-time reducible to $H$: there is a polynomial-time computable $f$ with $x\in L \iff f(x)\in H$ for every input $x$. A problem is *NP-complete* if it is in $NP$ and is NP-hard.

:::

::: {.remark name="Why NP-complete problems matter (extra)"}

If any one NP-complete problem had a polynomial-time algorithm, then composing it with the reductions would solve every problem in $NP$ in polynomial time, so $P=NP$. SAT was the first problem shown NP-complete (Cook–Levin, 1971); further problems are shown NP-complete by reducing a known NP-complete problem to them. Examples include $3$-SAT, Hamiltonian cycle, graph colouring, subset sum, and the decision version of TSP.

:::

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
 \draw (0,0) circle (2.6cm) node[above,yshift=2.1cm] {$NP$};
 \draw (3,0) circle (2.6cm) node[above,yshift=2.1cm] {$NP\text{-hard}$};
 \node at (-1.6,0) {$P$};
 \node[align=center] at (1.5,0.3) {$NP$-complete};
 \node[align=center,font=\small] at (1.5,-0.5) {(e.g.\ SAT)};
 \node[align=center,font=\small] at (4.5,1.0) {outside $NP$\\(e.g.\ TSP\\optimisation)};
\end{tikzpicture}
\end{center}
```

NP-complete $=$ NP $\cap$ NP-hard (drawn assuming $P\ne NP$)
