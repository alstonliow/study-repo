---
title: "The Strong Law of Large Numbers"
sources: [camii-pm-7]
requires: [math/probability/measure-theoretic/ergodic-theorems]
status: draft
---

<!-- Added 2026-11-21 from Cambridge Part II Probability and Measure (Michaelmas 2016 lecture notes), Section 7.1, in our own wording; proofs written out in steps. The weak law (math/probability/tail-bounds/concentration-inequalities) gives convergence in probability; here the convergence is almost sure. -->

Let $Y_1,Y_2,\dots$ be random variables and $S_n=Y_1+\dots+Y_n$. The weak law (@thm-law-of-large-numbers) says $S_n/n\to\mu$ in probability. The strong law says this happens for almost every outcome. We give two proofs: a short one under a fourth-moment assumption, and the general one from Birkhoff's theorem.

::: {#thm-slln-fourth-moment .theorem name="Strong law with bounded fourth moments"}

Let $Y_1,Y_2,\dots$ be independent with $E[Y_n]=\mu$ and $E[Y_n^4]\le M$ for all $n$. Then $S_n/n\to\mu$ almost surely.

:::

::: {.proof}

1. Replacing $Y_n$ by $X_n=Y_n-\mu$, we may assume $\mu=0$; the fourth moments stay bounded, since $(a-\mu)^4\le8(a^4+\mu^4)$, and $\mu^4=(E[Y_n])^4\le E[Y_n^4]$ by Jensen. Call the bound $M$ again.

2. Expand $S_n^4=\sum_{i,j,k,l}X_iX_jX_kX_l$. By independence and $E[X_i]=0$, every term in which some index appears exactly once has expectation $0$. What remains:
$$E[S_n^4]=\sum_iE[X_i^4]+6\sum_{i<j}E[X_i^2]E[X_j^2].$$

3. By Cauchy–Schwarz, $E[X_i^2]E[X_j^2]\le\sqrt{E[X_i^4]E[X_j^4]}\le M$. So $E[S_n^4]\le nM+3n(n-1)M\le3n^2M$.

4. Hence $E\big[\sum_n(S_n/n)^4\big]=\sum_nE[S_n^4]/n^4\le3M\sum_nn^{-2}<\infty$ by monotone convergence (@cor-series-nonnegative-integral).

5. A non-negative random variable with finite expectation is finite a.s., so $\sum_n(S_n/n)^4<\infty$ a.s., and therefore $(S_n/n)^4\to0$ a.s.

:::

::: {#thm-strong-law-of-large-numbers .theorem name="Strong law of large numbers"}

Let $Y_1,Y_2,\dots$ be i.i.d. and integrable with $E[Y_1]=\mu$. Then

$$
\frac{S_n}{n}\to\mu\qquad\text{almost surely and in }L^1 .
$$

:::

::: {.proof}

1. The statement concerns only the law of the sequence $(Y_n)$, so we may work on the Bernoulli shift space $E=\mathbb R^{\mathbb N}$ with the law $\mu_Y$ of the sequence (@prp-bernoulli-shift-ergodic): almost sure and $L^1$ convergence of $S_n/n=S_n(f)/n$ for $f(x)=x_1$ there are statements about $\mu_Y$.

2. With the shift $\Theta$, $f\circ\Theta^{k}(x)=x_{k+1}$, so $S_n(f)=x_1+\dots+x_n$. $f$ is integrable, $\Theta$ is measure-preserving and ergodic.

3. By Birkhoff's theorem (@thm-birkhoff-ergodic), $S_n(f)/n\to\bar f$ a.e., with $\bar f$ a.e. equal to a constant $c$.

4. By von Neumann's theorem (@thm-von-neumann-ergodic) with $p=1$, the convergence also holds in $L^1$. So $E[S_n/n]\to c$. But $E[S_n/n]=\mu$ for all $n$; hence $c=\mu$.

:::

::: {#fig-strong-law-of-large-numbers-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[->] (0,0) -- (7.3,0) node[lab, right] {$n$};
\draw[->] (0,0) -- (0,2.9);
\draw[faint, dashed] (0,1.3) -- (7.0,1.3);
\node[tick, left] at (0,1.3) {$\frac12$};
\node[tick, left] at (0,2.6) {$1$};
\node[tick, left] at (0,0) {$0$};
\draw[hl] (0.000,2.600) -- (0.702,1.300) -- (1.113,0.867) -- (1.405,0.650) -- (1.631,1.040) -- (1.816,1.300) -- (1.972,1.114) -- (2.107,0.975) -- (2.227,0.867) -- (2.333,0.780) -- (2.430,0.709) -- (2.518,0.650) -- (2.599,0.600) -- (2.674,0.557) -- (2.744,0.693) -- (2.810,0.650) -- (2.871,0.765) -- (2.929,0.722) -- (2.984,0.821) -- (3.036,0.780) -- (3.447,0.780) -- (3.738,0.910) -- (3.964,0.988) -- (4.149,1.127) -- (4.305,1.189) -- (4.441,1.105) -- (4.560,1.156) -- (4.667,1.118) -- (4.763,1.111) -- (4.851,1.170) -- (4.933,1.160) -- (5.008,1.133) -- (5.078,1.109) -- (5.143,1.154) -- (5.204,1.178) -- (5.262,1.184) -- (5.317,1.163) -- (5.369,1.222) -- (5.419,1.226) -- (5.466,1.205) -- (5.511,1.198) -- (5.554,1.203) -- (5.595,1.217) -- (5.635,1.230) -- (5.673,1.213) -- (5.710,1.207) -- (5.746,1.201) -- (5.780,1.205) -- (5.813,1.216) -- (5.845,1.243) -- (5.877,1.221) -- (5.907,1.208) -- (5.936,1.211) -- (5.965,1.192) -- (5.992,1.195) -- (6.019,1.177) -- (6.046,1.187) -- (6.071,1.190) -- (6.096,1.180) -- (6.121,1.195) -- (6.145,1.185) -- (6.168,1.194) -- (6.191,1.196) -- (6.213,1.198) -- (6.235,1.200) -- (6.256,1.208) -- (6.277,1.199) -- (6.298,1.206) -- (6.318,1.224) -- (6.337,1.235) -- (6.357,1.236) -- (6.376,1.228) -- (6.394,1.239) -- (6.412,1.244) -- (6.430,1.250) -- (6.448,1.255) -- (6.465,1.247) -- (6.482,1.239) -- (6.499,1.240) -- (6.516,1.254) -- (6.532,1.263) -- (6.548,1.263) -- (6.563,1.268) -- (6.579,1.261) -- (6.594,1.261) -- (6.609,1.254) -- (6.624,1.247) -- (6.639,1.252) -- (6.653,1.252) -- (6.667,1.257) -- (6.681,1.254) -- (6.695,1.251) -- (6.708,1.262) -- (6.722,1.266) -- (6.735,1.276) -- (6.748,1.270) -- (6.761,1.257) -- (6.774,1.258) -- (6.786,1.255) -- (6.799,1.262) -- (6.811,1.266) -- (6.823,1.266) -- (6.835,1.263) -- (6.847,1.264) -- (6.859,1.258) -- (6.870,1.268) -- (6.882,1.271) -- (6.893,1.277) -- (6.904,1.274) -- (6.916,1.272) -- (6.926,1.278) -- (6.937,1.281) -- (6.948,1.278) -- (6.959,1.273) -- (6.969,1.281) -- (6.980,1.281) -- (6.990,1.284) -- (7.000,1.287);
\draw[emph] (0.000,2.600) -- (0.702,1.300) -- (1.113,1.733) -- (1.405,1.300) -- (1.631,1.560) -- (1.816,1.300) -- (1.972,1.486) -- (2.107,1.625) -- (2.227,1.733) -- (2.333,1.560) -- (2.430,1.418) -- (2.518,1.517) -- (2.599,1.600) -- (2.674,1.671) -- (2.744,1.560) -- (2.810,1.463) -- (2.871,1.529) -- (2.929,1.589) -- (2.984,1.642) -- (3.036,1.560) -- (3.447,1.300) -- (3.738,1.235) -- (3.964,1.196) -- (4.149,1.213) -- (4.305,1.263) -- (4.441,1.300) -- (4.560,1.329) -- (4.667,1.326) -- (4.763,1.324) -- (4.851,1.300) -- (4.933,1.280) -- (5.008,1.281) -- (5.078,1.283) -- (5.143,1.316) -- (5.204,1.346) -- (5.262,1.343) -- (5.317,1.314) -- (5.369,1.287) -- (5.419,1.288) -- (5.466,1.276) -- (5.511,1.255) -- (5.554,1.235) -- (5.595,1.206) -- (5.635,1.220) -- (5.673,1.223) -- (5.710,1.244) -- (5.746,1.246) -- (5.780,1.257) -- (5.813,1.275) -- (5.845,1.259) -- (5.877,1.276) -- (5.907,1.269) -- (5.936,1.263) -- (5.965,1.278) -- (5.992,1.286) -- (6.019,1.286) -- (6.046,1.300) -- (6.071,1.320) -- (6.096,1.313) -- (6.121,1.312) -- (6.145,1.318) -- (6.168,1.300) -- (6.191,1.306) -- (6.213,1.300) -- (6.235,1.294) -- (6.256,1.289) -- (6.277,1.289) -- (6.298,1.290) -- (6.318,1.295) -- (6.337,1.290) -- (6.357,1.305) -- (6.376,1.314) -- (6.394,1.319) -- (6.412,1.314) -- (6.430,1.314) -- (6.448,1.327) -- (6.465,1.322) -- (6.482,1.322) -- (6.499,1.321) -- (6.516,1.325) -- (6.532,1.321) -- (6.548,1.324) -- (6.563,1.332) -- (6.579,1.339) -- (6.594,1.343) -- (6.609,1.338) -- (6.624,1.338) -- (6.639,1.337) -- (6.653,1.337) -- (6.667,1.336) -- (6.681,1.343) -- (6.695,1.353) -- (6.708,1.352) -- (6.722,1.362) -- (6.735,1.364) -- (6.748,1.363) -- (6.761,1.372) -- (6.774,1.375) -- (6.786,1.374) -- (6.799,1.370) -- (6.811,1.360) -- (6.823,1.353) -- (6.835,1.355) -- (6.847,1.348) -- (6.859,1.342) -- (6.870,1.347) -- (6.882,1.347) -- (6.893,1.349) -- (6.904,1.349) -- (6.916,1.351) -- (6.926,1.353) -- (6.937,1.350) -- (6.948,1.349) -- (6.959,1.346) -- (6.969,1.354) -- (6.980,1.350) -- (6.990,1.353) -- (7.000,1.349);
\draw[faint] (0.000,2.600) -- (0.702,2.600) -- (1.113,2.600) -- (1.405,1.950) -- (1.631,2.080) -- (1.816,1.733) -- (1.972,1.486) -- (2.107,1.300) -- (2.227,1.156) -- (2.333,1.040) -- (2.430,0.945) -- (2.518,0.867) -- (2.599,1.000) -- (2.674,1.114) -- (2.744,1.040) -- (2.810,1.137) -- (2.871,1.224) -- (2.929,1.300) -- (2.984,1.232) -- (3.036,1.300) -- (3.447,1.387) -- (3.738,1.560) -- (3.964,1.612) -- (4.149,1.517) -- (4.305,1.560) -- (4.441,1.560) -- (4.560,1.560) -- (4.667,1.534) -- (4.763,1.442) -- (4.851,1.430) -- (4.933,1.420) -- (5.008,1.356) -- (5.078,1.352) -- (5.143,1.349) -- (5.204,1.361) -- (5.262,1.372) -- (5.317,1.368) -- (5.369,1.404) -- (5.419,1.374) -- (5.466,1.359) -- (5.511,1.379) -- (5.554,1.376) -- (5.595,1.373) -- (5.635,1.420) -- (5.673,1.425) -- (5.710,1.430) -- (5.746,1.399) -- (5.780,1.404) -- (5.813,1.409) -- (5.845,1.414) -- (5.877,1.418) -- (5.907,1.430) -- (5.936,1.411) -- (5.965,1.423) -- (5.992,1.434) -- (6.019,1.423) -- (6.046,1.407) -- (6.071,1.417) -- (6.096,1.414) -- (6.121,1.405) -- (6.145,1.397) -- (6.168,1.400) -- (6.191,1.381) -- (6.213,1.390) -- (6.235,1.383) -- (6.256,1.376) -- (6.277,1.369) -- (6.298,1.362) -- (6.318,1.376) -- (6.337,1.375) -- (6.357,1.388) -- (6.376,1.382) -- (6.394,1.385) -- (6.412,1.388) -- (6.430,1.382) -- (6.448,1.385) -- (6.465,1.393) -- (6.482,1.400) -- (6.499,1.402) -- (6.516,1.396) -- (6.532,1.387) -- (6.548,1.385) -- (6.563,1.384) -- (6.579,1.371) -- (6.594,1.370) -- (6.609,1.376) -- (6.624,1.368) -- (6.639,1.371) -- (6.653,1.362) -- (6.667,1.361) -- (6.681,1.361) -- (6.695,1.370) -- (6.708,1.387) -- (6.722,1.389) -- (6.735,1.388) -- (6.748,1.387) -- (6.761,1.392) -- (6.774,1.404) -- (6.786,1.403) -- (6.799,1.405) -- (6.811,1.400) -- (6.823,1.405) -- (6.835,1.410) -- (6.847,1.415) -- (6.859,1.408) -- (6.870,1.412) -- (6.882,1.420) -- (6.893,1.421) -- (6.904,1.426) -- (6.916,1.427) -- (6.926,1.426) -- (6.937,1.422) -- (6.948,1.412) -- (6.959,1.414) -- (6.969,1.423) -- (6.980,1.411) -- (6.990,1.410) -- (7.000,1.412);
\node[tick, below] at (0.00,0) {$10^0$};
\node[tick, below] at (2.33,0) {$10^1$};
\node[tick, below] at (4.67,0) {$10^2$};
\node[tick, below] at (7.00,0) {$10^3$};
\end{tikzpicture}
\end{center}
```

Three simulated paths of the running proportion of heads $S_n/n$ for a fair coin, $n$ up to $1000$ on a logarithmic axis. Almost every path converges to $\frac12$.

:::

::: {#rmk-strong-law-of-large-numbers-1 .remark name="Integrability is necessary"}

If the $Y_n$ are i.i.d. with $E|Y_1|=\infty$, then $\limsup_n|S_n|/n=\infty$ almost surely, so $S_n/n$ converges with probability $0$. (This uses $\sum_n\Pr(|Y_1|\ge an)=\infty$ for every $a>0$ and the second Borel–Cantelli lemma; see the exercises.) So for i.i.d. sequences, almost-sure convergence of $S_n/n$ to a finite limit happens exactly when $Y_1$ is integrable.

:::

::: {#exm-normal-numbers .example name="Normal numbers"}

Let $\omega\in[0,1)$ be chosen uniformly and let $R_k(\omega)$ be its $k$-th binary digit. The $R_k$ are i.i.d. fair bits (@thm-iid-sequence-exists), so by the strong law

$$
\frac{R_1(\omega)+\dots+R_n(\omega)}{n}\to\frac12\qquad\text{for Lebesgue-almost every }\omega .
$$

Almost every number has asymptotically equal frequencies of $0$s and $1$s in its binary expansion. The exceptional null set is not empty: $\frac17=0.001001\ldots_2$ has digit frequency $\frac13$.

:::
