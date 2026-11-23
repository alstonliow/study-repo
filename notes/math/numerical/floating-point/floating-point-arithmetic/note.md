---
title: "Floating-Point Arithmetic"
sources: [mit18335-2]
requires: []
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 2 and its supplementary note on floating-point myths, in our own wording; numbers checked in Python (IEEE double). -->

A computer stores a real number with a fixed number of significant digits and a bounded exponent. Each arithmetic operation is then exact up to one rounding, and that single fact, a relative error of at most $\varepsilon_{\text{mach}}$ per operation, is the starting point of all error analysis in numerical computation.

::: {#def-floating-point-system .definition name="Floating-point numbers"}

Fix a base $\beta\ge2$, a precision $t\ge1$ and an exponent range $e_{\min}\le e\le e_{\max}$. The *floating-point numbers* are $0$ and
$$x=\pm\,\frac{m}{\beta^{t}}\,\beta^{e},\qquad m\in\mathbb{Z},\quad \beta^{t-1}\le m<\beta^{t},\quad e_{\min}\le e\le e_{\max}.$$
The integer $m$ is the *significand* (it has exactly $t$ digits in base $\beta$) and $e$ the *exponent*. The *unit roundoff* or *machine epsilon* is
$$\varepsilon_{\text{mach}}=\tfrac12\,\beta^{1-t}.$$

:::

Between $\beta^{e-1}$ and $\beta^{e}$ the numbers are equally spaced with gap $\beta^{e-t}$, so the gap grows with the size of the number: the *absolute* spacing varies, the *relative* spacing stays between $\beta^{-t}$ and $\beta^{1-t}$.

::: {#fig-floating-point-arithmetic-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.7cm]
\draw[->, faint] (-0.1,0) -- (7.4,0);
\foreach \v in {0.5,0.625,0.75,0.875,1,1.25,1.5,1.75,2,2.5,3,3.5,4,5,6,7} {\draw (\v,-0.12) -- (\v,0.12);}
\foreach \v in {0.5,1,2,4} {\draw[hl] (\v,-0.2) -- (\v,0.2);}
\fill (0,0) circle (1.5pt) node[lab, below=3pt] {$0$};
\foreach \v in {0.5,1,2,4,7} {\node[tick, below=4pt] at (\v,0) {$\v$};}
\draw[faint, <->] (4,0.45) -- (5,0.45) node[midway, lab, above] {gap $1$};
\draw[faint, <->] (1,0.45) -- (1.25,0.45) node[midway, lab, above] {$\tfrac14$};
\end{tikzpicture}
\end{center}
```

The positive numbers of the toy system $\beta=2$, $t=3$, $-1\le e\le3$: significands $m=4,5,6,7$ give $x=\tfrac m8\,2^{e}$. Each binade $[2^{e-1},2^{e})$ (marked at the thick ticks) holds four equally spaced numbers, and the spacing doubles from one binade to the next.

:::

::: {#thm-rounding-relative-error .theorem name="Rounding has relative error at most ε_mach"}

Let $\operatorname{fl}(x)$ be a nearest floating-point number to a real $x$ with $\beta^{e_{\min}-1}\le\lvert x\rvert\le\beta^{e_{\max}}(1-\beta^{-t})$ (no underflow or overflow). Then
$$\operatorname{fl}(x)=x(1+\delta)\qquad\text{for some }\lvert\delta\rvert\le\varepsilon_{\text{mach}}.$$

:::

::: {.proof}

1. Take $x>0$ and choose $e$ with $\beta^{e-1}\le x<\beta^{e}$. On this interval the floating-point numbers are the multiples of $\beta^{e-t}$, including both endpoints.

2. A nearest one is therefore within half a gap: $\lvert\operatorname{fl}(x)-x\rvert\le\tfrac12\beta^{e-t}$.

3. Divide by $x\ge\beta^{e-1}$: $\lvert\operatorname{fl}(x)-x\rvert/x\le\tfrac12\beta^{e-t}/\beta^{e-1}=\tfrac12\beta^{1-t}=\varepsilon_{\text{mach}}$.

4. Set $\delta=(\operatorname{fl}(x)-x)/x$. For $x<0$ apply the same argument to $-x$.

:::

::: {#def-floating-point-operations .definition name="Floating-point operations"}

For floating-point $x,y$ and an operation $*\in\{+,-,\times,\div\}$, the computed result is $x\circledast y=\operatorname{fl}(x*y)$: the exact result, correctly rounded. Combined with @thm-rounding-relative-error this gives the *fundamental axiom of floating-point arithmetic*:
$$x\circledast y=(x*y)(1+\delta),\qquad \lvert\delta\rvert\le\varepsilon_{\text{mach}},$$
whenever $x*y$ neither overflows nor underflows. The IEEE 754 standard requires this for $+,-,\times,\div$ and $\sqrt{\ }$.

:::

::: {#exm-ieee-double .example name="IEEE single and double precision"}

IEEE *double precision* uses $\beta=2$, $t=53$ and $-1021\le e\le1024$ in 64 bits (1 sign bit, 11 exponent bits, 52 stored significand bits; the leading bit is implicit). So
$$\varepsilon_{\text{mach}}=2^{-53}\approx1.11\times10^{-16},$$
about 16 significant decimal digits, and the largest number is about $1.8\times10^{308}$. *Single precision* has $t=24$ and $\varepsilon_{\text{mach}}=2^{-24}\approx5.96\times10^{-8}$.

The standard also has signed zeros, $\pm\infty$ (overflow, $1/0$), NaN ("not a number", for $0/0$ or $\sqrt{-1}$), and *subnormal* numbers below $\beta^{e_{\min}-1}$ that fill the gap around $0$ with less precision. Since $0.1$ is not a finite binary fraction, $0.1+0.2$ prints as $0.30000000000000004$; but every integer up to $2^{53}$ is exact, and $2^{53}+1$ rounds to $2^{53}$.

:::

::: {#prp-cancellation .proposition name="Cancellation"}

Let $\hat x=x(1+\delta_1)$ and $\hat y=y(1+\delta_2)$ with $\lvert\delta_i\rvert\le\varepsilon$, and $x\ne y$. Then
$$\frac{\lvert(\hat x-\hat y)-(x-y)\rvert}{\lvert x-y\rvert}\le\varepsilon\,\frac{\lvert x\rvert+\lvert y\rvert}{\lvert x-y\rvert}.$$
Subtracting nearly equal numbers can thus turn tiny relative errors in the data into a large relative error in the result, even though the subtraction itself is exact or nearly so.

:::

::: {.proof}

1. $(\hat x-\hat y)-(x-y)=x\delta_1-y\delta_2$.

2. By the triangle inequality $\lvert x\delta_1-y\delta_2\rvert\le\varepsilon(\lvert x\rvert+\lvert y\rvert)$.

3. Divide by $\lvert x-y\rvert$.

:::

::: {#exm-quadratic-cancellation .example name="The quadratic formula"}

The roots of $x^2-10^8x+1=0$ are about $10^8$ and $10^{-8}$. In double precision the textbook formula $\bigl(b-\sqrt{b^2-4}\bigr)/2$ with $b=10^8$ returns $7.45\times10^{-9}$ for the small root: $\sqrt{b^2-4}$ agrees with $b$ in almost all digits, and its rounding error of size $\varepsilon_{\text{mach}}b\approx10^{-8}$ is comparable to the answer. The equivalent formula $2/\bigl(b+\sqrt{b^2-4}\bigr)$, obtained by multiplying top and bottom by the conjugate, adds instead of subtracting and returns $1.0000000000000000\times10^{-8}$, correct to all digits.

:::

::: {#exm-finite-difference-error .example name="Rounding versus truncation in a difference quotient"}

Approximate $f'(x)$ by $\bigl(f(x+h)-f(x)\bigr)/h$. By Taylor's theorem the *truncation error* is about $\tfrac h2\lvert f''(x)\rvert$. The values $f(x+h)$ and $f(x)$ carry rounding errors of size about $\varepsilon_{\text{mach}}\lvert f(x)\rvert$, which the subtraction keeps and the division by $h$ magnifies, giving a *rounding error* of about $\varepsilon_{\text{mach}}\lvert f(x)\rvert/h$. The total
$$\tfrac h2\lvert f''\rvert+\varepsilon_{\text{mach}}\lvert f\rvert/h$$
is smallest near $h\approx\sqrt{\varepsilon_{\text{mach}}}\approx10^{-8}$, where the error is also about $10^{-8}$: only half the digits survive.

:::

::: {#fig-floating-point-arithmetic-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.38cm, y=0.38cm]
\draw[->, faint] (-16.5,-9) -- (0.8,-9) node[lab, right] {$\log_{10}h$};
\draw[->, faint] (-16.5,-9) -- (-16.5,1.2) node[lab, above] {$\log_{10}\text{error}$};
\foreach \x in {-16,-12,-8,-4,0} {\draw[faint] (\x,-9.15) -- (\x,-8.85); \node[tick, below] at (\x,-9.15) {$\x$};}
\foreach \y in {-8,-4,0} {\draw[faint] (-16.65,\y) -- (-16.35,\y); \node[tick, left] at (-16.65,\y) {$\y$};}
\draw[emph] plot coordinates {(-16,0.43) (-15,-0.41) (-14,-2.03) (-13,-3.34) (-12,-3.36) (-11,-4.49) (-10,-5.81) (-9,-6.67) (-8,-8.18) (-7,-6.85) (-6,-5.87) (-5,-4.87) (-4,-3.87) (-3,-2.87) (-2,-1.87) (-1,-0.85) (0,0.29)};
\foreach \p in {(-16,0.43),(-15,-0.41),(-14,-2.03),(-13,-3.34),(-12,-3.36),(-11,-4.49),(-10,-5.81),(-9,-6.67),(-8,-8.18),(-7,-6.85),(-6,-5.87),(-5,-4.87),(-4,-3.87),(-3,-2.87),(-2,-1.87),(-1,-0.85),(0,0.29)} {\fill \p circle (2pt);}
\draw[faint, dashed] (-15,0) -- (-7,-8);
\draw[faint, dashed] (-8,-7.4) -- (0,0.6);
\node[lab] at (-9.4,-1.4) {rounding $\sim\varepsilon/h$};
\node[lab] at (-2.2,-6.2) {truncation $\sim h$};
\end{tikzpicture}
\end{center}
```

Error of the forward difference for $f(x)=e^x$ at $x=1$ in double precision, $h=10^{-16},\dots,10^0$. For large $h$ the error falls like $h$ (slope $1$); below $h\approx10^{-8}$ rounding takes over and the error grows like $\varepsilon_{\text{mach}}/h$ (slope $-1$, jagged because rounding errors are not smooth).

:::

::: {#rmk-floating-point-arithmetic-1 .remark name="Floating point is not random noise"}

Floating-point results are deterministic and often exact: sums and products of small integers, multiplication by powers of two, and $x-y$ when $y/2\le x\le2y$ (Sterbenz) incur no error at all. What is lost is *associativity*: $(x\oplus y)\oplus z$ and $x\oplus(y\oplus z)$ can differ, so reordering a computation changes its rounding errors. Error analysis therefore asks how errors propagate through a particular algorithm, which is the subject of @sec-math-numerical-floating-point-stability-and-backward-error.

:::
