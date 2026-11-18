::: {.problem #prob-cs221hw-4-q6 origin="external" source="cs221hw-4-q6"}
In Problem 3 we estimated the MDP, and in Problems 4 and 5 we estimated Q-values. In this problem we will estimate the policy *directly*, using REINFORCE from the [policy gradient lecture](https://stanford-cs221.github.io/lectures/?trace=policy_gradient). We will train a policy for Mountain Car, see why it needs a baseline, add bootstrapping, and compare the result with your Q-learning agents.

Our policy is a linear softmax over your Fourier features from 4b. With features $\phi(s) \in \mathbb{R}^d$ and a $d \times 3$ matrix $\theta$ (one column per action), the logits are $z = \theta^\top \phi(s)$ and $$\pi_\theta(a \mid s) = \frac{e^{z_a}}{\sum_{a'} e^{z_{a'}}}.$$ As in lecture, the utility of a rollout (one episode) $\tau = (s_0, a_1, r_1, s_1, \ldots, a_n, r_n, s_n)$ is $\text{utility}(\tau) = \sum_{t=1}^n \gamma^{t-1} r_t$ (what the plots call the discounted reward of an episode). After each rollout, REINFORCE with a baseline $b$ takes a gradient ascent step on the lecture's objective $$J(\theta, \tau) = \sum_{t=1}^n \log \pi_\theta(a_t \mid s_{t-1})\, \big(\text{utility}(\tau) - b\big).$$

(a) Before we can do gradient ascent on the policy, we need the gradient of $\log \pi_\theta(a \mid s)$ with respect to $\theta$. Derive it for our softmax policy; your answer should be a $d \times 3$ matrix.

*Hint: $\log \pi_\theta(a \mid s)$ is the negative of the cross-entropy loss from HW2 Problem 1d, with logits $z$ and label $a$.*

*Expected:* Your derivation, showing the gradient with respect to the logits and the chain rule through $z = \theta^\top \phi(s)$, and the final matrix written in terms of $\phi(s)$, $\pi_\theta(\cdot \mid s)$, and the one-hot vector $e_a$ for action $a$.

(b) Let's try the REINFORCE update on a tiny version of Mountain Car. Use our softmax policy with a single feature $\phi(s) = 1$, so $\theta = (\theta_0, \theta_1, \theta_2)$ is one logit per action (accelerate left, don't accelerate, accelerate right) and $\pi_\theta(a) = e^{\theta_a} / (e^{\theta_0} + e^{\theta_1} + e^{\theta_2})$. Each episode is a single step, with reward $-3$ for accelerating left, $-2$ for not accelerating, and $-1$ for accelerating right. Start at $\theta = (0, 0, 0)$, and suppose the car accelerates right, the best action.

i.  With no baseline ($b = 0$), compute the update $\eta\, \nabla_\theta J(\theta, \tau)$ to $\theta$, with step size $\eta > 0$. Is the car more or less likely to accelerate right next time?
ii. Now compute the update with the baseline $b = -2$, the expected reward under the current policy. Is the car now more or less likely to accelerate right, and why does the baseline change the answer?

*Expected:* For (i), the update in terms of $\eta$, with your work shown, and "more" or "less". For (ii), the same, and 1-2 sentences on why the baseline changes the answer.

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::
