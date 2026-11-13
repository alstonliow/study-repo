---
title: "The Extended Euclidean Algorithm"
sources: [fit1058-cn-7.7, fit1058-cn-7.8]
requires: [math/discrete/number-theory/divisibility-and-primes, math/discrete/number-theory/remainders-and-parity]
status: draft
---

<!-- Migrated from 1058note notes/chapters/07-number-theory.tex: The gcd and integer linear combinations; The extended Euclidean algorithm. -->

## The gcd and integer linear combinations

::: {#def-integer-linear-combinations .definition name="Integer linear combinations"}

For $m,n\in\mathbb{Z}$, the set of all *integer linear combinations* of $m$ and $n$ is
$$m\mathbb{Z}+n\mathbb{Z}=\{xm+yn : x,y\in\mathbb{Z}\}.$$

:::

::: {#exm-extended-euclidean-algorithm-1 .example}

For $m=12$, $n=20$:  $1\cdot12+0\cdot20=12$,  $-1\cdot12+1\cdot20=8$,  $2\cdot12-1\cdot20=4$,  $-2\cdot12+1\cdot20=-4$,  $-5\cdot12+3\cdot20=0$. In fact $12\mathbb{Z}+20\mathbb{Z}$ is exactly $4\mathbb{Z}$, the multiples of $\gcd(12,20)=4$.

:::

::: {#lem-deltaz .lemma}

Let $m,n\in\mathbb{N}$ and let $\Delta$ be the least positive element of $m\mathbb{Z}+n\mathbb{Z}$. Then $m\mathbb{Z}+n\mathbb{Z}=\Delta\mathbb{Z}$.

:::

::: {.proof}

($\supseteq$) Write $\Delta=x_0m+y_0n$. For any $k\in\mathbb{Z}$, $k\Delta=(kx_0)m+(ky_0)n\in m\mathbb{Z}+n\mathbb{Z}$.

($\subseteq$) Let $z=xm+yn$ and divide: $z=q\Delta+r$ with $0\le r<\Delta$ (@thm-division). Both $z$ and $q\Delta$ lie in $m\mathbb{Z}+n\mathbb{Z}$, which is closed under subtraction, so $r=z-q\Delta$ does too. If $r>0$ this would contradict the minimality of $\Delta$. So $r=0$ and $\Delta\mid z$.

:::

::: {#thm-bezout .theorem name="Bézout"}

For $m,n\in\mathbb{N}$, $\gcd(m,n)$ is the least positive integer linear combination of $m$ and $n$. In particular, there exist $x,y\in\mathbb{Z}$ with $\gcd(m,n)=xm+yn$.

:::

::: {.proof}

Let $\Delta$ be as in @lem-deltaz. Since $\Delta$ divides every element of $m\mathbb{Z}+n\mathbb{Z}$, in particular $m$ and $n$, it is a common divisor. Conversely, any common divisor $d$ of $m$ and $n$ divides every $xm+yn$ (@prp-divlinear), in particular $\Delta$, so $d\le\Delta$. Hence $\Delta=\gcd(m,n)$.

:::

::: {.remark name="Bézout coefficients are never unique"}

Since $nm-mn=0$, adding $k$ times $(n,-m)$ to a solution gives another: $(x+kn)m+(y-km)n = xm+yn$. For example $4=2\cdot12-1\cdot20=(-3)\cdot12+2\cdot20$.

:::

## The extended Euclidean algorithm

::: {#def-extended-euclidean-algorithm-eea .definition name="Extended Euclidean Algorithm (EEA)"}

To find $\gcd(m,n)$ together with $x,y$ such that $\gcd(m,n)=xm+yn$:

1.  Input $m,n\in\mathbb{N}$; if $m<n$, swap them so that $m\ge n$.

2.  Initialise the triples $(a,x,y):=(m,1,0)$ and $(b,z,w):=(n,0,1)$.

3.  If $b=0$, output $(a,x,y)$.

4.  Let $q:=\lfloor a/b\rfloor$. Replace $(a,x,y)$ by $(b,z,w)$, and $(b,z,w)$ by $(a,x,y)-q\cdot(b,z,w)$ (using the old values). Go to step 3.

:::

::: {.remark name="The EA with extra bookkeeping"}

The first entries of the triples evolve exactly as in the EA. The other two entries just record how each first entry is made up as an integer linear combination of $m$ and $n$.

:::

::: {#thm-eea .theorem name="Correctness of the EEA"}

At every stage the triples satisfy $a=xm+yn$ and $b=zm+wn$. On termination $a=\gcd(m,n)$, so the output gives Bézout coefficients.

:::

::: {.proof}

Initially $m=1\cdot m+0\cdot n$ and $n=0\cdot m+1\cdot n$. If the invariant holds before an update, the new $a$-triple is the old $b$-triple, and the new $b$-triple satisfies $a-qb = (x-qz)m+(y-qw)n$, so the invariant still holds. Since the first entries follow the EA, at termination $a=\gcd(m,n)$.

:::

::: {#exm-extended-euclidean-algorithm-1-2 .example}

Compute $\gcd(40,27)$ and express it as a combination. Each row $(t,x,y)$ satisfies $t=40x+27y$, and each new row is the row two above minus $q$ times the row above:
$$\begin{array}{rrrl}
40 & 1 & 0 & \\
27 & 0 & 1 & \\
13 & 1 & -1 & (q=1)\\
1 & -2 & 3 & (q=2)\\
0 & 27 & -40 & (q=13)
\end{array}$$
So $\gcd(40,27)=1=-2\cdot40+3\cdot27$. The row with $t=1$ already gives the answer; the last row is only a check.

:::

::: {#exm-eea-with-a-nontrivial-gcd .example name="EEA with a nontrivial gcd"}

For $\gcd(1180,482)$, with rows $t=1180x+482y$:
$$\begin{array}{rrrl}
1180 & 1 & 0 & \\
482 & 0 & 1 & \\
216 & 1 & -2 & (q=2)\\
50 & -2 & 5 & (q=2)\\
16 & 9 & -22 & (q=4)\\
2 & -29 & 71 & (q=3)\\
0 & 241 & -590 & (q=8)
\end{array}$$
So $\gcd(1180,482)=2=-29\cdot1180+71\cdot482$. Check: $71\cdot482-29\cdot1180=34222-34220=2$.

:::

::: {.remark name="Error check"}

The signs in the last two columns alternate down the table. If they ever fail to alternate, an arithmetic mistake has been made.

:::
