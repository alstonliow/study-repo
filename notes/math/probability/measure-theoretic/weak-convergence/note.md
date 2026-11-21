---
title: "Characteristic Functions and Weak Convergence"
sources: [camii-pm-5]
requires: [math/analysis/measure-theory/fourier-inversion, math/probability/measure-theoretic/distribution-functions]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Sections 5.5 and 5.6, in our own wording. The source only sketches these proofs (non-examinable); the full proofs here, by Gaussian smoothing and Scheffé's lemma, are our own write-up. Lévy's theorem with a limit that is only continuous at 0 is stated without proof. -->

Throughout, $X,X_n$ are random variables in $\mathbb R^d$ with laws $\mu_X,\mu_{X_n}$ and characteristic functions $\varphi_X(u)=E[e^{i\langle u,X\rangle}]$ (@def-fourier-transform), and $Z$ is a standard Gaussian vector independent of everything else, so $\sqrt tZ$ has density $g_t$ (@def-gaussian-heat-kernel).

::: {#lem-smoothed-density .lemma name="Gaussian smoothing has an explicit density"}

For $t>0$, $X+\sqrt tZ$ has the bounded continuous density

$$
f_t(x)=(2\pi)^{-d}\int_{\mathbb R^d}\varphi_X(u)\,e^{-t|u|^2/2}\,e^{-i\langle u,x\rangle}\,du .
$$

:::

::: {.proof}

1. By Fubini, for Borel $A$, $\Pr(X+\sqrt tZ\in A)=\int\!\int\mathbf 1_A(y+z)g_t(z)\,dz\,\mu_X(dy)=\int_A\Big(\int g_t(x-y)\,\mu_X(dy)\Big)dx$. So $X+\sqrt tZ$ has density $x\mapsto\int g_t(x-y)\,\mu_X(dy)$.

2. Insert $g_t(x-y)=(2\pi)^{-d}\int e^{-t|u|^2/2}e^{-i\langle u,x-y\rangle}du$ (@cor-gaussian-inversion) and exchange the integrals (the integrand is bounded by $e^{-t|u|^2/2}$, integrable for $du\,\mu_X(dy)$). The $y$-integral is $\int e^{i\langle u,y\rangle}\mu_X(dy)=\varphi_X(u)$.

3. Boundedness and continuity follow from @prp-fourier-bounded-continuous, since $\varphi_Xe^{-t|u|^2/2}$ is integrable.

:::

::: {#fig-weak-convergence-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (-2.6,0) -- (3.4,0) node[lab, right] {$x$};
\draw[->] (0,-0.1) -- (0,2.6) node[lab, above] {};
\draw[emph, ->] (-1,0) -- (-1,1.2);
\draw[emph, ->] (1,0) -- (1,2.4);
\node[tick] at (-1,1.4) {$\frac13$};
\node[tick] at (1.25,2.4) {$\frac23$};
\draw[hl] (-2.500,0.000) -- (-2.450,0.000) -- (-2.400,0.000) -- (-2.350,0.000) -- (-2.300,0.000) -- (-2.250,0.000) -- (-2.200,0.000) -- (-2.150,0.000) -- (-2.100,0.000) -- (-2.050,0.001) -- (-2.000,0.001) -- (-1.950,0.002) -- (-1.900,0.003) -- (-1.850,0.006) -- (-1.800,0.009) -- (-1.750,0.015) -- (-1.700,0.024) -- (-1.650,0.037) -- (-1.600,0.055) -- (-1.550,0.078) -- (-1.500,0.108) -- (-1.450,0.146) -- (-1.400,0.190) -- (-1.350,0.241) -- (-1.300,0.295) -- (-1.250,0.350) -- (-1.200,0.403) -- (-1.150,0.449) -- (-1.100,0.486) -- (-1.050,0.509) -- (-1.000,0.517) -- (-0.950,0.509) -- (-0.900,0.486) -- (-0.850,0.449) -- (-0.800,0.403) -- (-0.750,0.350) -- (-0.700,0.295) -- (-0.650,0.241) -- (-0.600,0.190) -- (-0.550,0.146) -- (-0.500,0.108) -- (-0.450,0.078) -- (-0.400,0.055) -- (-0.350,0.037) -- (-0.300,0.024) -- (-0.250,0.015) -- (-0.200,0.010) -- (-0.150,0.006) -- (-0.100,0.004) -- (-0.050,0.003) -- (0.000,0.003) -- (0.050,0.004) -- (0.100,0.007) -- (0.150,0.011) -- (0.200,0.019) -- (0.250,0.031) -- (0.300,0.048) -- (0.350,0.074) -- (0.400,0.109) -- (0.450,0.156) -- (0.500,0.217) -- (0.550,0.292) -- (0.600,0.381) -- (0.650,0.481) -- (0.700,0.589) -- (0.750,0.700) -- (0.800,0.806) -- (0.850,0.899) -- (0.900,0.972) -- (0.950,1.018) -- (1.000,1.034) -- (1.050,1.018) -- (1.100,0.972) -- (1.150,0.899) -- (1.200,0.806) -- (1.250,0.700) -- (1.300,0.589) -- (1.350,0.481) -- (1.400,0.381) -- (1.450,0.292) -- (1.500,0.217) -- (1.550,0.156) -- (1.600,0.109) -- (1.650,0.074) -- (1.700,0.048) -- (1.750,0.031) -- (1.800,0.019) -- (1.850,0.011) -- (1.900,0.007) -- (1.950,0.004) -- (2.000,0.002) -- (2.050,0.001) -- (2.100,0.001) -- (2.150,0.000) -- (2.200,0.000) -- (2.250,0.000) -- (2.300,0.000) -- (2.350,0.000) -- (2.400,0.000) -- (2.450,0.000) -- (2.500,0.000) -- (2.550,0.000) -- (2.600,0.000) -- (2.650,0.000) -- (2.700,0.000) -- (2.750,0.000) -- (2.800,0.000) -- (2.850,0.000) -- (2.900,0.000) -- (2.950,0.000) -- (3.000,0.000);
\draw[faint] (-2.500,0.022) -- (-2.450,0.025) -- (-2.400,0.029) -- (-2.350,0.033) -- (-2.300,0.038) -- (-2.250,0.043) -- (-2.200,0.049) -- (-2.150,0.055) -- (-2.100,0.062) -- (-2.050,0.069) -- (-2.000,0.076) -- (-1.950,0.084) -- (-1.900,0.092) -- (-1.850,0.101) -- (-1.800,0.109) -- (-1.750,0.118) -- (-1.700,0.127) -- (-1.650,0.136) -- (-1.600,0.145) -- (-1.550,0.153) -- (-1.500,0.162) -- (-1.450,0.170) -- (-1.400,0.178) -- (-1.350,0.185) -- (-1.300,0.191) -- (-1.250,0.197) -- (-1.200,0.202) -- (-1.150,0.206) -- (-1.100,0.210) -- (-1.050,0.213) -- (-1.000,0.214) -- (-0.950,0.216) -- (-0.900,0.216) -- (-0.850,0.216) -- (-0.800,0.215) -- (-0.750,0.214) -- (-0.700,0.212) -- (-0.650,0.210) -- (-0.600,0.208) -- (-0.550,0.206) -- (-0.500,0.205) -- (-0.450,0.203) -- (-0.400,0.203) -- (-0.350,0.202) -- (-0.300,0.203) -- (-0.250,0.205) -- (-0.200,0.207) -- (-0.150,0.211) -- (-0.100,0.215) -- (-0.050,0.221) -- (0.000,0.228) -- (0.050,0.236) -- (0.100,0.246) -- (0.150,0.256) -- (0.200,0.267) -- (0.250,0.279) -- (0.300,0.292) -- (0.350,0.305) -- (0.400,0.318) -- (0.450,0.331) -- (0.500,0.344) -- (0.550,0.357) -- (0.600,0.369) -- (0.650,0.380) -- (0.700,0.390) -- (0.750,0.398) -- (0.800,0.406) -- (0.850,0.411) -- (0.900,0.415) -- (0.950,0.417) -- (1.000,0.418) -- (1.050,0.416) -- (1.100,0.412) -- (1.150,0.407) -- (1.200,0.399) -- (1.250,0.390) -- (1.300,0.379) -- (1.350,0.367) -- (1.400,0.353) -- (1.450,0.338) -- (1.500,0.323) -- (1.550,0.306) -- (1.600,0.289) -- (1.650,0.271) -- (1.700,0.254) -- (1.750,0.236) -- (1.800,0.218) -- (1.850,0.201) -- (1.900,0.184) -- (1.950,0.168) -- (2.000,0.152) -- (2.050,0.137) -- (2.100,0.123) -- (2.150,0.110) -- (2.200,0.098) -- (2.250,0.087) -- (2.300,0.076) -- (2.350,0.067) -- (2.400,0.058) -- (2.450,0.051) -- (2.500,0.044) -- (2.550,0.037) -- (2.600,0.032) -- (2.650,0.027) -- (2.700,0.023) -- (2.750,0.019) -- (2.800,0.016) -- (2.850,0.014) -- (2.900,0.011) -- (2.950,0.009) -- (3.000,0.008);
\end{tikzpicture}
\end{center}
```

Adding an independent $\sqrt tZ$ to a two-point variable gives a smooth density, computable from the characteristic function by @lem-smoothed-density ($t=0.5$ grey, $t=0.08$ red). Letting $t\to0$ recovers the law, which is why the characteristic function determines it.

:::

::: {#thm-characteristic-function-uniqueness .theorem name="The characteristic function determines the law"}

If $\varphi_X=\varphi_Y$ then $\mu_X=\mu_Y$. If moreover $\varphi_X$ is integrable, then $X$ has the bounded continuous density

$$
f_X(x)=(2\pi)^{-d}\int_{\mathbb R^d}\varphi_X(u)\,e^{-i\langle u,x\rangle}\,du .
$$

:::

::: {.proof}

1. By @lem-smoothed-density, $X+\sqrt tZ$ and $Y+\sqrt tZ$ have the same density, hence the same law, for every $t>0$.

2. Let $g$ be bounded and continuous. As $t\to0$, $g(X+\sqrt tZ)\to g(X)$ pointwise, so $E[g(X)]=\lim_tE[g(X+\sqrt tZ)]$ by bounded convergence. The same holds for $Y$, so $E[g(X)]=E[g(Y)]$.

3. For a box $B=\prod_j(a_j,b_j]$ let $h_{j,k}:\mathbb R\to[0,1]$ be continuous, equal to $1$ on $[a_j+\frac1k,b_j]$, $0$ outside $(a_j,b_j+\frac1k)$ and linear in between. As $k\to\infty$, $h_{j,k}\to\mathbf 1_{(a_j,b_j]}$ pointwise, so $g_k(x)=\prod_jh_{j,k}(x_j)\to\mathbf 1_B(x)$. By step 2 and bounded convergence $\mu_X(B)=\mu_Y(B)$. Boxes with $\emptyset$ form a generating π-system, so $\mu_X=\mu_Y$ (@thm-uniqueness-of-extension).

4. If $\varphi_X$ is integrable, $f_t\to f_X$ uniformly as $t\to0$, by dominated convergence with dominating function $|\varphi_X|$. For continuous $g$ of compact support, $E[g(X)]=\lim_t\int gf_t=\int gf_X$. As in step 3 this identifies $\mu_X$ with the measure of density $f_X$ (which is non-negative, being a limit of densities).

:::

::: {#def-weak-convergence .definition name="Weak convergence"}

Borel probability measures $\mu_n$ *converge weakly* to $\mu$ if $\mu_n(g)\to\mu(g)$ for every bounded continuous $g:\mathbb R^d\to\mathbb R$. Random variables $X_n\to X$ *weakly* if their laws do, i.e. $E[g(X_n)]\to E[g(X)]$ for all bounded continuous $g$.

:::

For real random variables, weak convergence is the same as convergence in distribution (@def-convergence-in-distribution); one direction is the remark after @thm-skorokhod-representation.

::: {#lem-scheffe .lemma name="Scheffé's lemma"}

If $f_n,f$ are probability densities with $f_n\to f$ almost everywhere, then $\|f_n-f\|_1\to0$.

:::

::: {.proof}

1. $(f-f_n)^+\le f$ and $(f-f_n)^+\to0$ a.e., so $\int(f-f_n)^+\to0$ by dominated convergence.

2. $\int(f-f_n)=0$, so $\int(f-f_n)^-=\int(f-f_n)^+$ and $\|f-f_n\|_1=2\int(f-f_n)^+\to0$.

:::

::: {#thm-levy-continuity .theorem name="Lévy's continuity theorem"}

$X_n\to X$ weakly if and only if $\varphi_{X_n}(u)\to\varphi_X(u)$ for every $u\in\mathbb R^d$.

:::

::: {.proof}

1. *(⇒)* $x\mapsto\cos\langle u,x\rangle$ and $\sin\langle u,x\rangle$ are bounded and continuous.

2. *(⇐), smoothed.* Fix $t>0$. By @lem-smoothed-density, $X_n+\sqrt tZ$ and $X+\sqrt tZ$ have densities $f_{n,t},f_t$, and $f_{n,t}(x)\to f_t(x)$ for every $x$ by dominated convergence ($|\varphi_{X_n}|\le1$, dominating function $e^{-t|u|^2/2}$). By Scheffé, $\|f_{n,t}-f_t\|_1\to0$, so $\big|E[g(X_n+\sqrt tZ)]-E[g(X+\sqrt tZ)]\big|\le\|g\|_\infty\|f_{n,t}-f_t\|_1\to0$ for every bounded measurable $g$.

3. *Removing the smoothing for $g$ continuous of compact support.* Such $g$ is uniformly continuous; let $\omega(r)=\sup_{|x-y|\le r}|g(x)-g(y)|$, bounded by $2\|g\|_\infty$ and tending to $0$ as $r\to0$. Then $\big|E[g(X_n+\sqrt tZ)]-E[g(X_n)]\big|\le E[\omega(\sqrt t|Z|)]$, which does not depend on $n$ and tends to $0$ as $t\to0$ by bounded convergence. The same bound holds for $X$. With step 2, $E[g(X_n)]\to E[g(X)]$.

4. *Tightness.* Given $\varepsilon>0$ choose $R$ with $\Pr(|X|>R)\le\varepsilon$ and a continuous $\chi$ with $\mathbf 1_{\{|x|\le R\}}\le\chi\le\mathbf 1_{\{|x|\le R+1\}}$. By step 3, $E[\chi(X_n)]\to E[\chi(X)]\ge1-\varepsilon$, so $E[1-\chi(X_n)]\le2\varepsilon$ for large $n$.

5. *All bounded continuous $g$.* Write $g=g\chi+g(1-\chi)$. The first part has compact support, so step 3 applies; the second satisfies $|E[g(1-\chi)(X_n)]|\le\|g\|_\infty E[1-\chi(X_n)]\le2\varepsilon\|g\|_\infty$ for large $n$, and likewise for $X$. So $\limsup_n|E[g(X_n)]-E[g(X)]|\le4\varepsilon\|g\|_\infty$.

:::

::: {#rmk-levy-continuity-full .remark name="The full continuity theorem"}

Lévy's theorem has a stronger form: if $\varphi_{X_n}(u)$ converges for every $u$ to a function $\psi$ that is continuous at $0$, then $\psi$ is the characteristic function of some $X$ and $X_n\to X$ weakly. The extra step is to show tightness from continuity of $\psi$ at $0$; we do not prove it. The proof above shows, along the way, that it suffices to test weak convergence on continuous functions of compact support once tightness is known.

:::

## Gaussian vectors

::: {#prp-gaussian-vector-characteristic-function .proposition name="Gaussian vectors through characteristic functions" related="thm-jointly-gaussian-properties"}

Let $X$ be a random vector in $\mathbb R^n$ such that $\langle u,X\rangle$ is normal for every $u$ (@def-jointly-gaussian), with mean $\mu=E[X]$ and covariance matrix $V$. Then

$$
\varphi_X(u)=\exp\Big(i\langle u,\mu\rangle-\tfrac12\langle u,Vu\rangle\Big),
$$

so the law of $X$ is determined by $\mu$ and $V$. If $X=(X^{(1)},X^{(2)})$ and every entry of $X^{(1)}$ is uncorrelated with every entry of $X^{(2)}$, then $X^{(1)}$ and $X^{(2)}$ are independent.

:::

::: {.proof}

1. $X\in L^2$: each coordinate $\langle e_j,X\rangle$ is normal. $\langle u,X\rangle$ is normal with mean $\langle u,\mu\rangle$ and variance $\operatorname{Var}\langle u,X\rangle=\langle u,Vu\rangle$ by bilinearity of covariance.

2. A normal variable $Y\sim N(m,s^2)$ has $E[e^{iY}]=e^{im-s^2/2}$, by @prp-gaussian-fourier after scaling and shifting. Take $Y=\langle u,X\rangle$: $\varphi_X(u)=E[e^{i\langle u,X\rangle}]$ is as stated. @thm-characteristic-function-uniqueness gives the uniqueness.

3. Uncorrelated blocks make $V$ block diagonal, so $\varphi_X(u_1,u_2)=\varphi_{X^{(1)}}(u_1)\varphi_{X^{(2)}}(u_2)$. The right side is the characteristic function of the product measure $\mu_{X^{(1)}}\otimes\mu_{X^{(2)}}$ (Fubini). By uniqueness, $\mu_X$ is this product, which is independence (@prp-independence-product-law).

:::
