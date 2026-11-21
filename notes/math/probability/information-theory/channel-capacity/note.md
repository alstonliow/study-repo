---
title: "Channel Capacity"
sources: [eecs126-8]
requires: [math/probability/information-theory/source-coding]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley EECS126 (Fall 2021), note "Capacity of the Binary Erasure Channel", in our own wording; proofs written out in steps. -->

Communication has three stages: compress the source (@thm-source-coding), add redundancy against the noise of the channel, and send. The second stage asks: at what rate can bits cross a noisy channel reliably?

::: {#def-channel-capacity .definition name="Channel, rate, capacity"}

A *discrete memoryless channel* takes an input $X$ and outputs $Y$ with a fixed conditional PMF $p(y\mid x)$, independently on each use. A *code of rate $R$* maps each of $2^{nR}$ messages to a block of $n$ inputs; the decoder guesses the message from the $n$ outputs. The rate $R$ is *achievable* if there are codes whose maximal error probability tends to $0$ as $n\to\infty$. The *capacity* is
$$C=\max_{p_X}I(X;Y),$$
the largest mutual information (@def-relative-entropy) over input distributions.

:::

::: {#thm-channel-coding .theorem name="Channel coding theorem (Shannon)"}

Every rate $R<C$ is achievable, and no rate $R>C$ is.

:::

::: {#fig-channel-capacity-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (6.4,0) node[lab, right] {rate $R$};
\path[shade] (0,-0.25) rectangle (4,0.25);
\draw[hl] (4,-0.4) -- (4,0.4) node[tick, above] {$C$};
\node[tick] at (2,0.55) {reliable codes exist};
\node[tick] at (5.2,0.55) {impossible};
\end{tikzpicture}
\end{center}
```

The channel coding theorem divides the rates: below capacity $C$ the error probability can be made arbitrarily small, above it it cannot

:::

We prove it for the simplest channel.

::: {#def-binary-erasure-channel .definition name="Binary erasure channel"}

The *binary erasure channel* $\operatorname{BEC}(p)$ has input $X\in\{0,1\}$ and output $Y\in\{0,1,e\}$: each bit is received correctly with probability $1-p$ and replaced by the erasure symbol $e$ with probability $p$, independently.

:::

::: {#fig-channel-capacity-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (x0) at (0,1.6) {$0$};
\node[small vertex] (x1) at (0,0) {$1$};
\node[small vertex] (y0) at (3.6,1.9) {$0$};
\node[small vertex, fill=accentLight, draw=accent] (ye) at (3.6,0.8) {$e$};
\node[small vertex] (y1) at (3.6,-0.3) {$1$};
\draw[map] (x0) -- node[edge label, above] {$1-p$} (y0);
\draw[map] (x0) -- node[edge label, pos=0.35, above right] {$p$} (ye);
\draw[map] (x1) -- node[edge label, pos=0.35, below right] {$p$} (ye);
\draw[map] (x1) -- node[edge label, below] {$1-p$} (y1);
\node[lab] at (0,2.4) {input $X$}; \node[lab] at (3.6,2.6) {output $Y$};
\end{tikzpicture}
\end{center}
```

The binary erasure channel $\operatorname{BEC}(p)$: each bit arrives intact with probability $1-p$ or is replaced by the erasure symbol $e$ with probability $p$. The receiver always knows which bits were lost; the capacity is $1-p$ (@thm-bec-capacity).

:::

::: {#thm-bec-capacity .theorem name="Capacity of the binary erasure channel"}

The capacity of $\operatorname{BEC}(p)$ is $1-p$ bits per use, and every rate $R<1-p$ is achieved by random linear codes.

:::

::: {.proof}

1. *Mutual information.* If $\Pr(X=1)=q$, then $H(X\mid Y)=p\,h(q)$ (the input is unknown exactly after an erasure), so $I(X;Y)=H(X)-H(X\mid Y)=(1-p)h(q)\le1-p$, with equality at $q=\tfrac12$. So $C=1-p$.

2. *Random code.* Choose a random $n\times k$ binary matrix $G$ with i.i.d. fair entries, $k=nR$, and send $x=Gm$ for a message $m\in\{0,1\}^k$. The receiver sees the rows of $G$ that were not erased, about $n(1-p)$ of them, and decodes by solving the linear system $G_Sm=x_S$ over $\mathbb F_2$ for the surviving rows $S$.

3. *Decoding works when $G_S$ has rank $k$.* For a fixed non-zero $m'$, $G_Sm'$ is uniform on $\{0,1\}^{|S|}$, so $\Pr(G_Sm'=0)=2^{-|S|}$. By the union bound over the $2^k-1$ non-zero vectors, the kernel is trivial except with probability at most $2^{k-|S|}$.

4. *Enough rows survive.* $|S|\sim\operatorname{Bin}(n,1-p)$, so by the law of large numbers $|S|\ge n(1-p-\delta)$ with probability tending to $1$ for any $\delta>0$. Taking $\delta=(1-p-R)/2$, the error probability is at most $2^{-n\delta}+o(1)\to0$.

5. *Converse.* A message of $nR$ bits cannot be recovered from the $|S|\approx n(1-p)$ unerased bits if $nR>|S|$: at least $2^{nR-|S|}$ messages agree on the received bits, so the error probability stays bounded away from $0$ when $R>1-p$.

:::

::: {#fig-channel-capacity-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (4.8,0) node[lab, right] {$p$};
\draw[->] (0,0) -- (0,2.6) node[lab, above] {$C$};
\draw[emph] (0,2.2) -- (4,0);
\draw (4,0) -- (4,-0.08) node[tick, below] {$1$};
\draw (0,2.2) -- (-0.08,2.2) node[tick, left] {$1$};
\end{tikzpicture}
\end{center}
```

The capacity of the binary erasure channel falls linearly, $C=1-p$: the fraction of bits that are erased is lost, and the rest arrives intact

:::

::: {#rmk-channel-capacity-feedback .remark name="With feedback it is easy"}

If the sender learns which bits were erased, it can simply resend each erased bit; on average $1/(1-p)$ uses carry one bit, rate $1-p$. The theorem says the same rate is possible without feedback. Fountain codes (a lab topic of the course) achieve it in practice for erasures.

:::
