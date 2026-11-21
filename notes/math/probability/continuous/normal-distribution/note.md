---
title: "Normal Distribution"
sources: [cs70-20.4]
requires: [math/probability/continuous/continuous-random-variables]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 20 (cs70-20.4), in our own wording; proofs written out in steps. The proof that the density integrates to 1 is our own addition (CS70 leaves it as an exercise). -->

::: {#def-normal-distribution .definition name="Normal distribution"}

For $\mu\in\mathbb R$ and $\sigma>0$, $X$ is *normal* (Gaussian) with parameters $\mu,\sigma^2$, written $X\sim N(\mu,\sigma^2)$, if it has density
$$f(x)=\frac1{\sqrt{2\pi\sigma^2}}\,e^{-(x-\mu)^2/(2\sigma^2)}.$$
$N(0,1)$ is the *standard normal* distribution. The graph of $f$ is a bell-shaped curve, symmetric about $\mu$, whose width is set by $\sigma$.

:::

::: {#fig-normal-distribution-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.75cm,y=7cm]
\draw[->, muted] (-6.3,0) -- (6.5,0) node[lab, right] {$x$};
\draw[->, muted] (-6.3,0) -- (-6.3,0.47);
\foreach \x in {-6,-4,-2,0,2,4,6} \node[tick, below] at (\x,0) {$\x$};
\foreach \y in {0.1,0.2,0.3,0.4} \node[tick, left] at (-6.3,\y) {$\y$};
\draw[emph, primary, domain=-6:6, samples=100] plot (\x,{exp(-\x*\x/2)/sqrt(2*pi)});
\draw[emph, secondary, domain=-6:6, samples=100] plot (\x,{exp(-\x*\x/8)/sqrt(8*pi)});
\draw[emph, accent, domain=-4:6, samples=100] plot (\x,{exp(-(\x-2)*(\x-2)/2)/sqrt(2*pi)});
\node[lab, primary, anchor=east] at (-0.9,0.36) {$N(0,1)$};
\node[lab, secondary] at (-4.2,0.12) {$N(0,4)$};
\node[lab, accent, anchor=west] at (3.1,0.3) {$N(2,1)$};
\end{tikzpicture}
\end{center}
```

Normal densities: $\mu$ moves the bell, and $\sigma$ sets its width; a larger $\sigma$ gives a wider, lower bell.

:::

::: {#prp-gaussian-integral .proposition name="Gaussian integral"}

$\displaystyle\int_{-\infty}^{\infty}e^{-x^2/2}\,dx=\sqrt{2\pi}$. Hence the normal density integrates to $1$.

:::

::: {.proof}

1. Let $I=\int_{-\infty}^{\infty}e^{-x^2/2}\,dx$; it converges because $e^{-x^2/2}\le e^{-|x|+1/2}$. Then
   $$I^2=\int_{-\infty}^{\infty}e^{-x^2/2}dx\int_{-\infty}^{\infty}e^{-y^2/2}dy=\iint_{\mathbb R^2}e^{-(x^2+y^2)/2}\,dx\,dy.$$

2. In polar coordinates, $x^2+y^2=r^2$ and $dx\,dy=r\,dr\,d\theta$:
   $$I^2=\int_0^{2\pi}\int_0^\infty e^{-r^2/2}\,r\,dr\,d\theta=\int_0^{2\pi}\Bigl[-e^{-r^2/2}\Bigr]_0^\infty d\theta=\int_0^{2\pi}1\,d\theta=2\pi.$$

3. $I>0$, so $I=\sqrt{2\pi}$.

4. For $N(\mu,\sigma^2)$, substitute $y=(x-\mu)/\sigma$, $dx=\sigma\,dy$: $\int f(x)\,dx=\frac1{\sqrt{2\pi}}\int e^{-y^2/2}\,dy=1$.

:::

::: {#lem-normal-standardize .lemma name="Shifting and scaling"}

If $X\sim N(\mu,\sigma^2)$, then $Y=\dfrac{X-\mu}\sigma\sim N(0,1)$. Equivalently, if $Y\sim N(0,1)$, then $\sigma Y+\mu\sim N(\mu,\sigma^2)$.

:::

::: {.proof}

1. For $a\le b$, the event $a\le Y\le b$ is the event $\sigma a+\mu\le X\le\sigma b+\mu$, since $\sigma>0$.

2. Substitute $x=\sigma y+\mu$, $dx=\sigma\,dy$:
   $$\Pr(a\le Y\le b)=\int_{\sigma a+\mu}^{\sigma b+\mu}\frac{e^{-(x-\mu)^2/(2\sigma^2)}}{\sqrt{2\pi\sigma^2}}\,dx=\int_a^b\frac{e^{-y^2/2}}{\sqrt{2\pi}}\,dy.$$

3. So $Y$ has the standard normal density. The second statement is the same computation read backwards.

:::

So $\Pr(X\le a)=\Pr\bigl(Y\le\frac{a-\mu}\sigma\bigr)$ with $Y$ standard normal: a table of the standard normal c.d.f. serves every normal distribution.

::: {#thm-normal-mean-variance .theorem name="Mean and variance of the normal distribution"}

If $X\sim N(\mu,\sigma^2)$, then $E[X]=\mu$ and $\mathrm{Var}(X)=\sigma^2$.

:::

::: {.proof}

1. *Standard case, mean.* Let $Y\sim N(0,1)$. The function $ye^{-y^2/2}$ is odd and its integral converges, so $E[Y]=\frac1{\sqrt{2\pi}}\int_{-\infty}^\infty ye^{-y^2/2}\,dy=0$.

2. *Standard case, variance.* Integrate by parts with $u=y$, $dv=ye^{-y^2/2}dy$, $v=-e^{-y^2/2}$:
   $$E[Y^2]=\frac1{\sqrt{2\pi}}\int_{-\infty}^\infty y^2e^{-y^2/2}\,dy=\frac1{\sqrt{2\pi}}\Bigl[-ye^{-y^2/2}\Bigr]_{-\infty}^{\infty}+\frac1{\sqrt{2\pi}}\int_{-\infty}^\infty e^{-y^2/2}\,dy=0+1,$$
   by @prp-gaussian-integral. So $\mathrm{Var}(Y)=1-0^2=1$.

3. *General case.* By @lem-normal-standardize, $X=\sigma Y+\mu$ with $Y\sim N(0,1)$. So $E[X]=\sigma E[Y]+\mu=\mu$ and $\mathrm{Var}(X)=\sigma^2\mathrm{Var}(Y)=\sigma^2$.

:::

::: {#fig-normal-distribution-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (7.4,0) node[lab, right] {$x$};
\fill[shade, domain=1.5:5.5, variable=\x] (1.5,0) -- plot ({\x}, {5*exp(-((\x-3.5)^2)/(2*1^2))/(1*sqrt(2*pi))}) -- (5.5,0) -- cycle;
\fill[hl cell, domain=2.5:4.5, variable=\x] (2.5,0) -- plot ({\x}, {5*exp(-((\x-3.5)^2)/(2*1^2))/(1*sqrt(2*pi))}) -- (4.5,0) -- cycle;
\draw[emph, domain=0:7, samples=80, smooth, variable=\x] plot ({\x}, {5*exp(-((\x-3.5)^2)/(2*1^2))/(1*sqrt(2*pi))});
\draw (1.5,0) -- (1.5,-0.08) node[tick, below] {$\mu-2\sigma$};
\draw (2.5,0) -- (2.5,-0.08) node[tick, below] {$\mu-\sigma$};
\draw (3.5,0) -- (3.5,-0.08) node[tick, below] {$\mu$};
\draw (4.5,0) -- (4.5,-0.08) node[tick, below] {$\mu+\sigma$};
\draw (5.5,0) -- (5.5,-0.08) node[tick, below] {$\mu+2\sigma$};
\node[tick] at (3.5,0.6) {$68\%$};
\draw[<->] (1.5,2.25) -- node[tick, above] {$95\%$} (5.5,2.25);
\end{tikzpicture}
\end{center}
```

About $68\%$ of a normal distribution lies within one standard deviation of the mean and about $95\%$ within two

:::

The parameters are the mean and the variance, which explains the notation. About $68\%$ of the probability lies within $\sigma$ of $\mu$, about $95\%$ within $2\sigma$ and $99.7\%$ within $3\sigma$; half of it lies within about $0.67\sigma$.

## Sums of independent normal variables

::: {#thm-sum-of-standard-normals .theorem name="Combination of independent standard normals"}

If $X,Y\sim N(0,1)$ are independent and $a,b$ are constants, not both $0$, then $aX+bY\sim N(0,a^2+b^2)$.

:::

::: {.proof}

1. By @thm-independent-joint-density, $(X,Y)$ has joint density $f(x,y)=\frac1{2\pi}e^{-(x^2+y^2)/2}$. It depends only on the distance $\sqrt{x^2+y^2}$ from the origin, so it is unchanged by any rotation $T$ of the plane about the origin. A rotation preserves area, so $\Pr((X,Y)\in A)=\Pr((X,Y)\in T(A))$ for every region $A$.

2. Fix $t$ and let $c=\sqrt{a^2+b^2}$. Then $\Pr(aX+bY\le t)=\Pr((X,Y)\in A)$ for the half-plane $A=\{(x,y):ax+by\le t\}$.

3. The boundary line $ax+by=t$ has unit normal $(a,b)/c$ and lies at signed distance $t/c$ from the origin. Rotating the vector $(a,b)/c$ onto $(1,0)$ carries $A$ onto the half-plane $\{(x,y):x\le t/c\}$.

4. By step 1, $\Pr(aX+bY\le t)=\Pr(X\le t/c)=\Pr(cX\le t)$. This holds for every $t$, so $aX+bY$ has the same c.d.f., hence the same distribution, as $cX$.

5. By @lem-normal-standardize, $cX\sim N(0,c^2)=N(0,a^2+b^2)$.

:::

::: {#fig-normal-distribution-2}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.9cm,y=0.9cm]
\begin{scope}
\clip (-2.6,-2.6) rectangle (2.6,2.6);
\fill[tintA] (-2.6,3.1) -- (3.1,-2.6) -- (-2.6,-2.6) -- cycle;
\draw[emph, primary] (-2.6,3.1) -- (3.1,-2.6);
\foreach \r in {0.8,1.6,2.4} \draw[faint] (0,0) circle[radius=\r];
\draw[->, muted] (-2.6,0) -- (2.6,0); \draw[->, muted] (0,-2.6) -- (0,2.6);
\draw[<->, accent] (0,0) -- (0.25,0.25);
\end{scope}
\node[tick, accent] at (0.55,0.15) {$d$};
\node[lab, primary] at (1.2,1.6) {$ax+by=t$};
\node[lab] at (-1.3,-1.7) {$A$};
\draw[->, emph, muted] (3,0) -- node[lab, above] {rotate} (4.2,0);
\begin{scope}[xshift=7.2cm]
\clip (-2.6,-2.6) rectangle (2.6,2.6);
\fill[tintA] (-2.6,-2.6) rectangle (0.354,2.6);
\draw[emph, primary] (0.354,-2.6) -- (0.354,2.6);
\foreach \r in {0.8,1.6,2.4} \draw[faint] (0,0) circle[radius=\r];
\draw[->, muted] (-2.6,0) -- (2.6,0); \draw[->, muted] (0,-2.6) -- (0,2.6);
\end{scope}
\node[lab, primary] at (8.9,1.6) {$x=d$};
\node[lab] at (6.0,-1.7) {$T(A)$};
\end{tikzpicture}
\end{center}
```

The joint density of two independent standard normals is constant on circles about the origin, so rotating the half-plane $A=\{ax+by\le t\}$ onto $\{x\le d\}$, $d=t/\sqrt{a^2+b^2}$, does not change its probability.

:::

::: {#cor-sum-of-normals .corollary name="Sums of independent normals"}

If $X\sim N(\mu_X,\sigma_X^2)$ and $Y\sim N(\mu_Y,\sigma_Y^2)$ are independent, and $a,b$ are constants, not both $0$, then
$$aX+bY\sim N\bigl(a\mu_X+b\mu_Y,\ a^2\sigma_X^2+b^2\sigma_Y^2\bigr).$$

:::

::: {.proof}

1. By @lem-normal-standardize, $Z_1=(X-\mu_X)/\sigma_X$ and $Z_2=(Y-\mu_Y)/\sigma_Y$ are standard normal, and they are independent because $X$ and $Y$ are.

2. $aX+bY=(a\mu_X+b\mu_Y)+(a\sigma_XZ_1+b\sigma_YZ_2)$.

3. By @thm-sum-of-standard-normals, $a\sigma_XZ_1+b\sigma_YZ_2\sim N(0,a^2\sigma_X^2+b^2\sigma_Y^2)$; adding the constant $a\mu_X+b\mu_Y$ shifts the mean (@lem-normal-standardize).

:::
