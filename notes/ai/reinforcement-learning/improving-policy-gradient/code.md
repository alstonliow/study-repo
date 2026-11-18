<!-- Added 2026-11-18 for Stanford CS221 Lectures 11-12; our own NumPy version of REINFORCE and the future-utility estimator on the first game show (the lecture's agents are in PyTorch). -->

::: {#exm-improving-policy-gradient-code-1 .example name="REINFORCE versus future utility" origin="self"}

Needs NumPy. Ten training runs of each estimator, as in @fig-improving-policy-gradient-2; the only difference is the credit given to step $t$.

```{.python .runnable packages="numpy"}
import numpy as np

# Two-step game show: step 1 left = 10 points, right = 1; step 2 left = 2, right = 1.
REWARD = {("S", "left"): 10, ("S", "right"): 1, ("A", "left"): 2, ("A", "right"): 1}
sigma = lambda z: 1 / (1 + np.exp(-z))

def train(credit, seed, episodes=100, eta=0.1):
    rng, theta = np.random.default_rng(seed), {"S": 0.0, "A": 0.0}  # pi(left | s) = sigma(theta_s)
    for _ in range(episodes):
        steps = []
        for s in ("S", "A"):
            a = "left" if rng.random() < sigma(theta[s]) else "right"
            steps.append((s, a, REWARD[(s, a)]))
        rewards = [r for _, _, r in steps]
        for t, (s, a, _) in enumerate(steps):
            grad_log = (1 - sigma(theta[s])) if a == "left" else -sigma(theta[s])  # d/dtheta log pi(a|s)
            theta[s] += eta * credit(rewards, t) * grad_log                        # gradient ascent
    return sigma(theta["A"])

reinforce = lambda rewards, t: sum(rewards)        # u(tau) for every step
future = lambda rewards, t: sum(rewards[t:])       # u_t: rewards from step t on
for name, credit in [("REINFORCE", reinforce), ("future utility", future)]:
    probs = [train(credit, seed) for seed in range(10)]
    print(f"{name:15s} P(left in step 2): mean {np.mean(probs):.2f}, runs below 0.5: {sum(p < 0.5 for p in probs)}")
```

```text
REINFORCE       P(left in step 2): mean 0.40, runs below 0.5: 6
future utility  P(left in step 2): mean 0.87, runs below 0.5: 0
```

:::
