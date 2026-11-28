<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-6-q2" status="draft"}
(a) $\operatorname{var}(\bar X_n)=\sigma^2/n$. By Chebyshev's inequality with $\epsilon=\sigma/\sqrt{na}$, $P(|\bar X_n-\mu|\ge\epsilon)\le\frac{\sigma^2/n}{\epsilon^2}=a$.

(b) Choose $\epsilon$ with $2e^{-2n\epsilon^2}=a$, i.e. $\epsilon=\sqrt{\ln(2/a)/(2n)}=\frac1{2\sqrt n}\sqrt{2\ln\frac2a}$. (This is @thm-hoeffding-inequality with range $1$.)

(c) For $s>0$, Markov's inequality on $e^{sZ}$ gives $P(Z\ge\epsilon)\le e^{-s\epsilon}E[e^{sZ}]=e^{-s\epsilon+s^2/2}$; take $s=\epsilon$. By symmetry $P(|Z|\ge\epsilon)\le2e^{-\epsilon^2/2}$.

(d) By the CLT, $\sqrt n(\bar X_n-\mu)/\sigma$ is approximately $N(0,1)$, so $P(|\bar X_n-\mu|\ge\sigma\epsilon/\sqrt n)\approx P(|Z|\ge\epsilon)\le2e^{-\epsilon^2/2}$, which equals $a$ for $\epsilon=\sqrt{2\ln(2/a)}$. It is heuristic because the CLT is only a limit statement, with no error bound at finite $n$.

(e) All three shrink like $1/\sqrt n$. Their widths scale with $a$ as $a^{-1/2}$ (Chebyshev) against $\sqrt{\ln(2/a)}$ (the other two), so for small $a$ Chebyshev is far wider. The Chernoff interval does not need $\sigma$ (it is the CLT interval with the worst case $\sigma=\frac12$), so it is always valid but wider when $q$ is near $0$ or $1$; the CLT interval is the narrowest but only approximate. For $a=0.05$ the half-widths are $4.47\sigma/\sqrt n$, $1.36/\sqrt n$ and $2.72\sigma/\sqrt n$.
:::

::: {.solution for="prob-eecs126-1-q2" status="draft"}
As in the notes, assume $\mu_i=0$ and $K=1$ (centring changes $K$ by a factor of at most $2$, which goes into $c$), and bound the upper tail; the lower tail is the same for $-X_i$ and costs a factor $2$ in $C$.

1. *A moment generating bound for all $t\ge0$.* For $|y|\le t$, Taylor's theorem gives $e^y=1+y+\frac{y^2}2e^\xi$ with $|\xi|\le t$, so $e^y\le1+y+\frac{y^2}2e^t$. With $y=tX_i$ and $EX_i=0$: $Ee^{tX_i}\le1+\frac{t^2\sigma_i^2}2e^t\le\exp\bigl(\frac{t^2\sigma_i^2}2e^t\bigr)$.

2. *Markov.* By independence $Ee^{tS_n}\le\exp\bigl(\frac{t^2\sigma^2}2e^t\bigr)$, so for every $t\ge0$
$$P(S_n\ge\lambda\sigma)\le\exp\Bigl(\frac{t^2\sigma^2}2e^t-t\lambda\sigma\Bigr).$$

3. *Choose $t$ outside $[0,1]$.* Let $\lambda>\sigma$ and $t=\frac12\log\frac\lambda\sigma>0$, so $e^t=(\lambda/\sigma)^{1/2}$. Then $\frac{t^2\sigma^2}2e^t\le\frac{t\lambda\sigma}2$ is equivalent to $t\le(\lambda/\sigma)^{1/2}$, that is, $\frac12\log u\le u^{1/2}$ with $u=\lambda/\sigma$. This holds for all $u>0$, since $\log u\le u^{1/2}$ (the maximum of $u^{-1/2}\log u$ is $2/e<1$).

4. *The bound.* Hence $P(S_n\ge\lambda\sigma)\le e^{-t\lambda\sigma/2}=\exp\bigl(-\frac{\lambda\sigma}4\log\frac\lambda\sigma\bigr)=(\lambda/\sigma)^{-\lambda\sigma/4}$.

5. *Undo $K=1$.* Apply step 4 to $X_i/K$, whose standard deviation is $\sigma/K$: the event $S_n\ge\lambda\sigma$ is $S_n/K\ge\lambda(\sigma/K)$. So $P(S_n\ge\lambda\sigma)\le(\lambda K/\sigma)^{-\lambda\sigma/(4K)}$ when $\lambda K>\sigma$.

6. *Replace the term.* If $\lambda K/\sigma\le e$, then $(\lambda K/\sigma)^{-c\lambda\sigma/K}\ge e^{-c\lambda\sigma/K}$, so the old bound (6) already gives the new one. If $\lambda K/\sigma>e$, step 5 gives it with $c=1/4$. Taking $c$ as the smaller of the two constants, $P(|S_n-\mu|\ge\lambda\sigma)\le C\max\bigl(e^{-c\lambda^2},(\lambda K/\sigma)^{-c\lambda\sigma/K}\bigr)$. For $\lambda K\gg\sigma$ the factor $\log(\lambda K/\sigma)$ in the exponent makes this much smaller than $e^{-c\lambda\sigma/K}$.
:::
