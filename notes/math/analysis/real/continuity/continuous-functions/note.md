---
title: "Continuous Functions"
sources: [cama1-4]
requires: [math/analysis/real/sequences/convergence-of-sequences, math/calculus/single-variable/limits/continuity]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 4.1, in our own wording; proofs written out in steps. Continuity via limits and the rules for combining continuous functions are in @sec-math-calculus-single-variable-limits-continuity; this note works on an arbitrary domain $A\subseteq\mathbb R$ and connects continuity with sequences. -->

## The $\varepsilon$–$\delta$ definition

::: {#def-continuity-epsilon-delta .definition name="Continuity on a set" equivalent="def-continuity"}

Let $A\subseteq\mathbb R$, $f:A\to\mathbb R$ and $a\in A$. Then $f$ is *continuous at $a$* if
$$\forall\varepsilon>0\ \exists\delta>0\ \forall y\in A\quad |y-a|<\delta\Rightarrow|f(y)-f(a)|<\varepsilon,$$
and *continuous* if it is continuous at every point of $A$.

:::

When $A$ contains an interval around $a$, this says $\lim_{x\to a}f(x)=f(a)$ (@def-limit-of-a-function), which is @def-continuity. The present form also covers points of $A$ that are isolated or at the edge of $A$, and domains such as $\mathbb Q$.

Informally: $f(a)$ can be computed to any accuracy $\varepsilon$ from inputs that are accurate enough (within $\delta$ of $a$). For the step function equal to $0$ for $x\le\pi$ and $1$ for $x>\pi$, inputs $3,\ 3.14,\ 3.1416,\ 3.14159,\dots$ give $0,0,1,0,\dots$: no accuracy of the input pins down the output, and the function is discontinuous at $\pi$.

Constant functions are continuous (any $\delta$ works), and so is $f(x)=x$ (take $\delta=\varepsilon$).

::: {#thm-sequential-continuity .theorem name="Sequential continuity"}

$f:A\to\mathbb R$ is continuous at $a\in A$ if and only if for every sequence $(a_n)$ in $A$,
$$a_n\to a\ \Longrightarrow\ f(a_n)\to f(a).$$

:::

::: {.proof}

1. ($\Rightarrow$) Let $a_n\to a$ and $\varepsilon>0$. Continuity gives $\delta>0$ with $|f(y)-f(a)|<\varepsilon$ whenever $y\in A$, $|y-a|<\delta$.

2. Since $a_n\to a$, there is $N$ with $|a_n-a|<\delta$ for $n\ge N$, and then $|f(a_n)-f(a)|<\varepsilon$. So $f(a_n)\to f(a)$.

3. ($\Leftarrow$) Suppose $f$ is not continuous at $a$: there is $\varepsilon>0$ such that for every $\delta>0$ some $y\in A$ has $|y-a|<\delta$ but $|f(y)-f(a)|\ge\varepsilon$.

4. Taking $\delta=1/n$, choose such a $y=a_n$ for each $n$. Then $a_n\to a$ (@thm-archimedean-property) but $|f(a_n)-f(a)|\ge\varepsilon$ for all $n$, so $f(a_n)\not\to f(a)$.

:::

::: {#exm-continuous-functions-1 .example name="Testing continuity with sequences"}

1. The sign-type function $f(x)=-1$ for $x<0$, $f(x)=1$ for $x\ge0$ is discontinuous at $0$: $-\frac1n\to0$ but $f(-\frac1n)=-1\not\to1=f(0)$.

2. On the domain $\mathbb Q$, let $f(x)=1$ if $x^2>2$ and $f(x)=0$ if $x^2<2$ (every rational falls in one case). This $f$ is continuous: each rational $a$ has an interval around it, avoiding $\pm\sqrt2$, on which $f$ is constant.

3. Let $f(x)=\sin(1/x)$ for $x\ne0$ and $f(0)=0$. With $a_n=\frac{1}{(2n+\frac12)\pi}\to0$ we get $f(a_n)=\sin\bigl(2n\pi+\frac\pi2\bigr)=1\not\to0$, so $f$ is discontinuous at $0$.

:::

## Building continuous functions

::: {#prp-continuity-algebra-on-sets .proposition name="Sums, products, quotients, composites" related="prp-continuity-algebra"}

Let $f,g:A\to\mathbb R$ be continuous. Then $f+g$ and $fg$ are continuous, and so is $f/g$ if $g$ never vanishes. If $f:A\to B$ and $h:B\to\mathbb R$ are continuous, then $h\circ f$ is continuous.

:::

::: {.proof}

1. Let $a\in A$ and $a_n\to a$ in $A$. By @thm-sequential-continuity, $f(a_n)\to f(a)$ and $g(a_n)\to g(a)$.

2. By the limit laws (@prp-limit-laws, proved in @sec-math-analysis-real-sequences-convergence-of-sequences), $f(a_n)+g(a_n)\to f(a)+g(a)$, $f(a_n)g(a_n)\to f(a)g(a)$, and $f(a_n)/g(a_n)\to f(a)/g(a)$ when $g$ has no zeros. By @thm-sequential-continuity again, the three functions are continuous at $a$.

3. *Composite.* $f(a_n)\to f(a)$, and $(f(a_n))$ is a sequence in $B$, so continuity of $h$ gives $h(f(a_n))\to h(f(a))$.

:::

Starting from constants and $x$, it follows that every polynomial is continuous on $\mathbb R$, and every rational function $P/Q$ is continuous wherever $Q\ne0$.

::: {#rmk-continuous-functions-1 .remark name="The same proof with $\varepsilon$ and $\delta$"}

The composite can also be handled directly. Given $\varepsilon>0$, continuity of $h$ at $f(a)$ gives $\eta>0$ with $|z-f(a)|<\eta\Rightarrow|h(z)-h(f(a))|<\varepsilon$ for $z\in B$; continuity of $f$ at $a$ gives $\delta>0$ with $|y-a|<\delta\Rightarrow|f(y)-f(a)|<\eta$. Chaining the two, $|y-a|<\delta\Rightarrow|h(f(y))-h(f(a))|<\varepsilon$. The sequence version is shorter because the $\varepsilon$-work was done once, for sequences.

:::
