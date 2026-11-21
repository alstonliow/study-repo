::: {.problem #prob-camii-pms-3-q1 origin="external" source="camii-pms-3-q1"}
Suppose that a nonnegative simple function $f$ has two representations
$$f=\sum_{k=1}^ma_k\mathbf 1_{A_k}=\sum_{j=1}^nb_j\mathbf 1_{B_j}.$$
Here all $A_k,B_j$ are measurable and $a_k,b_j\ge0$. In the sums below, use the convention $0\cdot\infty=0$. For $\varepsilon=(\varepsilon_1,\dots,\varepsilon_m)\in\{0,1\}^m$, define $A_\varepsilon=A_1^{\varepsilon_1}\cap\dots\cap A_m^{\varepsilon_m}$ where $A_k^0=A_k^c$ and $A_k^1=A_k$. Define similarly $B_\delta$ for $\delta\in\{0,1\}^n$. Then set $f_{\varepsilon,\delta}=\sum_{k=1}^m\varepsilon_ka_k$ if $A_\varepsilon\cap B_\delta\neq\emptyset$ and $f_{\varepsilon,\delta}=0$ otherwise. Show that, for any measure $\mu$,
$$\sum_{k=1}^ma_k\mu(A_k)=\sum_{\varepsilon,\delta}f_{\varepsilon,\delta}\,\mu(A_\varepsilon\cap B_\delta)$$
and deduce that
$$\sum_{k=1}^ma_k\mu(A_k)=\sum_{j=1}^nb_j\mu(B_j).$$
:::

::: {.problem #prob-camii-pms-3-q3 origin="external" source="camii-pms-3-q3"}
Let $f$ be an integrable function on a measure space $(E,\mathcal E,\mu)$. Suppose that, for some π-system $\mathcal A$ containing $E$ and generating $\mathcal E$, we have $\mu(f\mathbf 1_A)=0$ for all $A\in\mathcal A$. Show that $f=0$ a.e.
:::

::: {.problem #prob-camii-pms-3-q5 origin="external" source="camii-pms-3-q5"}
For $\alpha\in(0,\infty)$ and $x\in(0,\infty)$, define $f_\alpha(x)=x^{-\alpha}$. Show that $f_\alpha$ is integrable with respect to Lebesgue measure on $(0,1]$ if and only if $\alpha<1$. Show also that $f_\alpha$ is integrable with respect to Lebesgue measure on $[1,\infty)$ if and only if $\alpha>1$.
:::

::: {.problem #prob-camii-pms-3-q6 origin="external" source="camii-pms-3-q6"}
Show that the function $\sin x/x$ is not Lebesgue integrable over $[1,\infty)$ but that integral $\int_1^N(\sin x/x)\,dx$ converges as $N\to\infty$.
:::

::: {.problem #prob-camii-pms-3-q9 origin="external" source="camii-pms-3-q9"}
Let $(E,\mathcal E)$ and $(G,\mathcal G)$ be measurable spaces and let $f:E\to G$ be a measurable function. Given a measure $\mu$ on $(E,\mathcal E)$, consider the image measure $\nu=\mu\circ f^{-1}$ on $(G,\mathcal G)$. Show that $\nu(g)=\mu(g\circ f)$ for all non-negative measurable functions $g$ on $G$.
:::
