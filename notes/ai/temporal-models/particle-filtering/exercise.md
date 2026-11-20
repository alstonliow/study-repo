::: {#prob-particle-filter-code .problem .coding origin="adapted" source="res-ucb-cs188-projects-tracking" solution="withheld"}
Implement one step of particle filtering (@def-particle-filtering): elapse time, observe and resample. Write `particle_filter_step(particles, e, sample_next, emission, rng)`.

- `particles` is a list of $N$ states (hashable values, repetitions allowed).
- `sample_next(x, rng)` returns a state drawn from $P(X_{t+1}\mid X_t=x)$, using `rng`.
- `emission(e, x)` returns $P(E=e\mid X=x)$.
- `rng` is a `random.Random`; draw all randomness from it, never from the module `random`.

Return a new list of $N$ unweighted particles and leave `particles` unchanged. Assume at least one weight is positive. The tests are statistical: they compare particle frequencies with the exact belief, with tolerances that a correct filter passes with overwhelming probability.

```{.python .starter}
def particle_filter_step(particles, e, sample_next, emission, rng):
    """Elapse time, weight by the evidence e and resample; return N new particles."""
    ...
```

```{.python .tests}
import random
from collections import Counter

# the weather chain: stays the same with probability 0.7;
# P(umbrella | rain) = 0.8, P(umbrella | sun) = 0.3
def sample_next(x, rng):
    if rng.random() < 0.7:
        return x
    return "sun" if x == "rain" else "rain"


def emission(e, x):
    p = 0.8 if x == "rain" else 0.3
    return p if e == "umbrella" else 1 - p


def freq(ps, x):
    return Counter(ps)[x] / len(ps)


def test_matches_exact_belief():
    rng = random.Random(1)
    N = 20000
    particles = ["rain"] * (N * 8 // 11) + ["sun"] * (N - N * 8 // 11)   # B_1 of the umbrella example
    new = particle_filter_step(particles, "umbrella", sample_next, emission, rng)
    assert len(new) == N
    assert abs(freq(new, "rain") - 104 / 131) < 0.02, f"rain frequency {freq(new, 'rain'):.3f}, exact 0.794"


def test_evidence_against_rain():
    rng = random.Random(2)
    N = 20000
    new = particle_filter_step(["rain"] * N, "none", sample_next, emission, rng)
    # prediction 0.7 rain; weights 0.2 and 0.7 give 0.14 / (0.14 + 0.21) = 0.4
    assert abs(freq(new, "rain") - 0.4) < 0.02, f"rain frequency {freq(new, 'rain'):.3f}, exact 0.4"


def test_decisive_evidence_and_input_unchanged():
    rng = random.Random(3)
    walk = lambda x, rng: x + rng.choice([-1, 0, 1])
    sensor = lambda e, x: 1.0 if x == e else 0.0       # the sensor reads the state exactly
    particles = [0] * 50 + [5] * 50
    before = list(particles)
    new = particle_filter_step(particles, 1, walk, sensor, rng)
    assert particles == before
    assert len(new) == 100 and set(new) == {1}


def test_uses_given_rng():
    run = lambda seed: particle_filter_step(["rain", "sun"] * 50, "umbrella", sample_next, emission, random.Random(seed))
    assert run(7) == run(7), "the same seed must give the same particles"
    assert any(run(7) != run(s) for s in range(8, 12))
```
:::
