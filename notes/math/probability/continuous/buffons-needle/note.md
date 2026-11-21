---
title: "Buffon's Needle"
sources: [cs70-20.6]
requires: [math/probability/continuous/continuous-random-variables, math/probability/discrete/indicator-variables]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 20 (cs70-20.6, optional section), in our own wording; proofs written out in steps. -->

A needle of length $\ell$ is thrown at random onto a floor ruled with parallel lines at distance $\ell$ apart. The probability that it crosses a line turns out to be $\frac2\pi$, so the fraction of crossings in many throws estimates $\pi$ (@thm-law-of-large-numbers). We prove the value twice.

::: {#fig-buffons-needle-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.3cm,y=1.3cm]
\foreach \y in {0,2} \draw[emph, muted] (-0.3,\y) -- (4.6,\y);
\draw[bold, accent] (1.626,-0.169) -- (2.774,1.469);
\fill[ink] (2.2,0.65) circle[pt];
\draw[faint, dashed] (2.2,0.65) -- (2.2,1.9);
\draw[<->, primary] (1.300,0) -- node[lab, left] {$Y$} (1.300,0.65);
\draw[faint, dashed] (1.200,0.65) -- (2.2,0.65);
\draw[primary] (2.2,1.15) arc[start angle=90, end angle=55, radius=0.5];
\node[lab, primary] at (2.35,1.4) {$\Theta$};
\draw[<->, muted] (4.3,0) -- node[lab, right] {$\ell$} (4.3,2);
\end{tikzpicture}
\end{center}
```

The position of the needle: the distance $Y$ from its midpoint to the nearest line, and its angle $\Theta$ to the normal. It crosses a line when $Y\le\frac\ell2\cos\Theta$.

:::

::: {#thm-buffons-needle .theorem name="Buffon's needle"}

A needle of length $\ell$ thrown at random onto a floor with parallel lines at distance $\ell$ apart crosses a line with probability $\dfrac2\pi$.

:::

::: {.proof}

*First proof: integrating a joint density.*

1. The position of the needle relative to the lines is given by two random variables: the distance $Y$ from its midpoint to the nearest line, in $[0,\frac\ell2]$, and the angle $\Theta$ between the needle and the normal to the lines, in $[-\frac\pi2,\frac\pi2]$. A random throw means that $(Y,\Theta)$ is uniform on this rectangle, whose area is $\frac{\pi\ell}2$: its joint density is $f(y,\theta)=\frac2{\pi\ell}$ there and $0$ elsewhere.

2. The two ends of the needle lie at distance $\frac\ell2\cos\Theta$ from the midpoint, measured along the normal. So the needle crosses a line exactly when $Y\le\frac\ell2\cos\Theta$.

3. Integrate the density over this region (@def-joint-density):
   $$\Pr\Bigl(Y\le\tfrac\ell2\cos\Theta\Bigr)=\int_{-\pi/2}^{\pi/2}\int_0^{(\ell/2)\cos\theta}\frac2{\pi\ell}\,dy\,d\theta=\int_{-\pi/2}^{\pi/2}\frac{\cos\theta}\pi\,d\theta=\frac1\pi\Bigl[\sin\theta\Bigr]_{-\pi/2}^{\pi/2}=\frac2\pi.$$

:::

::: {#fig-buffons-needle-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.3cm,y=2.4cm]
\fill[shade, domain=-1.5708:1.5708, samples=60] (-1.5708,0) -- plot (\x,{cos(\x r)}) -- (1.5708,0) -- cycle;
\draw[cell frame, fill=none] (-1.5708,0) rectangle (1.5708,1);
\draw[emph, primary, domain=-1.5708:1.5708, samples=60] plot (\x,{cos(\x r)});
\draw[->, muted] (-2,0) -- (2.1,0) node[lab, right] {$\theta$};
\draw[->, muted] (0,0) -- (0,1.3) node[lab, above] {$y$};
\node[tick, below] at (-1.5708,0) {$-\frac\pi2$}; \node[tick, below] at (1.5708,0) {$\frac\pi2$};
\node[tick, left] at (-1.6,1) {$\frac\ell2$};
\node[lab, primary] at (1.4,0.75) {$y=\frac\ell2\cos\theta$};
\end{tikzpicture}
\end{center}
```

$(\Theta,Y)$ is uniform on the rectangle; the needle crosses a line when the point lies in the shaded region, whose share of the rectangle is $\frac2\pi$.

:::

::: {#rmk-buffons-needle-noodle .remark name="Second proof: Buffon's noodle"}

Take lines at distance $1$, and let $p$ be the crossing probability for a needle of length $1$. A needle crosses at most one line except with probability $0$, so $p$ is also the expected number $E[X]$ of crossings (@prp-expectation-of-indicator).

1. *Expected crossings are proportional to length.* Cut a needle of length $1$ into $m$ equal pieces and let $I_k$ count the crossings of piece $k$. All pieces are thrown in the same random way, so the $E[I_k]$ are equal, and by @thm-linearity-of-expectation $E[X]=mE[I_1]$. So a piece of length $\frac1m$ has $\frac1m E[X]$ expected crossings, and by additivity again a needle of length $\frac km$ has $\frac kmE[X]$. Approximating any length $\ell$ by rationals, a needle of length $\ell$ has $\ell\,E[X]$ expected crossings.

2. *Bent needles.* Join needles of lengths $\ell_1,\dots,\ell_n$ end to end at hinges into a "noodle". Linearity of expectation still applies, even though the pieces are dependent, so the noodle has $(\ell_1+\dots+\ell_n)E[X]$ expected crossings. Letting the pieces become short, the same holds for any curve: the expected number of crossings is its length times $E[X]$.

3. *A circle.* A circle of diameter $1$ has length $\pi$ and, except with probability $0$, crosses the lines exactly twice. So $\pi E[X]=2$, and $p=E[X]=\frac2\pi$.

The limits in steps 1 and 2 need a continuity argument, which we do not give; the first proof is complete.

:::

::: {#fig-buffons-needle-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) -- (6,0);
\draw[faint] (0,1.2) -- (6,1.2);
\draw[faint] (0,2.4) -- (6,2.4);
\draw[emph] (0.800,0.500) -- (1.600,1.500) -- (2.600,0.900) -- (3.400,1.900) -- (4.400,2.700) -- (5.200,1.800);
\node[hl dot] at (1.36,1.2) {};
\node[hl dot] at (2.10,1.2) {};
\node[hl dot] at (2.84,1.2) {};
\node[hl dot] at (4.03,2.4) {};
\node[hl dot] at (4.67,2.4) {};
\end{tikzpicture}
\end{center}
```

A bent noodle crossing the lines. By linearity each small piece contributes its own expected number of crossings, so the expected count depends only on the total length

:::
