::: {.problem #prob-camii-pms-7-q6 origin="external" source="camii-pms-7-q6"}
(i) Show that for any real numbers $a,b$ one has $\int_a^be^{itx}\,dx\to0$ as $|t|\to\infty$.
(ii) Show that, for any $f\in L^1(\mathbb R)$, the Fourier transform
$$\hat f(t)=\int_{-\infty}^\infty e^{itx}f(x)\,dx$$
tends to $0$ as $|t|\to\infty$. This is the *Riemann–Lebesgue Lemma*.
(iii)$^*$ Show that the image of $L^1(\mathbb R)$ under the Fourier transform is a *proper* subset of the space $C_0(\mathbb R)$ of bounded continuous functions that vanish at infinity. [Hint: Use the *open mapping theorem* from linear analysis.]
:::

::: {.problem #prob-camii-pms-7-q7 origin="external" source="camii-pms-7-q7"}
Say that $f\in L^2(\mathbb R)$ is $L^2$-differentiable with $L^2$-derivative $Df$ if
$$\frac{\|\tau_hf-f-hDf\|_2}{h}\to0\quad\text{as}\quad h\to0,$$
where $\tau_hf(x)=f(x+h)$. Show that the function $f(x)=\max(1-|x|,0)$ is $L^2$-differentiable and find its $L^2$-derivative. Suppose that $f\in L^1\cap L^2$ is $L^2$-differentiable. Show that $u\hat f(u)\in L^2$. Deduce that $f$ has a continuous version and that $\|f\|_\infty\le C\|(1+|u|)\hat f(u)\|_2$ for some absolute constant $C<\infty$, to be determined. This is a simple example of a *Sobolev inequality*.
:::
