---
title: "Polynomials and Their Roots"
sources: [cs70-8]
requires: [math/discrete/proof/induction]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 8 (cs70-8), in our own wording; proofs written out in steps. -->

::: {#def-polynomial .definition name="Polynomial, degree, root"}

A *polynomial* in $x$ is an expression $p(x)=a_dx^d+a_{d-1}x^{d-1}+\cdots+a_1x+a_0$ with coefficients $a_i$. If $a_d\ne0$, its *degree* is $d$. A *root* of $p$ is a value $a$ with $p(a)=0$. For now the coefficients and values are real (or rational, or complex) numbers; @sec-math-discrete-polynomials-finite-fields shows that everything here works modulo a prime too.

:::

::: {#thm-polynomial-division .theorem name="Division of polynomials"}

If $q$ is a polynomial of degree at least $0$ (not the zero polynomial), then every polynomial $p$ can be written as
$$p(x)=s(x)\,q(x)+r(x),$$
where the *remainder* $r$ is $0$ or has degree less than that of $q$.

:::

::: {.proof}

1. By induction on the degree of $p$. If $p=0$ or $\deg p<\deg q$, take $s=0$ and $r=p$.

2. Otherwise let $p$ have leading term $a_dx^d$ and $q$ leading term $b_ex^e$, with $d\ge e$ and $b_e\ne0$. Then $p_1(x)=p(x)-\frac{a_d}{b_e}x^{d-e}q(x)$ has its $x^d$ term cancelled, so $p_1=0$ or $\deg p_1<d$.

3. By the induction hypothesis $p_1=s_1q+r$ with $r$ as required, so $p=\bigl(\frac{a_d}{b_e}x^{d-e}+s_1\bigr)q+r$.

:::

::: {#rmk-polynomials-and-roots-division .remark name="Long division"}

The proof is the usual long division: subtract a multiple of $q$ to remove the leading term, and repeat. Only adding, subtracting, multiplying and dividing by the non-zero number $b_e$ are used.

:::

::: {#thm-factor-theorem .theorem name="Factor theorem"}

If $a$ is a root of a polynomial $p$ of degree $d\ge1$, then $p(x)=(x-a)\,s(x)$ for a polynomial $s$ of degree $d-1$.

:::

::: {.proof}

1. Divide by $x-a$ (@thm-polynomial-division): $p(x)=(x-a)s(x)+r(x)$, where $r$ has degree less than $1$, so $r$ is a constant $c$.

2. Putting $x=a$: $0=p(a)=0\cdot s(a)+c$, so $c=0$.

3. Comparing degrees, $s$ has degree $d-1$.

:::

::: {#thm-at-most-d-roots .theorem name="At most d roots"}

A polynomial of degree $d$ that is not the zero polynomial has at most $d$ roots.

:::

::: {.proof}

1. We first show by induction on $d$: if $p$ has degree $d$ and distinct roots $a_1,\dots,a_d$, then $p(x)=c(x-a_1)\cdots(x-a_d)$ for a constant $c\ne0$. For $d=0$, $p$ is a non-zero constant $c$.

2. Let $p$ have degree $d+1$ and distinct roots $a_1,\dots,a_{d+1}$. By @thm-factor-theorem, $p(x)=(x-a_{d+1})s(x)$ with $\deg s=d$. For $i\le d$, $0=p(a_i)=(a_i-a_{d+1})s(a_i)$ and $a_i-a_{d+1}\ne0$, so $s(a_i)=0$. By the induction hypothesis $s(x)=c(x-a_1)\cdots(x-a_d)$, which gives the form of $p$.

3. Now suppose $p$ had $d+1$ distinct roots. By step 1 applied to $d$ of them, $p(x)=c(x-a_1)\cdots(x-a_d)$; at the remaining root $a$, every factor $a-a_i$ and $c$ are non-zero, so $p(a)\ne0$, a contradiction.

:::

::: {#fig-polynomials-and-roots-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.1cm,y=0.55cm]
\draw[->, muted] (-2.4,0) -- (3,0) node[lab, right] {$x$};
\draw[->, muted] (0,-3.2) -- (0,3.6);
\draw[emph, primary, domain=-2.05:2.6, samples=80] plot (\x,{0.5*(\x+1.5)*(\x-0.5)*(\x-2)});
\foreach \r/\l in {-1.5/-\frac32, 0.5/\frac12, 2/2} {\fill[accent] (\r,0) circle[pt]; \node[tick, below] at (\r,-0.15) {$\l$};}
\node[lab, primary] at (-1.6,2.8) {$p(x)$};
\end{tikzpicture}
\end{center}
```

The cubic $p(x)=\frac12\bigl(x+\frac32\bigr)\bigl(x-\frac12\bigr)(x-2)$ has three real roots, the most a polynomial of degree $3$ can have.

:::
