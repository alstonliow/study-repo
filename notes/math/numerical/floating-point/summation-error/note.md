---
title: "Rounding Errors in Summation"
sources: [mit18335-3]
requires: [math/numerical/floating-point/stability-and-backward-error]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lecture 3 and its two notes (accuracy of naive summation; backwards stability of recursive summation), in our own wording; proofs written out in steps; errors measured in Python with numpy float32 against math.fsum. -->

Adding $n$ numbers is the simplest computation whose rounding errors accumulate. Its analysis shows the typical pattern: the computed sum is the exact sum of slightly perturbed data, the perturbation grows with $n$, and a smarter order of operations makes it grow much more slowly.

::: {#def-naive-summation .definition name="Recursive (naive) summation"}

To compute $f(\mathbf{x})=\sum_{i=1}^nx_i$ for floating-point $x_i$, set $\tilde s_1=x_1$ and $\tilde s_k=\tilde s_{k-1}\oplus x_k$ for $k=2,\dots,n$, and return $\tilde f(\mathbf{x})=\tilde s_n$.

:::

::: {#thm-naive-summation-backward .theorem name="Recursive summation is backward stable"}

The computed sum is the exact sum of perturbed data:
$$\tilde f(\mathbf{x})=\sum_{i=1}^n x_i(1+\delta_i),\qquad \lvert\delta_i\rvert\le(n-1)\varepsilon_{\text{mach}}+O(\varepsilon_{\text{mach}}^2).$$
Consequently
$$\lvert\tilde f(\mathbf{x})-f(\mathbf{x})\rvert\le(n-1)\,\varepsilon_{\text{mach}}\sum_{i=1}^n\lvert x_i\rvert+O(\varepsilon_{\text{mach}}^2).$$

:::

::: {.proof}

1. *Claim:* $\tilde s_k=\sum_{i=1}^k x_i\prod_{j=\max(i,2)}^{k}(1+\varepsilon_j)$ with $\lvert\varepsilon_j\rvert\le\varepsilon_{\text{mach}}$. For $k=1$ the product is empty and $\tilde s_1=x_1$.

2. *Induction step.* By @def-floating-point-operations, $\tilde s_k=(\tilde s_{k-1}+x_k)(1+\varepsilon_k)$. Multiplying the expression for $\tilde s_{k-1}$ by $(1+\varepsilon_k)$ and adding $x_k(1+\varepsilon_k)$ gives the claim for $k$.

3. The term $x_i$ is multiplied by at most $n-1$ factors $(1+\varepsilon_j)$. Expanding the product, $\prod(1+\varepsilon_j)=1+\sum\varepsilon_j+(\text{products of two or more }\varepsilon\text{'s})$, so it equals $1+\delta_i$ with $\lvert\delta_i\rvert\le(n-1)\varepsilon_{\text{mach}}+O(\varepsilon_{\text{mach}}^2)$.

4. This is the backward-stability statement, with $\tilde x_i=x_i(1+\delta_i)$ and $\lvert\tilde x_i-x_i\rvert\le(n-1)\varepsilon_{\text{mach}}\lvert x_i\rvert$.

5. Subtracting $f(\mathbf{x})$ and using the triangle inequality, $\lvert\tilde f-f\rvert=\bigl\lvert\sum_ix_i\delta_i\bigr\rvert\le\max_i\lvert\delta_i\rvert\sum_i\lvert x_i\rvert$.

:::

Dividing by $\lvert f(\mathbf{x})\rvert$, the relative error is at most $(n-1)\varepsilon_{\text{mach}}$ times $\sum_i\lvert x_i\rvert/\lvert\sum_ix_i\rvert$. That ratio is the condition number of summation in the $1$-norm (@def-relative-condition-number): it is $1$ for numbers of one sign and huge when large terms cancel.

::: {#rmk-summation-error-1 .remark name="Average errors grow like √n"}

The bound $n\varepsilon_{\text{mach}}$ is a worst case in which all rounding errors have the same sign. If the $\varepsilon_j$ behave like independent random variables of mean zero and size about $\varepsilon_{\text{mach}}$, the error $\sum_ix_i\delta_i$ is a sum of $n$ random terms and grows like $\sqrt n$, a random walk. Real rounding errors are not random (for instance, summing many positive numbers of similar size into a growing partial sum biases them), so the observed growth lies between $\sqrt n$ and $n$.

:::

::: {#def-pairwise-summation .definition name="Pairwise (cascade) summation"}

Split the list into two halves, sum each half recursively in the same way, and add the two results: $\tilde f(x_1)=x_1$ and, for $n>1$, $\tilde f(x_1,\dots,x_n)=\tilde f(x_1,\dots,x_{\lfloor n/2\rfloor})\oplus\tilde f(x_{\lfloor n/2\rfloor+1},\dots,x_n)$. Each $x_i$ then passes through only about $\log_2n$ additions instead of up to $n-1$, so the backward error bound improves from $(n-1)\varepsilon_{\text{mach}}$ to about $\varepsilon_{\text{mach}}\log_2n$ (see the exercises). To avoid the cost of recursion one sums small blocks of, say, $100$ elements by the simple loop and combines the blocks pairwise; the bound worsens only by the block size.

:::

```{=latex}
\begin{algorithm}
\caption{Pairwise summation $\mathrm{psum}(x_1,\dots,x_n)$}
\begin{algorithmic}
\INPUT floating-point numbers $x_1,\dots,x_n$, $n\ge1$
\IF{$n=1$}
    \STATE \textbf{return} $x_1$
\ENDIF
\STATE $m\gets\lfloor n/2\rfloor$
\STATE \textbf{return} $\mathrm{psum}(x_1,\dots,x_m)\oplus\mathrm{psum}(x_{m+1},\dots,x_n)$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-summation-error-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm, y=0.95cm]
\foreach \i in {1,...,8} {\node[box] (x\i) at (\i,0) {$x_{\i}$};}
\foreach \i/\a/\b in {1/1/2,2/3/4,3/5/6,4/7/8} {\node[small vertex] (a\i) at ({\a+0.5},1.1) {$\oplus$}; \draw (x\a) -- (a\i); \draw (x\b) -- (a\i);}
\node[small vertex] (b1) at (2.5,2.2) {$\oplus$}; \draw (a1) -- (b1); \draw (a2) -- (b1);
\node[small vertex] (b2) at (6.5,2.2) {$\oplus$}; \draw (a3) -- (b2); \draw (a4) -- (b2);
\node[small vertex, fill=accentLight, draw=accent] (c) at (4.5,3.3) {$\oplus$}; \draw (b1) -- (c); \draw (b2) -- (c);
\begin{scope}[xshift=9.6cm]
\node[box] (y1) at (0,0) {$x_1$};
\node[box] (y2) at (1,0) {$x_2$};
\node[small vertex] (s2) at (0.5,0.75) {$\oplus$}; \draw (y1) -- (s2); \draw (y2) -- (s2);
\foreach \i/\p in {3/2,4/3,5/4,6/5,7/6,8/7} {\node[box] (y\i) at ({\i-1},0) {$x_{\i}$}; \node[small vertex] (s\i) at ({\i-1.5},{0.42*\i-0.1}) {$\oplus$}; \draw (s\p) -- (s\i); \draw (y\i) -- (s\i);}
\end{scope}
\end{tikzpicture}
\end{center}
```

Pairwise summation of eight numbers (left) has depth $\log_28=3$: every $x_i$ is touched by three roundings. Recursive summation (right) is a chain of depth $7$, and $x_1,x_2$ pass through all seven additions.

:::

::: {#fig-summation-error-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.5cm, y=1.1cm]
\draw[->, faint] (0.8,-8) -- (5.4,-8) node[lab, right] {$\log_{10}n$};
\draw[->, faint] (0.8,-8) -- (0.8,-4.8) node[lab, above] {$\log_{10}(\text{relative error})$};
\foreach \x in {1,...,5} {\draw[faint] (\x,-8.06) -- (\x,-7.94); \node[tick, below] at (\x,-8.06) {$\x$};}
\foreach \y in {-8,-7,-6,-5} {\draw[faint] (0.76,\y) -- (0.84,\y); \node[tick, left] at (0.76,\y) {$\y$};}
\draw[faint, dashed] (0.8,-7.22) -- (5.2,-7.22) node[lab, right] {$\varepsilon_{\text{mach}}$};
\draw[hl] plot coordinates {(1,-7.48) (2,-7.09) (3,-6.47) (4,-6.04) (5,-5.23)};
\foreach \p in {(1,-7.48),(2,-7.09),(3,-6.47),(4,-6.04),(5,-5.23)} {\fill[accent] \p circle (2.2pt);}
\draw[emph] plot coordinates {(1,-7.49) (2,-7.57) (3,-7.57) (4,-7.64) (5,-7.57)};
\foreach \p in {(1,-7.49),(2,-7.57),(3,-7.57),(4,-7.64),(5,-7.57)} {\fill \p circle (2.2pt);}
\node[lab] at (4.1,-5.45) {recursive};
\node[lab] at (3.0,-7.85) {pairwise};
\end{tikzpicture}
\end{center}
```

Mean relative error of summing $n$ uniform random numbers in $[0,1)$ in single precision ($\varepsilon_{\text{mach}}\approx6\times10^{-8}$), measured against an exact sum. The recursive sum loses about half a digit per tenfold increase in $n$; the pairwise sum stays at the level of a single rounding.

:::

::: {#def-compensated-summation .definition name="Compensated (Kahan) summation"}

Keep a running correction $c$ that captures the low-order bits lost in each addition: start with $s=x_1$, $c=0$, and for $k=2,\dots,n$ compute $y=x_k\ominus c$, $t=s\oplus y$, $c=(t\ominus s)\ominus y$, $s=t$. In exact arithmetic $c$ is always $0$; in floating point $(t\ominus s)\ominus y$ is (minus) the rounding error of $s\oplus y$, which is fed back into the next term. The computed sum satisfies $\tilde f=\sum_ix_i(1+\delta_i)$ with $\lvert\delta_i\rvert\le2\varepsilon_{\text{mach}}+O(n\varepsilon_{\text{mach}}^2)$, independent of $n$ to first order.

:::

```{=latex}
\begin{algorithm}
\caption{Compensated summation}
\begin{algorithmic}
\INPUT floating-point numbers $x_1,\dots,x_n$
\STATE $s\gets x_1$, $c\gets0$
\FOR{$k=2,\dots,n$}
    \STATE $y\gets x_k\ominus c$ \COMMENT{correct the new term}
    \STATE $t\gets s\oplus y$
    \STATE $c\gets(t\ominus s)\ominus y$ \COMMENT{what was lost in $s\oplus y$}
    \STATE $s\gets t$
\ENDFOR
\STATE \textbf{return} $s$
\end{algorithmic}
\end{algorithm}
```

::: {#exm-compensated-summation .example name="Adding many small numbers to a large one"}

In double precision, $1\oplus10^{-16}=1$ because $10^{-16}<\varepsilon_{\text{mach}}$. Adding $10^{-16}$ to $1$ a million times by recursive summation therefore returns exactly $1$, an absolute error of $10^{-10}$. Compensated summation returns $1.0000000001$ correctly rounded: after the first step $c=-10^{-16}$, and the lost pieces accumulate in $c$ until they are large enough to change $s$.

:::
