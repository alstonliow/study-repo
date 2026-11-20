---
title: "Properties of the Riemann Integral"
sources: [cama1-7]
requires: [math/analysis/real/integration/riemann-integral]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IA Analysis I (Lent 2015 lecture notes), Section 7.1, in our own wording; proofs written out in steps. @prp-integral-properties states linearity, additivity and monotonicity for the Riemann-sum integral; here they are proved for the integral of @def-riemann-integral-darboux, together with integrability of $|f|$ and of products. -->

All functions here are bounded on $[a,b]$, and "integrable" means Riemann integrable. On a subinterval $[x_{i-1},x_i]$ of a dissection, write $M_i(f),m_i(f)$ for the supremum and infimum of $f$.

::: {#thm-integral-linear .theorem name="Linearity" related="prp-integral-properties"}

If $f,g$ are integrable on $[a,b]$ and $\lambda,\mu\in\mathbb R$, then $\lambda f+\mu g$ is integrable and
$$\int_a^b(\lambda f+\mu g)=\lambda\int_a^bf+\mu\int_a^bg.$$

:::

::: {.proof}

1. *Scaling by $\lambda\ge0$.* $M_i(\lambda f)=\lambda M_i(f)$ and $m_i(\lambda f)=\lambda m_i(f)$, so $U_D(\lambda f)=\lambda U_D(f)$ and $L_D(\lambda f)=\lambda L_D(f)$. Taking infimum and supremum over $D$, both integrals of $\lambda f$ equal $\lambda\int f$.

2. *Negation.* $M_i(-f)=-m_i(f)$ and $m_i(-f)=-M_i(f)$, so $U_D(-f)=-L_D(f)$ and $L_D(-f)=-U_D(f)$. Hence $\overline\int(-f)=-\underline\int f=-\int f=\underline\int(-f)$.

3. *Sums.* On each subinterval $f(x)+g(x)\le M_i(f)+M_i(g)$, so $M_i(f+g)\le M_i(f)+M_i(g)$ and $U_D(f+g)\le U_D(f)+U_D(g)$; likewise $L_D(f+g)\ge L_D(f)+L_D(g)$.

4. Given $\varepsilon>0$, choose $D_1,D_2$ with $U_{D_1}(f)<\int f+\varepsilon$ and $U_{D_2}(g)<\int g+\varepsilon$; for their common refinement $D$, $\overline\int(f+g)\le U_D(f+g)\le U_D(f)+U_D(g)<\int f+\int g+2\varepsilon$. So $\overline\int(f+g)\le\int f+\int g$, and symmetrically $\underline\int(f+g)\ge\int f+\int g$. As $\underline\int\le\overline\int$, all are equal.

5. Combining steps 1, 2 and 4 gives the general case.

:::

::: {#prp-integral-monotone .proposition name="Monotonicity and absolute value"}

Let $f,g$ be integrable on $[a,b]$.

1. If $f\le g$, then $\int_a^bf\le\int_a^bg$.
2. $|f|$ is integrable, and $\left|\int_a^bf\right|\le\int_a^b|f|$.
3. If $|f-g|\le C$ on $[a,b]$, then $\left|\int_a^bf-\int_a^bg\right|\le C(b-a)$.

:::

::: {.proof}

1. $M_i(f)\le M_i(g)$ for each subinterval, so $U_D(f)\le U_D(g)$ for every $D$; take infima.

2. On a subinterval, $M_i(f)-m_i(f)=\sup_{u,v}|f(u)-f(v)|$, and likewise for $|f|$. By the reverse triangle inequality $\bigl||f(u)|-|f(v)|\bigr|\le|f(u)-f(v)|$, so $U_D(|f|)-L_D(|f|)\le U_D(f)-L_D(f)$, and @thm-riemann-criterion gives integrability of $|f|$.

3. From $-|f|\le f\le|f|$ and part 1, $-\int|f|\le\int f\le\int|f|$, which is the inequality in part 2.

4. For part 3, apply part 2 to $f-g$ (integrable by linearity) and part 1 to $|f-g|\le C$: $\left|\int(f-g)\right|\le\int|f-g|\le C(b-a)$.

:::

::: {#thm-integral-additive .theorem name="Additivity over intervals"}

Let $a<b<c$. Then $f$ is integrable on $[a,c]$ if and only if it is integrable on $[a,b]$ and on $[b,c]$, and then
$$\int_a^bf+\int_b^cf=\int_a^cf.$$

:::

::: {.proof}

1. A dissection $D$ of $[a,c]$ containing $b$ splits into dissections $D_1$ of $[a,b]$ and $D_2$ of $[b,c]$, with $U_D(f)=U_{D_1}(f)+U_{D_2}(f)$ and $L_D(f)=L_{D_1}(f)+L_{D_2}(f)$. Every dissection of $[a,c]$ can be refined to contain $b$, and every pair $D_1,D_2$ arises this way.

2. ($\Rightarrow$) Let $\varepsilon>0$. By @thm-riemann-criterion there is $D$ with $U_D(f)-L_D(f)<\varepsilon$; adding $b$ keeps this (@lem-refinement-sums). Then $(U_{D_1}-L_{D_1})+(U_{D_2}-L_{D_2})<\varepsilon$, and both brackets are non-negative, so each is less than $\varepsilon$: $f$ is integrable on both pieces.

3. ($\Leftarrow$) Given dissections $D_1,D_2$ of the pieces with $U-L<\varepsilon/2$ on each, their union $D$ has $U_D(f)-L_D(f)<\varepsilon$.

4. In either case, $\int_a^bf+\int_b^cf$ and $\int_a^cf$ both lie between $L_D(f)$ and $U_D(f)$ for the dissections in step 2 or 3, which differ by less than $\varepsilon$. So they are equal.

:::

With the convention $\int_b^af=-\int_a^bf$ (and $\int_a^af=0$), the formula holds for $a,b,c$ in any order.

::: {#prp-integral-product .proposition name="Products"}

If $f,g$ are integrable on $[a,b]$, so is $fg$.

:::

::: {.proof}

1. Let $|f|,|g|\le C$ on $[a,b]$. Fix a dissection $D$ and a subinterval $[x_{i-1},x_i]$, and let $u,v$ be any two of its points.

2. Then $f(v)g(v)-f(u)g(u)=f(v)\bigl(g(v)-g(u)\bigr)+\bigl(f(v)-f(u)\bigr)g(u)$, so
$$|f(v)g(v)-f(u)g(u)|\le C\bigl(M_i(g)-m_i(g)\bigr)+C\bigl(M_i(f)-m_i(f)\bigr).$$

3. The supremum of the left side over $u,v$ is $M_i(fg)-m_i(fg)$. Multiplying by $x_i-x_{i-1}$ and summing,
$$U_D(fg)-L_D(fg)\le C\bigl(U_D(f)-L_D(f)+U_D(g)-L_D(g)\bigr).$$

4. Choose $D$ (a common refinement) making both brackets less than $\frac{\varepsilon}{2C}$; then @thm-riemann-criterion applies.

:::

There is no product formula: in general $\int fg\ne\int f\int g$. Integration by parts (@thm-integration-by-parts-proof) is the substitute.
