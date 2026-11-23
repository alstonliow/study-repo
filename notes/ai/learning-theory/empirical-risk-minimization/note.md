---
title: "Empirical Risk Minimization and Finite Hypothesis Classes"
sources: [cs229-8]
requires: [ai/machine-learning/bias-variance-tradeoff, math/probability/tail-bounds/chernoff-bounds]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS229 lecture notes (version of 23 August 2026), Chapter 8.3.1-8.3.2 (training and generalization error, empirical risk minimization, uniform convergence for a finite hypothesis class, sample complexity), in our own wording. The union bound and Hoeffding's inequality are used from the probability notes; the numerical example is our own. Proofs written out in steps. -->

How many training examples are enough for the training error to be a trustworthy estimate of the test error? For a finite set of classifiers, two probability tools answer this: Hoeffding's inequality (@thm-hoeffding-inequality) for one classifier, and the union bound (@thm-union-bound) for all of them at once.

::: {#def-erm .definition name="Generalization error, empirical risk minimization"}

Let examples $(\mathbf{x},y)$ with $y\in\{0,1\}$ come from a distribution $\mathcal D$, and let the training set $S$ consist of $N$ independent draws from $\mathcal D$. For a classifier $h$,

$$
\varepsilon(h)=P_{(\mathbf{x},y)\sim\mathcal D}\bigl(h(\mathbf{x})\ne y\bigr),\qquad \hat\varepsilon(h)=\frac1N\sum_{i=1}^N\mathbf 1\{h(\mathbf{x}^{(i)})\ne y^{(i)}\}
$$

are its *generalization error* and its *training error* (empirical risk). Given a hypothesis class $\mathcal H$, *empirical risk minimization* (ERM) returns

$$
\hat h=\operatorname*{arg\,min}_{h\in\mathcal H}\hat\varepsilon(h).
$$

Write $h^\star=\operatorname{arg\,min}_{h\in\mathcal H}\varepsilon(h)$ for the best classifier in the class.

:::

Logistic regression and SVMs can be viewed as convex surrogates of ERM with the zero-one loss, which is hard to minimize directly.

::: {#thm-uniform-convergence-finite .theorem name="Uniform convergence for a finite class"}

Let $\lvert\mathcal H\rvert=k$ and $\gamma>0$. With probability at least $1-2k\,e^{-2\gamma^2N}$ over the training set,

$$
\lvert\varepsilon(h)-\hat\varepsilon(h)\rvert\le\gamma\qquad\text{for every }h\in\mathcal H.
$$

:::

::: {.proof}

1. Fix $h\in\mathcal H$. The indicators $Z_i=\mathbf 1\{h(\mathbf{x}^{(i)})\ne y^{(i)}\}$ are independent, take values in $[0,1]$ and have mean $\varepsilon(h)$, and $\hat\varepsilon(h)=\frac1N\sum_iZ_i$.

2. Hoeffding's inequality (@thm-hoeffding-inequality) with $t=\gamma N$ and $b_i-a_i=1$ gives $P\bigl(\hat\varepsilon(h)-\varepsilon(h)\ge\gamma\bigr)\le e^{-2\gamma^2N}$; applied to $-Z_i$ it gives the same bound for $\varepsilon(h)-\hat\varepsilon(h)\ge\gamma$. So the event $A_h=\{\lvert\varepsilon(h)-\hat\varepsilon(h)\rvert>\gamma\}$ has probability at most $2e^{-2\gamma^2N}$.

3. By the union bound (@thm-union-bound), the probability that some $A_h$ occurs is at most $\sum_{h\in\mathcal H}P(A_h)\le2k\,e^{-2\gamma^2N}$. The complement is the stated event.

:::

::: {#cor-erm-finite .corollary name="ERM with a finite class"}

Let $\lvert\mathcal H\rvert=k$ and $\delta\in(0,1)$.

1. *Sample complexity.* If $N\ge\dfrac1{2\gamma^2}\log\dfrac{2k}\delta$, then with probability at least $1-\delta$ all training errors are within $\gamma$ of the generalization errors.
2. *Error bound.* With probability at least $1-\delta$,

   $$
   \varepsilon(\hat h)\le\varepsilon(h^\star)+2\sqrt{\frac1{2N}\log\frac{2k}\delta}.
   $$

:::

::: {.proof}

1. The condition on $N$ is equivalent to $2k\,e^{-2\gamma^2N}\le\delta$; apply @thm-uniform-convergence-finite.

2. Let $\gamma=\sqrt{\log(2k/\delta)/(2N)}$, so that $2k\,e^{-2\gamma^2N}=\delta$, and assume the uniform-convergence event holds (probability at least $1-\delta$).

3. Then $\varepsilon(\hat h)\le\hat\varepsilon(\hat h)+\gamma$ by uniform convergence, $\hat\varepsilon(\hat h)\le\hat\varepsilon(h^\star)$ because $\hat h$ minimizes the training error, and $\hat\varepsilon(h^\star)\le\varepsilon(h^\star)+\gamma$ by uniform convergence again.

4. Chaining the three inequalities gives $\varepsilon(\hat h)\le\varepsilon(h^\star)+2\gamma$.

:::

::: {#exm-erm-sample-size .example name="How much data for a thousand classifiers"}

For $k=1000$ classifiers, confidence $1-\delta=0.95$ and accuracy $\gamma=0.05$, part 1 of @cor-erm-finite asks for

$$
N\ge\frac1{2\cdot0.05^2}\log\frac{2000}{0.05}=200\log40000\approx2119.3,
$$

so $2120$ examples suffice. Multiplying the class size by $1000$ adds only $200\log1000\approx1382$ examples: the dependence on $k$ is logarithmic.

:::

::: {#rmk-erm-tradeoff .remark name="The tradeoff again"}

In part 2 of @cor-erm-finite, a larger class $\mathcal H$ can only lower $\varepsilon(h^\star)$ (the bias-like term) but raises $\log k$ (the variance-like term), the same tradeoff as in @thm-bias-variance-decomposition. A class described by $d$ real parameters stored as $64$-bit numbers has $k=2^{64d}$ members, so $\log k$ is proportional to $d$ and the number of examples needed grows linearly in the number of parameters; @sec-ai-learning-theory-vc-dimension makes this precise without discretization.

:::
