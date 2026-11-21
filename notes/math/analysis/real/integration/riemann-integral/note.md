---
title: "The Riemann Integral"
sources: [cama1-7]
requires: [math/analysis/real/real-numbers/ordered-fields-and-completeness, math/calculus/single-variable/integrals/definite-integral]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 7.1, in our own wording; proofs written out in steps. @def-riemann-sum defines the integral as a limit of Riemann sums over equal subintervals; here it is defined by upper and lower sums over arbitrary dissections (Darboux's form), and @thm-regular-dissections connects the two. -->

The integral is defined directly, not as an antiderivative: many functions, such as $e^{-x^2}$, have no antiderivative in closed form but should still have an integral. The idea is to trap the area under $f$ between areas of rectangles lying above and below the graph.

## Upper and lower sums

::: {#def-dissection-upper-lower-sums .definition name="Dissection, upper and lower sums"}

A *dissection* of $[a,b]$ is a finite sequence $D: a=x_0<x_1<\cdots<x_n=b$. For a bounded $f:[a,b]\to\mathbb R$ let $M_i=\sup_{[x_{i-1},x_i]}f$ and $m_i=\inf_{[x_{i-1},x_i]}f$. The *upper* and *lower sums* are
$$U_D(f)=\sum_{i=1}^n(x_i-x_{i-1})M_i,\qquad L_D(f)=\sum_{i=1}^n(x_i-x_{i-1})m_i.$$
A dissection $D'$ *refines* $D$ if every point of $D$ is a point of $D'$. The *mesh* of $D$ is $\max_i(x_i-x_{i-1})$.

:::

::: {#fig-riemann-integral-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.6) node[lab, above] {$y$};
\fill[tintB] (0.3,0) rectangle (1.0,1.326); \draw[faint] (0.3,0) rectangle (1.0,1.326);
\fill[shade] (0.3,0) rectangle (1.0,0.821);
\fill[tintB] (1.0,0) rectangle (1.6,1.667); \draw[faint] (1.0,0) rectangle (1.6,1.667);
\fill[shade] (1.0,0) rectangle (1.6,1.326);
\fill[tintB] (1.6,0) rectangle (2.5,1.918); \draw[faint] (1.6,0) rectangle (2.5,1.918);
\fill[shade] (1.6,0) rectangle (2.5,1.667);
\fill[tintB] (2.5,0) rectangle (3.1,1.933); \draw[faint] (2.5,0) rectangle (3.1,1.933);
\fill[shade] (2.5,0) rectangle (3.1,1.918);
\fill[tintB] (3.1,0) rectangle (4.0,1.922); \draw[faint] (3.1,0) rectangle (4.0,1.922);
\fill[shade] (3.1,0) rectangle (4.0,1.827);
\draw[emph] (0.300,0.821) -- (0.346,0.856) -- (0.392,0.890) -- (0.439,0.925) -- (0.485,0.959) -- (0.531,0.994) -- (0.578,1.028) -- (0.624,1.062) -- (0.670,1.096) -- (0.716,1.129) -- (0.762,1.162) -- (0.809,1.195) -- (0.855,1.227) -- (0.901,1.259) -- (0.948,1.291) -- (0.994,1.321) -- (1.040,1.352) -- (1.086,1.382) -- (1.133,1.411) -- (1.179,1.440) -- (1.225,1.467) -- (1.271,1.495) -- (1.318,1.521) -- (1.364,1.547) -- (1.410,1.572) -- (1.456,1.597) -- (1.503,1.620) -- (1.549,1.643) -- (1.595,1.665) -- (1.641,1.686) -- (1.688,1.706) -- (1.734,1.725) -- (1.780,1.744) -- (1.826,1.761) -- (1.873,1.778) -- (1.919,1.794) -- (1.965,1.809) -- (2.011,1.823) -- (2.057,1.836) -- (2.104,1.848) -- (2.150,1.860) -- (2.196,1.870) -- (2.243,1.880) -- (2.289,1.889) -- (2.335,1.897) -- (2.381,1.904) -- (2.428,1.910) -- (2.474,1.916) -- (2.520,1.920) -- (2.566,1.924) -- (2.612,1.927) -- (2.659,1.930) -- (2.705,1.932) -- (2.751,1.933) -- (2.797,1.933) -- (2.844,1.933) -- (2.890,1.932) -- (2.936,1.931) -- (2.982,1.929) -- (3.029,1.926) -- (3.075,1.923) -- (3.121,1.920) -- (3.167,1.916) -- (3.214,1.912) -- (3.260,1.908) -- (3.306,1.903) -- (3.353,1.898) -- (3.399,1.893) -- (3.445,1.888) -- (3.491,1.883) -- (3.537,1.877) -- (3.584,1.872) -- (3.630,1.866) -- (3.676,1.861) -- (3.723,1.855) -- (3.769,1.850) -- (3.815,1.845) -- (3.861,1.840) -- (3.908,1.836) -- (3.954,1.831) -- (4.000,1.827);
\draw[faint] (0.300,-0.06) -- (0.300,0.06); \node[lab, tick, below] at (0.300,-0.05) {$x_0=a$};\draw[faint] (4.000,-0.06) -- (4.000,0.06); \node[lab, tick, below] at (4.000,-0.05) {$x_n=b$};
\end{tikzpicture}
\end{center}
```

Upper and lower sums for a dissection: on each piece, a rectangle up to the supremum of $f$ (outlined) and one up to the infimum (shaded). $L_D(f)\le$ area $\le U_D(f)$.

:::

Clearly $L_D(f)\le U_D(f)$. Refining can only improve both bounds:

::: {#lem-refinement-sums .lemma name="Refinement"}

If $D'$ refines $D$, then $U_{D'}(f)\le U_D(f)$ and $L_{D'}(f)\ge L_D(f)$. Consequently, for any two dissections $D_1,D_2$,
$$L_{D_1}(f)\le U_{D_2}(f).$$

:::

::: {.proof}

1. Suppose $D'$ adds one point $z\in(x_{i-1},x_i)$ to $D$. Only the $i$-th term of the upper sum changes: $(x_i-x_{i-1})M_i$ is replaced by $(z-x_{i-1})\sup_{[x_{i-1},z]}f+(x_i-z)\sup_{[z,x_i]}f$.

2. Both suprema are over subsets of $[x_{i-1},x_i]$, so each is at most $M_i$, and the new term is at most $(z-x_{i-1})M_i+(x_i-z)M_i=(x_i-x_{i-1})M_i$. So $U_{D'}(f)\le U_D(f)$.

3. A general refinement adds finitely many points one at a time, so induction gives the claim. For lower sums the infima can only increase, by the same argument.

4. For $D_1,D_2$, let $D$ consist of the points of both (their *common refinement*). Then $L_{D_1}(f)\le L_D(f)\le U_D(f)\le U_{D_2}(f)$.

:::

::: {#fig-riemann-integral-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.6,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,2.6) node[lab, above] {$y$};
\fill[hl cell] (0.3,0) rectangle (1.0,1.326); \draw[faint] (0.3,0) rectangle (1.0,1.326);
\fill[hl cell] (1.0,0) rectangle (1.6,1.667); \draw[faint] (1.0,0) rectangle (1.6,1.667);
\fill[hl cell] (1.6,0) rectangle (2.5,1.918); \draw[faint] (1.6,0) rectangle (2.5,1.918);
\fill[hl cell] (2.5,0) rectangle (3.1,1.933); \draw[faint] (2.5,0) rectangle (3.1,1.933);
\fill[hl cell] (3.1,0) rectangle (4.0,1.922); \draw[faint] (3.1,0) rectangle (4.0,1.922);
\fill[cell frame] (0.3,0) rectangle (1.0,1.326); \draw[faint] (0.3,0) rectangle (1.0,1.326);
\fill[cell frame] (1.0,0) rectangle (1.6,1.667); \draw[faint] (1.0,0) rectangle (1.6,1.667);
\fill[cell frame] (1.6,0) rectangle (2.05,1.834); \draw[faint] (1.6,0) rectangle (2.05,1.834);
\fill[cell frame] (2.05,0) rectangle (2.5,1.918); \draw[faint] (2.05,0) rectangle (2.5,1.918);
\fill[cell frame] (2.5,0) rectangle (3.1,1.933); \draw[faint] (2.5,0) rectangle (3.1,1.933);
\fill[cell frame] (3.1,0) rectangle (4.0,1.922); \draw[faint] (3.1,0) rectangle (4.0,1.922);
\draw[emph] (0.300,0.821) -- (0.346,0.856) -- (0.392,0.890) -- (0.439,0.925) -- (0.485,0.959) -- (0.531,0.994) -- (0.578,1.028) -- (0.624,1.062) -- (0.670,1.096) -- (0.716,1.129) -- (0.762,1.162) -- (0.809,1.195) -- (0.855,1.227) -- (0.901,1.259) -- (0.948,1.291) -- (0.994,1.321) -- (1.040,1.352) -- (1.086,1.382) -- (1.133,1.411) -- (1.179,1.440) -- (1.225,1.467) -- (1.271,1.495) -- (1.318,1.521) -- (1.364,1.547) -- (1.410,1.572) -- (1.456,1.597) -- (1.503,1.620) -- (1.549,1.643) -- (1.595,1.665) -- (1.641,1.686) -- (1.688,1.706) -- (1.734,1.725) -- (1.780,1.744) -- (1.826,1.761) -- (1.873,1.778) -- (1.919,1.794) -- (1.965,1.809) -- (2.011,1.823) -- (2.057,1.836) -- (2.104,1.848) -- (2.150,1.860) -- (2.196,1.870) -- (2.243,1.880) -- (2.289,1.889) -- (2.335,1.897) -- (2.381,1.904) -- (2.428,1.910) -- (2.474,1.916) -- (2.520,1.920) -- (2.566,1.924) -- (2.612,1.927) -- (2.659,1.930) -- (2.705,1.932) -- (2.751,1.933) -- (2.797,1.933) -- (2.844,1.933) -- (2.890,1.932) -- (2.936,1.931) -- (2.982,1.929) -- (3.029,1.926) -- (3.075,1.923) -- (3.121,1.920) -- (3.167,1.916) -- (3.214,1.912) -- (3.260,1.908) -- (3.306,1.903) -- (3.353,1.898) -- (3.399,1.893) -- (3.445,1.888) -- (3.491,1.883) -- (3.537,1.877) -- (3.584,1.872) -- (3.630,1.866) -- (3.676,1.861) -- (3.723,1.855) -- (3.769,1.850) -- (3.815,1.845) -- (3.861,1.840) -- (3.908,1.836) -- (3.954,1.831) -- (4.000,1.827);
\draw[faint] (2.050,-0.06) -- (2.050,0.06); \node[lab, tick, below] at (2.050,-0.05) {new point};
\end{tikzpicture}
\end{center}
```

Adding a point to the dissection can only lower the upper sum (the orange piece disappears) and raise the lower sum. So every lower sum is below every upper sum.

:::

## The integral

::: {#def-riemann-integral-darboux .definition name="Riemann integral" related="def-riemann-sum"}

Let $f:[a,b]\to\mathbb R$ be bounded. Its *upper* and *lower integrals* are
$$\overline{\int_a^b}f=\inf_DU_D(f),\qquad\underline{\int_a^b}f=\sup_DL_D(f),$$
over all dissections $D$ of $[a,b]$. If they are equal, $f$ is *Riemann integrable* and the common value is $\int_a^bf(x)\,dx$.

:::

By @lem-refinement-sums every lower sum is at most every upper sum, so $\underline\int f\le\overline\int f$ always. An unbounded $f$ is not Riemann integrable: on some subinterval of every dissection it is unbounded, so some $M_i$ or $m_i$ is infinite.

::: {#exm-riemann-integral-1 .example name="Integrating $x$ from the definition"}

Let $f(x)=x$ on $[a,b]$ and $D$ any dissection. On $[x_{i-1},x_i]$ the supremum is $x_i$, and $x_i(x_i-x_{i-1})=\frac12(x_i^2-x_{i-1}^2)+\frac12(x_i-x_{i-1})^2$. Summing, the first parts telescope:
$$U_D(f)=\frac{b^2-a^2}2+\frac12\sum_{i=1}^n(x_i-x_{i-1})^2.$$
If the mesh of $D$ is less than $\delta$, the error is at most $\frac\delta2\sum(x_i-x_{i-1})=\frac\delta2(b-a)$. So $\overline\int f\le\frac{b^2-a^2}2$. In the same way $L_D(f)=\frac{b^2-a^2}2-\frac12\sum(x_i-x_{i-1})^2$ gives $\underline\int f\ge\frac{b^2-a^2}2$. Hence $\int_a^bx\,dx=\frac{b^2-a^2}2$.

:::

::: {#exm-dirichlet-function .example name="A function that is not Riemann integrable"}

Let $f(x)=1$ for rational $x\in[0,1]$ and $f(x)=0$ for irrational $x$. Every interval of positive length contains rationals and irrationals, so $M_i=1$ and $m_i=0$ for every dissection. Then $U_D(f)=1$ and $L_D(f)=0$ always, so the upper integral is $1$, the lower integral is $0$, and $f$ is not Riemann integrable.

The rationals are countable, so in a sense $f$ is $0$ "almost everywhere"; the Lebesgue integral, built on measure theory, assigns it the integral $0$. That integral handles limits far better and is the one used in probability.

:::

::: {#fig-riemann-integral-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->, faint] (-0.2,0) -- (4.8,0) node[lab, right] {$x$};
\draw[->, faint] (0,-0.2) -- (0,1.8) node[lab, above] {$y$};
\node[hl dot] at (0.200,1.200) {};
\node[dot] at (0.410,0.000) {};
\node[dot] at (0.620,0.000) {};
\node[hl dot] at (0.830,1.200) {};
\node[dot] at (1.040,0.000) {};
\node[dot] at (1.250,0.000) {};
\node[hl dot] at (1.460,1.200) {};
\node[dot] at (1.670,0.000) {};
\node[dot] at (1.880,0.000) {};
\node[hl dot] at (2.090,1.200) {};
\node[dot] at (2.300,0.000) {};
\node[dot] at (2.510,0.000) {};
\node[hl dot] at (2.720,1.200) {};
\node[dot] at (2.930,0.000) {};
\node[dot] at (3.140,0.000) {};
\node[hl dot] at (3.350,1.200) {};
\node[dot] at (3.560,0.000) {};
\node[dot] at (3.770,0.000) {};
\node[hl dot] at (3.980,1.200) {};
\node[dot] at (4.190,0.000) {};
\draw[faint, dashed] (0.2,1.2) -- (4.3,1.2); \node[lab, right] at (4.4,1.2) {$1$ on $\mathbb Q$}; \node[lab, right] at (4.4,0.25) {$0$ off $\mathbb Q$};
\end{tikzpicture}
\end{center}
```

A sketch of the Dirichlet function: every piece of every dissection contains rationals (value $1$) and irrationals (value $0$), so $U_D=1$ and $L_D=0$ always, and the integral does not exist.

:::

::: {#thm-riemann-criterion .theorem name="Riemann's criterion"}

A bounded $f:[a,b]\to\mathbb R$ is integrable if and only if for every $\varepsilon>0$ there is a dissection $D$ with
$$U_D(f)-L_D(f)<\varepsilon.$$

:::

::: {.proof}

1. ($\Rightarrow$) Let $I=\int_a^bf$ and $\varepsilon>0$. By the definitions of infimum and supremum there are $D_1,D_2$ with $U_{D_1}(f)<I+\frac\varepsilon2$ and $L_{D_2}(f)>I-\frac\varepsilon2$.

2. For their common refinement $D$, @lem-refinement-sums gives $U_D(f)-L_D(f)\le U_{D_1}(f)-L_{D_2}(f)<\varepsilon$.

3. ($\Leftarrow$) For every $D$, $\underline\int f\ge L_D(f)$ and $\overline\int f\le U_D(f)$, so $0\le\overline\int f-\underline\int f\le U_D(f)-L_D(f)$.

4. If the right side can be made less than any $\varepsilon>0$, the two integrals are equal.

:::

## Equal subintervals suffice

The definition allows all dissections, which makes common refinements easy. For an integrable function, the regular dissections of @def-riemann-sum already give the integral.

::: {#thm-regular-dissections .theorem name="Regular dissections"}

Let $f$ be integrable on $[a,b]$ and let $D_n$ divide $[a,b]$ into $n$ equal parts. Then
$$U_{D_n}(f)\to\int_a^bf\quad\text{and}\quad L_{D_n}(f)\to\int_a^bf.$$
Consequently every Riemann sum $\sum f(c_i)\Delta x$ over $D_n$ also tends to $\int_a^bf$.

:::

::: {.proof}

1. Let $I=\int_a^bf$, $|f|\le C$, and $\varepsilon>0$. Choose a dissection $D$ with $m$ interior points and $U_D(f)<I+\frac\varepsilon2$.

2. Let $D'$ be the common refinement of $D_n$ and $D$, so $U_{D'}(f)\le U_D(f)$. The sums $U_{D_n}(f)$ and $U_{D'}(f)$ differ only on the at most $m$ subintervals of $D_n$ that contain a point of $D$.

3. On such a subinterval, of length $\frac{b-a}n$, both sums contribute a value between $-C\frac{b-a}n$ and $C\frac{b-a}n$, so they differ by at most $2C\frac{b-a}n$. Hence $U_{D_n}(f)\le U_{D'}(f)+2Cm\frac{b-a}n<I+\frac\varepsilon2+2Cm\frac{b-a}n$.

4. For $n>4Cm(b-a)/\varepsilon$ this gives $I\le U_{D_n}(f)<I+\varepsilon$. So $U_{D_n}(f)\to I$; lower sums are similar.

5. A Riemann sum over $D_n$ lies between $L_{D_n}(f)$ and $U_{D_n}(f)$, so it tends to $I$ by the sandwich rule.

:::
