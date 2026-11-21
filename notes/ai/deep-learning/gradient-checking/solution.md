<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs231na-1-q5" status="draft"}
1. *Cause.* The SVM loss is piecewise linear: each term $\max(0,s_j-s_{y_i}+\Delta)$ has a kink where its argument is $0$. If the two evaluations $f(\theta\pm h\mathbf{e}_k)$ of the centred difference lie on different sides of a kink, the numerical gradient averages the two one-sided slopes, while the analytic gradient takes one of them (@sec-ai-deep-learning-gradient-checking).
2. *Concern.* It is not a sign of a bug, as long as the mismatches are rare and occur only in dimensions near a kink; a bug produces mismatches in many dimensions.
3. *One-dimensional example.* Let $f(w)=\max(0,w)$, with analytic derivative $1$ for $w>0$. At $w=10^{-6}$ with $h=10^{-5}$, the centred difference is $\bigl(\max(0,1.1\cdot10^{-5})-\max(0,-0.9\cdot10^{-5})\bigr)/(2\cdot10^{-5})=0.55$, a relative error of $0.45$.
4. *Effect of the margin.* A mismatch requires some argument $s_j-s_{y_i}+\Delta$ to be within about $h$ of $0$. With small random weights the score differences $s_j-s_{y_i}$ are all near $0$, so with $\Delta=0$ almost every term sits at its kink and mismatches are frequent. A larger margin $\Delta$ moves the kinks away from where the arguments concentrate at initialization, so mismatches become rarer (later in training, as score differences spread out, the frequency depends on how many arguments happen to lie near $0$).
:::
