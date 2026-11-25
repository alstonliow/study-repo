---
title: "Polynomial Multiplication and the Fast Fourier Transform"
sources: [mit6046-3]
requires: [cs/algorithms/divide-and-conquer, math/discrete/polynomials/interpolation]
aliases: [cs/algorithm-design/fast-fourier-transform]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-17 from MIT 6.046 (Spring 2015), Lecture 3, in our own wording; proofs written out in steps. Complex numbers are assumed. -->

A polynomial $A(x)=a_0+a_1x+\dots+a_{n-1}x^{n-1}$ can be stored in three ways:

1. *coefficients* $(a_0,\dots,a_{n-1})$;
2. *roots* $r_1,\dots,r_{n-1}$ and a leading coefficient;
3. *samples* $(x_k,A(x_k))$ at $n$ distinct points, which determine $A$ uniquely (@thm-interpolation).

| operation | coefficients | roots | samples |
|---|---|---|---|
| evaluate at a point | $O(n)$ (Horner) | $O(n)$ | $O(n^2)$ |
| add | $O(n)$ | impossible in general | $O(n)$ |
| multiply | $O(n^2)$ | $O(n)$ | $O(n)$ |

No representation is good at everything. Multiplying in coefficient form is a *convolution*, $c_k=\sum_ja_jb_{k-j}$, which costs $O(n^2)$; in sample form it is pointwise, $C(x_k)=A(x_k)B(x_k)$. So we convert: coefficients $\to$ samples (evaluate), multiply pointwise, samples $\to$ coefficients (interpolate). The conversion is the hard part.

## Evaluating at roots of unity

Evaluating at $n$ arbitrary points costs $\Theta(n^2)$. The trick is to choose the points so that the problem halves.

::: {#def-roots-of-unity .definition name="Roots of unity"}

For $n$ a power of $2$, the *$n$-th roots of unity* are $\omega_n^k=e^{2\pi ik/n}=\cos\frac{2\pi k}n+i\sin\frac{2\pi k}n$ for $k=0,\dots,n-1$. Their squares are the $\frac n2$-th roots of unity, each taken twice: $(\omega_n^k)^2=\omega_{n/2}^k$ and $\omega_n^{k+n/2}=-\omega_n^k$.

:::

::: {#def-dft .definition name="Discrete Fourier transform"}

The *DFT* of $(a_0,\dots,a_{n-1})$ is the vector of values $A(\omega_n^k)$ for $k=0,\dots,n-1$.

:::

::: {#thm-fft .theorem name="Fast Fourier transform"}

Split $A(x)=A_{\rm even}(x^2)+x\,A_{\rm odd}(x^2)$, where $A_{\rm even}$ has coefficients $a_0,a_2,\dots$ and $A_{\rm odd}$ has $a_1,a_3,\dots$. Compute the DFTs of $A_{\rm even}$ and $A_{\rm odd}$ (size $\frac n2$) recursively; then for $k<\frac n2$
$$A(\omega_n^k)=A_{\rm even}(\omega_{n/2}^k)+\omega_n^kA_{\rm odd}(\omega_{n/2}^k),\qquad A(\omega_n^{k+n/2})=A_{\rm even}(\omega_{n/2}^k)-\omega_n^kA_{\rm odd}(\omega_{n/2}^k).$$
This computes the DFT in $O(n\log n)$ time.

:::

::: {.proof}

1. The split is a regrouping of the terms of $A$ by the parity of the exponent.

2. Substituting $x=\omega_n^k$, the arguments $x^2=\omega_{n/2}^k$ of $A_{\rm even}$ and $A_{\rm odd}$ range over only $\frac n2$ values (@def-roots-of-unity), so two DFTs of size $\frac n2$ give them all. The second formula uses $\omega_n^{k+n/2}=-\omega_n^k$ and $(\omega_n^{k+n/2})^2=\omega_{n/2}^k$.

3. Combining costs $O(n)$, so $T(n)=2T(n/2)+O(n)=O(n\log n)$.

:::

```{=latex}
\begin{algorithm}
\caption{FFT$(a,\omega)$}
\begin{algorithmic}
\INPUT Coefficients $a=(a_0,\dots,a_{n-1})$, $n$ a power of $2$; a primitive $n$-th root of unity $\omega$ ($\omega_n$ for the DFT)
\OUTPUT $y_k=A(\omega^k)$ for $k=0,\dots,n-1$
\IF{$n=1$}
    \RETURN $(a_0)$
\ENDIF
\STATE $e\gets$ FFT$((a_0,a_2,\dots,a_{n-2}),\omega^2)$; $o\gets$ FFT$((a_1,a_3,\dots,a_{n-1}),\omega^2)$
\FOR{$k=0$ to $n/2-1$}
    \STATE $y_k\gets e_k+\omega^ko_k$; $y_{k+n/2}\gets e_k-\omega^ko_k$
\ENDFOR
\RETURN $y$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-fast-fourier-transform-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (n00) at (6.00,0.00) {$a_0,a_1,a_2,a_3,a_4,a_5,a_6,a_7$};
\node[box] (n10) at (3.00,-0.85) {$a_0,a_2,a_4,a_6$};
\node[box] (n20) at (1.50,-1.70) {$a_0,a_4$};
\node[box] (n30) at (0.75,-2.55) {$a_0$};
\node[box] (n32) at (2.25,-2.55) {$a_4$};
\draw (n20) -- (n30);
\draw (n20) -- (n32);
\node[box] (n23) at (4.50,-1.70) {$a_2,a_6$};
\node[box] (n33) at (3.75,-2.55) {$a_2$};
\node[box] (n34) at (5.25,-2.55) {$a_6$};
\draw (n23) -- (n33);
\draw (n23) -- (n34);
\draw (n10) -- (n20);
\draw (n10) -- (n23);
\node[box] (n16) at (9.00,-0.85) {$a_1,a_3,a_5,a_7$};
\node[box] (n26) at (7.50,-1.70) {$a_1,a_5$};
\node[box] (n36) at (6.75,-2.55) {$a_1$};
\node[box] (n38) at (8.25,-2.55) {$a_5$};
\draw (n26) -- (n36);
\draw (n26) -- (n38);
\node[box] (n29) at (10.50,-1.70) {$a_3,a_7$};
\node[box] (n39) at (9.75,-2.55) {$a_3$};
\node[box] (n310) at (11.25,-2.55) {$a_7$};
\draw (n29) -- (n39);
\draw (n29) -- (n310);
\draw (n16) -- (n26);
\draw (n16) -- (n29);
\draw (n00) -- (n10);
\draw (n00) -- (n16);
\end{tikzpicture}
\end{center}
```

The recursion of the FFT for $n=8$: each polynomial splits into its even- and odd-indexed coefficients. There are $\lg n$ levels, and combining the two halves at each level costs $O(n)$, so the transform takes $O(n\lg n)$ time.

:::

::: {#prp-inverse-dft .proposition name="Inverse transform"}

Let $V$ be the $n\times n$ matrix with entries $V_{jk}=\omega_n^{jk}$, so that the DFT is $a\mapsto Va$. Then $V^{-1}=\frac1n\overline V$, where $\overline V_{jk}=\omega_n^{-jk}$. So interpolation is an FFT with $\omega_n^{-1}$ in place of $\omega_n$, followed by division by $n$, again $O(n\log n)$.

:::

::: {.proof}

1. The $(j,l)$ entry of $\overline VV$ is $\sum_k\omega_n^{k(l-j)}$.

2. If $l=j$ every term is $1$ and the sum is $n$.

3. If $l\ne j$, then $q=\omega_n^{l-j}\ne1$ but $q^n=1$, so the geometric sum is $\frac{q^n-1}{q-1}=0$.

4. Hence $\overline VV=nI$.

:::

```{=latex}
\begin{algorithm}
\caption{Inverse DFT}
\begin{algorithmic}
\INPUT Values $y_k=A(\omega_n^k)$, $k=0,\dots,n-1$
\OUTPUT The coefficients $a$ of $A$
\STATE $a\gets$ FFT$(y,\omega_n^{-1})$
\RETURN $a/n$ \COMMENT{divide every entry by $n$}
\end{algorithmic}
\end{algorithm}
```

::: {#cor-fast-polynomial-multiplication .corollary name="Fast polynomial multiplication"}

Two polynomials of degree less than $n$ can be multiplied in $O(n\log n)$ time: pad both to length $N\ge2n$ (a power of $2$), apply the FFT to each, multiply the $N$ values pointwise, and apply the inverse FFT.

:::

```{=latex}
\begin{algorithm}
\caption{Polynomial multiplication by FFT}
\begin{algorithmic}
\INPUT Coefficients $a$ and $b$ of two polynomials of degree less than $n$
\OUTPUT The coefficients $c$ of their product
\STATE $N\gets$ the least power of $2$ with $N\ge2n$; pad $a$ and $b$ with zeros to length $N$
\STATE $\hat a\gets$ FFT$(a,\omega_N)$; $\hat b\gets$ FFT$(b,\omega_N)$
\FOR{$k=0$ to $N-1$}
    \STATE $\hat c_k\gets\hat a_k\hat b_k$
\ENDFOR
\RETURN the inverse DFT of $\hat c$
\end{algorithmic}
\end{algorithm}
```

::: {#fig-fast-fourier-transform-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,0.000) rectangle (1.150,1.150);
\node[lab] at (0.575,0.575) {$1$};
\draw[cell frame] (1.150,0.000) rectangle (2.300,1.150);
\node[lab] at (1.725,0.575) {$1$};
\draw[cell frame] (2.300,0.000) rectangle (3.450,1.150);
\node[lab] at (2.875,0.575) {$0$};
\draw[cell frame] (3.450,0.000) rectangle (4.600,1.150);
\node[lab] at (4.025,0.575) {$0$};
\node[lab, anchor=east] at (-0.100,0.575) {$a$};
\draw[cell frame] (0.000,-0.750) rectangle (1.150,0.400);
\node[lab] at (0.575,-0.175) {$1$};
\draw[cell frame] (1.150,-0.750) rectangle (2.300,0.400);
\node[lab] at (1.725,-0.175) {$2$};
\draw[cell frame] (2.300,-0.750) rectangle (3.450,0.400);
\node[lab] at (2.875,-0.175) {$0$};
\draw[cell frame] (3.450,-0.750) rectangle (4.600,0.400);
\node[lab] at (4.025,-0.175) {$0$};
\node[lab, anchor=east] at (-0.100,-0.175) {$b$};
\draw[cell frame] (0.000,-1.500) rectangle (1.150,-0.350);
\node[lab] at (0.575,-0.925) {$2$};
\draw[cell frame] (1.150,-1.500) rectangle (2.300,-0.350);
\node[lab] at (1.725,-0.925) {$1+i$};
\draw[cell frame] (2.300,-1.500) rectangle (3.450,-0.350);
\node[lab] at (2.875,-0.925) {$0$};
\draw[cell frame] (3.450,-1.500) rectangle (4.600,-0.350);
\node[lab] at (4.025,-0.925) {$1-i$};
\node[lab, anchor=east] at (-0.100,-0.925) {$\hat a=\mathrm{FFT}(a)$};
\draw[cell frame] (0.000,-2.250) rectangle (1.150,-1.100);
\node[lab] at (0.575,-1.675) {$3$};
\draw[cell frame] (1.150,-2.250) rectangle (2.300,-1.100);
\node[lab] at (1.725,-1.675) {$1+2i$};
\draw[cell frame] (2.300,-2.250) rectangle (3.450,-1.100);
\node[lab] at (2.875,-1.675) {$-1$};
\draw[cell frame] (3.450,-2.250) rectangle (4.600,-1.100);
\node[lab] at (4.025,-1.675) {$1-2i$};
\node[lab, anchor=east] at (-0.100,-1.675) {$\hat b=\mathrm{FFT}(b)$};
\draw[cell frame] (0.000,-3.000) rectangle (1.150,-1.850);
\node[lab] at (0.575,-2.425) {$6$};
\draw[cell frame] (1.150,-3.000) rectangle (2.300,-1.850);
\node[lab] at (1.725,-2.425) {$-1+3i$};
\draw[cell frame] (2.300,-3.000) rectangle (3.450,-1.850);
\node[lab] at (2.875,-2.425) {$0$};
\draw[cell frame] (3.450,-3.000) rectangle (4.600,-1.850);
\node[lab] at (4.025,-2.425) {$-1-3i$};
\node[lab, anchor=east] at (-0.100,-2.425) {$\hat c=\hat a\hat b$};
\draw[hl cell] (0.000,-3.750) rectangle (1.150,-2.600);
\node[lab] at (0.575,-3.175) {$1$};
\draw[hl cell] (1.150,-3.750) rectangle (2.300,-2.600);
\node[lab] at (1.725,-3.175) {$3$};
\draw[hl cell] (2.300,-3.750) rectangle (3.450,-2.600);
\node[lab] at (2.875,-3.175) {$2$};
\draw[hl cell] (3.450,-3.750) rectangle (4.600,-2.600);
\node[lab] at (4.025,-3.175) {$0$};
\node[lab, anchor=east] at (-0.100,-3.175) {$c=\frac14\mathrm{FFT}(\hat c,\omega^{-1})$};
\node[lab,tick] at (0.57,0.95) {$k=0$};
\node[lab,tick] at (1.72,0.95) {$k=1$};
\node[lab,tick] at (2.88,0.95) {$k=2$};
\node[lab,tick] at (4.02,0.95) {$k=3$};
\end{tikzpicture}
\end{center}
```

Multiplying $1+x$ by $1+2x$ with $N=4$ and $\omega_4=i$. The FFT gives the values at $1,i,-1,-i$; the products of the values are the values of the product; the inverse transform (an FFT with $\omega^{-1}=-i$, then division by $4$) recovers the coefficients $1,3,2,0$: the product is $1+3x+2x^2$.

:::

The product has degree less than $2n-1$, which is why $N\ge2n$ samples are needed. The same method multiplies large integers (as polynomials in the base) and computes convolutions in signal and image processing.
