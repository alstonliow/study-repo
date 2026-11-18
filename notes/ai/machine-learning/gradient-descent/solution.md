<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-1-q3" status="draft"}
1. Derivative: $f'(\theta)=2\sum_i w_i(\theta-x_i)=2\big(\theta\sum_i w_i-\sum_i w_ix_i\big)$.
2. Setting $f'(\theta)=0$ gives the weighted mean
$$\theta^*=\frac{\sum_{i=1}^n w_ix_i}{\sum_{i=1}^n w_i}.$$
3. Minimum: $f''(\theta)=2\sum_i w_i>0$ because every $w_i>0$. So $f$ is strictly convex and $\theta^*$ is its unique global minimum.
4. Negative weights: if $\sum_i w_i<0$, then $f''<0$, $f$ is a downward parabola, $\theta^*$ is a maximum and $f(\theta)\to-\infty$ as $|\theta|\to\infty$, so there is no minimum. If $\sum_i w_i=0$, $f$ is linear (or constant) and $\theta^*$ is undefined, with again no minimum unless $\sum_i w_ix_i=0$. Even when $\sum_i w_i>0$, a negative weight pushes $\theta^*$ away from that point, and $\theta^*$ can fall outside the range of the $x_i$.
:::
