<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-4-q6" status="draft"}
**(a)**

1. With logits $z=\theta^\top\phi(s)$, $\log\pi_\theta(a\mid s)=z_a-\log\sum_{a'}e^{z_{a'}}$.
2. Its gradient with respect to the logits is $\nabla_z\log\pi_\theta(a\mid s)=e_a-\pi_\theta(\cdot\mid s)$ (the negative of the cross-entropy gradient $p-y$).
3. Chain rule: $z_{a'}=\sum_j\theta_{ja'}\phi_j(s)$, so $\partial z_{a'}/\partial\theta_{ja'}=\phi_j(s)$ and $z_{a'}$ does not depend on other columns.
4. Hence, as a $d\times 3$ matrix,
$$\nabla_\theta\log\pi_\theta(a\mid s)=\phi(s)\,\big(e_a-\pi_\theta(\cdot\mid s)\big)^\top.$$

**(b)** At $\theta=0$ the policy is uniform, so $\nabla_\theta\log\pi_\theta(\text{right})=e_2-(\tfrac13,\tfrac13,\tfrac13)=(-\tfrac13,-\tfrac13,\tfrac23)$. The episode's utility is $-1$.

1. No baseline: the weight is $\text{utility}-b=-1$, so the update is
$$\eta\,(-1)\,(-\tfrac13,-\tfrac13,\tfrac23)=\eta\,(\tfrac13,\tfrac13,-\tfrac23).$$
$\theta_2$ drops, so the car is **less** likely to accelerate right, even though it took the best action.
2. Baseline $b=-2$: the weight is $-1-(-2)=+1$, so the update is
$$\eta\,(-\tfrac13,-\tfrac13,\tfrac23),$$
and the car is **more** likely to accelerate right. All rewards are negative, so without a baseline every sampled action is pushed down; the good action is only pushed down less than bad ones would be, which shows up only on average over many episodes. The baseline measures the reward against the policy's expected reward, so an action better than average gets a positive weight in every single update.
:::
