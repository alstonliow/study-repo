<!-- Added 2026-11-18 for Stanford CS221 Lecture 10; our own NumPy version of linear Q-learning with doubling features (the lecture's agent is in PyTorch). -->

::: {#exm-function-approximation-code-1 .example name="Linear Q-learning on the flaky tram" origin="self"}

Needs NumPy. The run of @exm-function-approximation-1: four parameters, Q-learning steps on the squared loss, and the exact expected time of the learned greedy policy.

```{.python .runnable packages="numpy"}
import numpy as np

n, p = 100, 0.4                       # flaky tram with 100 locations
rng = np.random.default_rng(0)

def actions(s):
    return ["walk"] + (["tram"] if 2 * s <= n else [])

def step(s, a):                       # environment: unknown to the agent
    if a == "walk":
        return -1, s + 1
    return -2, (2 * s if rng.random() > p else s)

def phi(s, a):                        # doubling features, d(s) = log2(n / s)
    d = np.log2(n / s)
    return np.array([a == "walk", a == "tram", (a == "walk") * d, (a == "tram") * d], float)

theta, eta, eps = np.zeros(4), 0.01, 0.2
Q = lambda s, a: theta @ phi(s, a)
for episode in range(30):
    s = 1
    while s != n:
        acts = actions(s)
        a = rng.choice(acts) if rng.random() < eps else max(acts, key=lambda b: Q(s, b))
        r, s2 = step(s, a)
        target = r if s2 == n else r + max(Q(s2, b) for b in actions(s2))
        theta -= eta * (Q(s, a) - target) * phi(s, a)   # Q-learning step on the squared loss
        s = s2
print(np.round(theta, 2))
print("greedy actions at 1, 10, 30, 60:", [max(actions(s), key=lambda b: Q(s, b)) for s in (1, 10, 30, 60)])

def expected_time(policy):            # exact, by solving the MDP for this policy
    V = {n: 0.0}
    for s in range(n - 1, 0, -1):
        V[s] = 1 + V[s + 1] if policy(s) == "walk" else (2 + (1 - p) * V[2 * s]) / (1 - p)
    return round(V[1], 2)
print("expected time of greedy policy:", expected_time(lambda s: max(actions(s), key=lambda b: Q(s, b))))
print("always walk:", expected_time(lambda s: "walk"))
```

```text
[-6.73 -1.61 -2.32 -3.49]
greedy actions at 1, 10, 30, 60: ['walk', 'tram', 'tram', 'walk']
expected time of greedy policy: 37.33
always walk: 99.0
```

:::
