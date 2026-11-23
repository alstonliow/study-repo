<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-eecs126hw-6-q2" status="draft"}
(a) $\operatorname{var}(\bar X_n)=\sigma^2/n$. By Chebyshev's inequality with $\epsilon=\sigma/\sqrt{na}$, $P(|\bar X_n-\mu|\ge\epsilon)\le\frac{\sigma^2/n}{\epsilon^2}=a$.

(b) Choose $\epsilon$ with $2e^{-2n\epsilon^2}=a$, i.e. $\epsilon=\sqrt{\ln(2/a)/(2n)}=\frac1{2\sqrt n}\sqrt{2\ln\frac2a}$. (This is @thm-hoeffding-inequality with range $1$.)

(c) For $s>0$, Markov's inequality on $e^{sZ}$ gives $P(Z\ge\epsilon)\le e^{-s\epsilon}E[e^{sZ}]=e^{-s\epsilon+s^2/2}$; take $s=\epsilon$. By symmetry $P(|Z|\ge\epsilon)\le2e^{-\epsilon^2/2}$.

(d) By the CLT, $\sqrt n(\bar X_n-\mu)/\sigma$ is approximately $N(0,1)$, so $P(|\bar X_n-\mu|\ge\sigma\epsilon/\sqrt n)\approx P(|Z|\ge\epsilon)\le2e^{-\epsilon^2/2}$, which equals $a$ for $\epsilon=\sqrt{2\ln(2/a)}$. It is heuristic because the CLT is only a limit statement, with no error bound at finite $n$.

(e) All three shrink like $1/\sqrt n$. Their widths scale with $a$ as $a^{-1/2}$ (Chebyshev) against $\sqrt{\ln(2/a)}$ (the other two), so for small $a$ Chebyshev is far wider. The Chernoff interval does not need $\sigma$ (it is the CLT interval with the worst case $\sigma=\frac12$), so it is always valid but wider when $q$ is near $0$ or $1$; the CLT interval is the narrowest but only approximate. For $a=0.05$ the half-widths are $4.47\sigma/\sqrt n$, $1.36/\sqrt n$ and $2.72\sigma/\sqrt n$.
:::
