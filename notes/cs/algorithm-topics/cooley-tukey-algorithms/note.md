---
title: "Cooley–Tukey FFTs for General Sizes"
sources: [mit18335-38, mit18335-39]
requires: [cs/algorithm-topics/fast-fourier-transform]
aliases: [cs/algorithm-design/cooley-tukey-algorithms]   # old ids (moved)
status: draft
---

<!-- Added 2026-11-22 from MIT 18.335 (Spring 2019), Lectures 38 and 39 (the DFT and FFT algorithms; FFT algorithms and FFTW) and the note on FFT algorithms, in our own wording; proofs written out in steps; the accuracy comparison was computed with numpy and scipy (single precision against a double-precision reference). -->

The radix-2 FFT (@thm-fft) splits a transform of size $N$ into two of size $N/2$. Cooley and Tukey's algorithm works for any factorisation $N=N_1N_2$: it re-indexes the one-dimensional transform as a two-dimensional one, with a diagonal twiddle-factor multiplication in between. Recursing on the factors gives $O(N\log N)$ for every $N$ with small prime factors, and other algorithms handle large primes. Here we use the signal-processing convention $y_k=\sum_{n=0}^{N-1}x_n\,\omega_N^{nk}$ with $\omega_N=e^{-2\pi i/N}$; replacing $\omega_N$ by $\overline{\omega_N}$ gives the polynomial-evaluation convention of @def-dft and changes nothing below.

::: {#thm-cooley-tukey-general .theorem name="Cooley–Tukey for N = N1 N2" generalizes="thm-fft"}

Let $N=N_1N_2$ and write $n=N_1n_2+n_1$ and $k=N_2k_1+k_2$ with $0\le n_1,k_1<N_1$ and $0\le n_2,k_2<N_2$. Then
$$y_{N_2k_1+k_2}=\sum_{n_1=0}^{N_1-1}\omega_{N_1}^{n_1k_1}\Bigl[\omega_N^{n_1k_2}\Bigl(\sum_{n_2=0}^{N_2-1}x_{N_1n_2+n_1}\,\omega_{N_2}^{n_2k_2}\Bigr)\Bigr].$$
So a DFT of size $N$ is computed by $N_1$ DFTs of size $N_2$ (the inner sums), multiplication by the $N$ *twiddle factors* $\omega_N^{n_1k_2}$, and $N_2$ DFTs of size $N_1$ (the outer sums).

:::

::: {.proof}

1. Expand the exponent: $nk=(N_1n_2+n_1)(N_2k_1+k_2)=Nn_2k_1+N_1n_2k_2+N_2n_1k_1+n_1k_2$.

2. $\omega_N^{Nn_2k_1}=1$, $\omega_N^{N_1n_2k_2}=\omega_{N_2}^{n_2k_2}$ and $\omega_N^{N_2n_1k_1}=\omega_{N_1}^{n_1k_1}$, since $\omega_N^{N_1}=\omega_{N_2}$ and $\omega_N^{N_2}=\omega_{N_1}$.

3. As $n$ runs over $0,\dots,N-1$, the pair $(n_1,n_2)$ runs over all index pairs exactly once, so $y_k=\sum_{n_1}\sum_{n_2}x_{N_1n_2+n_1}\omega_{N_2}^{n_2k_2}\omega_N^{n_1k_2}\omega_{N_1}^{n_1k_1}$, which is the stated nesting.

4. For $N_1=2$ this is the even/odd split of @thm-fft with the roles of the two sizes as above (*decimation in time*); choosing $N_2=2$ instead gives the *decimation in frequency* variant.

:::

::: {#fig-cooley-tukey-algorithms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.85cm, y=0.85cm]
\foreach \a in {0,1} {\foreach \b in {0,1,2} {\pgfmathtruncatemacro{\n}{2*\b+\a} \draw[cell frame] (\b,-\a) rectangle ++(1,-1); \node[tick] at (\b+0.5,-\a-0.5) {$x_{\n}$};}}
\node[note] at (1.5,0.45) {$n=2n_2+n_1$};
\node[note, anchor=east] at (-0.1,-0.5) {$n_1=0$}; \node[note, anchor=east] at (-0.1,-1.5) {$n_1=1$};
\draw[map] (3.2,-1) -- (5.0,-1) node[midway, note, above] {row DFTs};
\node[note] at (4.1,-1.45) {(size $3$)};
\foreach \a in {0,1} {\foreach \b in {0,1,2} {\draw[cell frame] (5.2+\b,-\a) rectangle ++(1,-1);}}
\foreach \b in {1,2} {\draw[hl cell] (5.2+\b,-1) rectangle ++(1,-1); \node[tick] at (5.7+\b,-1.5) {$\omega_6^{\b}$};}
\node[note] at (6.7,0.45) {twiddles (shaded)};
\draw[map] (8.4,-1) -- (10.2,-1) node[midway, note, above] {column DFTs};
\node[note] at (9.3,-1.45) {(size $2$)};
\foreach \a in {0,1} {\foreach \b in {0,1,2} {\pgfmathtruncatemacro{\k}{3*\a+\b} \draw[cell frame] (10.4+\b,-\a) rectangle ++(1,-1); \node[tick] at (10.9+\b,-\a-0.5) {$y_{\k}$};}}
\node[note] at (11.9,0.45) {$k=3k_1+k_2$};
\end{tikzpicture}
\end{center}
```

Cooley–Tukey for $N=6=2\cdot3$: the input is arranged as a $2\times3$ array by $n=2n_2+n_1$, each row is transformed (size $3$), the entries with $n_1=1$ are multiplied by twiddle factors $\omega_6^{k_2}$, each column is transformed (size $2$), and the output is read with $k=3k_1+k_2$, i.e. transposed.

:::

::: {#cor-fft-operation-count .corollary name="Cost for highly composite N"}

If $N=p_1p_2\cdots p_m$ with all $p_j\le P$, recursive application of @thm-cooley-tukey-general computes the DFT in $O\bigl(N\sum_jp_j\bigr)\subseteq O(PN\log_2N)$ operations. For $N=2^m$ the radix-2 algorithm uses $\sim5N\log_2N$ real flops.

:::

::: {.proof}

1. Let $C(N)$ be the cost. One step with $N=p\cdot(N/p)$ does $N/p$ DFTs of size $p$ directly ($O(p^2)$ each), $N$ twiddle multiplications and $p$ transforms of size $N/p$: $C(N)=pC(N/p)+O(Np)$.

2. Unrolling over the factors, $C(N)=O\bigl(N(p_1+\dots+p_m)\bigr)$. Since $m\le\log_2N$ and each $p_j\le P$, this is $O(PN\log_2N)$.

3. For radix $2$, each of the $\log_2N$ stages does $N/2$ butterflies $(a,b)\mapsto(a+\omega b,\ a-\omega b)$: one complex multiplication ($6$ real flops) and two complex additions ($4$ real flops), $10\cdot N/2=5N$ flops per stage.

:::

::: {#rmk-cooley-tukey-algorithms-1 .remark name="Prime sizes"}

For a large prime $N$ Cooley–Tukey gives nothing, but $O(N\log N)$ is still possible. *Rader's algorithm* uses a generator $g$ of the multiplicative group modulo $N$ to rewrite the DFT outputs $y_{g^{-q}}$, $q=0,\dots,N-2$, as a cyclic convolution of length $N-1$, computed by FFTs of size $N-1$ (or of a padded power-of-two size). *Bluestein's algorithm* writes $nk=\tfrac12\bigl(n^2+k^2-(k-n)^2\bigr)$, which turns any DFT into a convolution with the "chirp" $\omega_N^{-m^2/2}$, again computed by power-of-two FFTs.

:::

::: {#rmk-cooley-tukey-algorithms-2 .remark name="Fast in practice: FFTW"}

Operation counts no longer determine speed (@sec-math-numerical-direct-solvers-caches-and-blocking). The FFTW library generates optimised straight-line *codelets* for small sizes, and a *planner* measures at run time which factorisation, radix and loop order are fastest on the given machine. Recursive decompositions are naturally cache-oblivious: the subtransforms eventually fit in every level of cache. Real-input, real-symmetric (cosine) and multidimensional transforms reuse the same machinery, and the cosine transforms are what Chebyshev interpolation and Clenshaw–Curtis quadrature need (@def-clenshaw-curtis).

:::

::: {#prp-fft-accuracy .proposition name="Accuracy of the FFT"}

With exactly rounded twiddle factors, the radix-2 FFT in floating point computes $\tilde y$ with
$$\frac{\lVert\tilde y-y\rVert_2}{\lVert y\rVert_2}=O(\varepsilon_{\text{mach}}\log_2N)$$
in the worst case, and $O(\varepsilon_{\text{mach}}\sqrt{\log_2N})$ on average; the direct matrix–vector product has worst-case error $O(\varepsilon_{\text{mach}}N)$ and average $O(\varepsilon_{\text{mach}}\sqrt N)$.

:::

::: {.proof}

1. Each stage applies the butterflies, a matrix $B_j$ that is $\sqrt2$ times a unitary matrix, in floating point; each output of a butterfly has a relative error $O(\varepsilon_{\text{mach}})$, so the computed stage is $B_j(I+E_j)$ applied to its input with $\lVert E_j\rVert=O(\varepsilon_{\text{mach}})$.

2. The DFT is $F=B_m\cdots B_1P$ with $P$ a permutation, and $\lVert F\mathbf{x}\rVert=\sqrt N\lVert\mathbf{x}\rVert=2^{m/2}\lVert\mathbf{x}\rVert$. Since each $B_j/\sqrt2$ is unitary, errors introduced at stage $j$ are scaled exactly as the signal is by the later stages, and contribute a relative error $O(\varepsilon_{\text{mach}})$ to the output.

3. Summing $m=\log_2N$ stages gives the worst case $O(\varepsilon_{\text{mach}}\log_2N)$; if the stage errors behave like independent random vectors, their norms add in quadrature, giving $O(\varepsilon_{\text{mach}}\sqrt{\log_2N})$.

4. The direct product forms each output as a sum of $N$ terms, whose rounding errors behave as in recursive summation (@thm-naive-summation-backward and @sec-math-numerical-floating-point-summation-error).

:::

::: {#fig-cooley-tukey-algorithms-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.8cm, y=1.4cm]
\draw[->, faint] (3,-7.3) -- (12.8,-7.3) node[lab, right] {$\log_2N$};
\draw[->, faint] (3,-7.3) -- (3,-5.6) node[lab, above] {$\log_{10}$ relative error};
\foreach \x in {4,6,...,12} {\draw[faint] (\x,-7.34) -- (\x,-7.26); \node[tick, below] at (\x,-7.34) {$\x$};}
\foreach \y in {-7,-6.5,-6} {\draw[faint] (2.94,\y) -- (3.06,\y); \node[tick, left] at (2.94,\y) {$\y$};}
\draw[hl] plot coordinates {(4,-7.17) (6,-7.02) (8,-6.99) (10,-6.96) (12,-6.90)};
\draw[emph] plot coordinates {(4,-7.06) (6,-6.82) (8,-6.57) (10,-6.23) (12,-5.93)};
\node[lab] at (11.2,-7.15) {FFT};
\node[lab] at (11.0,-6.0) {direct sum};
\end{tikzpicture}
\end{center}
```

Relative error of the DFT of a random complex vector computed in single precision, by scipy's FFT and by the direct sum over $N$ terms, against a double-precision reference. The FFT error barely grows with $N$; the direct sum's grows like $\sqrt N$ (slope $0.15$ per doubling).

:::
