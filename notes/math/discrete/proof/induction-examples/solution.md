<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->

::: {.solution for="prob-proofs-10"}
(a) For fixed $i,j$: $j$ loop from $1$ to $i$, $k$ loop from $1$ to
    $j$. Observe that for each pair $(i,j)$, the innermost action is
    performed $j$ times.

(b) For fixed $i$: $j$ loops from $1$ to $i$, and for each $j$ the
    inner loop runs $j$ times. So the number of times the action is
    performed is
    $$\sum_{j=1}^{i} j = \frac{i(i+1)}{2}.$$

(c) Summing over $i$ from $1$ to $n$:
    $$\text{num of action} = \sum_{i=1}^{n}\sum_{j=1}^{i} j
                = \sum_{i=1}^{n} \frac{i(i+1)}{2}.$$

(d) Evaluating $\displaystyle\sum_{i=1}^{n}\frac{i(i+1)}{2}$ for
    small $n$:
    $$n=1: 1, \quad n=2: 4, \quad n=3: 10, \quad n=4: 20, \quad
                n=5: 35.$$

(e) The sequence $1,4,10,20,35,\dots$ is the sequence of
    *tetrahedral numbers*. Each term is obtained from the
    previous by adding the next triangular number
    ($1,3,6,10,15,\dots$), and the values grow roughly cubically in
    $n$.

(f) Conjecture:
    $$\sum_{i=1}^{n}\frac{i(i+1)}{2} = \frac{n(n+1)(n+2)}{6}.$$
    *Derivation:* using $\displaystyle\sum_{i=1}^n i^2 =
            \frac{n(n+1)(2n+1)}{6}$ and $\displaystyle\sum_{i=1}^n i =
            \frac{n(n+1)}{2}$,
    $$\begin{aligned}
                \sum_{i=1}^n \frac{i^2+i}{2}
                &= \frac12\left[\frac{n(n+1)(2n+1)}{6}
                    + \frac{n(n+1)}{2}\right] \\
                &= \frac{1}{12}\left[n(n+1)(2n+1) + 3n(n+1)\right] \\
                &= \frac{1}{12}\,n(n+1)\big[(2n+1)+3\big]
                    = \frac{1}{12}\,n(n+1)(2n+4) \\
                &= \frac{1}{6}\,n(n+1)(n+2).
            \end{aligned}$$
    This matches the numerical values in part (d): $n=5$ gives
    $\frac{5\cdot6\cdot7}{6}=35$. 

(g) **Proof (by induction on $n$).**

    *Base case ($n=1$).* LHS $=\dfrac{1\cdot2}{2}=1$.
    RHS $=\dfrac{1\cdot2\cdot3}{6}=1$. Equal, so the base case holds.

    *Inductive hypothesis.* Assume for some $n\ge1$,
    $$\sum_{i=1}^{n}\frac{i(i+1)}{2} = \frac{n(n+1)(n+2)}{6}.$$

    *Inductive step.* We show the formula holds for $n+1$:
    $$\begin{aligned}
                \sum_{i=1}^{n+1}\frac{i(i+1)}{2}
                &= \sum_{i=1}^{n}\frac{i(i+1)}{2} + \frac{(n+1)(n+2)}{2} \\
                &= \frac{n(n+1)(n+2)}{6} + \frac{(n+1)(n+2)}{2}
                    \qquad \text{(by inductive hypothesis)} \\
                &= \frac{n(n+1)(n+2) + 3(n+1)(n+2)}{6} \\
                &= \frac{(n+1)(n+2)(n+3)}{6}.
            \end{aligned}$$
    This matches the conjectured formula with $n$ replaced by $n+1$.

    By the Principle of Mathematical Induction, the formula
    $$\sum_{i=1}^{n}\frac{i(i+1)}{2} = \frac{n(n+1)(n+2)}{6}$$
    holds for all $n\ge1$. 0◻
:::

::: {.solution for="prob-proofs-11"}
The $n$-th harmonic number $H_n$ is defined by
$$H_n = 1+\frac12+\frac13+\cdots+\frac1n.$$

# Main result: $H_n \ge \ln(n+1)$

::: {.proof name="Proof (by induction on $n$)"}

**Base case ($n=1$).** $H_1=1$, and $\ln(1+1)=\ln2<1$. So
$H_1 \ge \ln(1+1)$.

**Inductive hypothesis.** Assume $H_n \ge \ln(n+1)$ for some
$n\ge1$.

**Inductive step.** We show $H_{n+1}\ge\ln(n+2)$.

By definition,
$$H_{n+1} = H_n+\frac{1}{n+1} \ge \ln(n+1)+\frac{1}{n+1}.$$
We claim $\ln(n+1)+\dfrac{1}{n+1} \ge \ln(n+2)$. Observe that
$$\ln(n+2)-\ln(n+1) = \ln\left(\frac{n+2}{n+1}\right)
        = \ln\left(1+\frac{1}{n+1}\right) \le \frac{1}{n+1},$$
using $\ln(1+x)\le x$ (with $x=\frac{1}{n+1}$). Rearranging,
$$\ln(n+1)+\frac{1}{n+1} \ge \ln(n+2).$$
Combining the two inequalities,
$$H_{n+1} \ge \ln(n+1)+\frac{1}{n+1} \ge \ln(n+2).$$
So the statement holds for $n+1$.

**Conclusion.** By the Principle of Mathematical Induction,
$H_n \ge \ln(n+1)$ for all $n\ge1$.

:::

# Advanced afterthoughts

1.  The inequality $H_n\ge\ln(n+1)$ implies $H_n\ge\ln n$, since
    $\ln(n+1)\ge\ln n$. Trying to prove $H_n\ge\ln n$ *directly*
    by induction runs into a snag: in the inductive step, one would
    need
    $$\ln(n+1)-\ln n = \ln\left(1+\frac1n\right) \le \frac{1}{n+1},$$
    but $\ln(1+x)\le x$ only gives the weaker bound
    $\ln(1+\frac1n)\le\frac1n$, which is not tight enough (since
    $\frac1n > \frac{1}{n+1}$). This illustrates that induction
    sometimes requires proving something *stronger* than what
    one set out to prove — the extra “room” in $\ln(n+1)$
    compared to $\ln n$ is exactly what makes the induction go
    through.

2.  The proof relies on the inequality $\ln(1+x)\le x$, which is a
    property specific to the natural logarithm (it comes from
    $\ln(1+x)$ being concave with tangent line $y=x$ at $x=0$). For a
    logarithm to another base $b\ne e$, the analogous inequality
    $\log_b(1+x)\le x$ does not hold in general, so the proof does
    not transfer directly to other bases without first converting
    back to $\ln$ via the change-of-base formula.

3.  **Claim: $H_n \le \ln n+1$.**

    ::: {.proof name="Proof (by induction on $n$)"}

    **Base case ($n=1$).** $H_1=1$. RHS $=\ln1+1=0+1=1$.
    So $H_1\le\ln1+1$.

    **Inductive hypothesis.** Assume $H_n\le\ln n+1$ for
    some $n\ge1$.

    **Inductive step.** We show $H_{n+1}\le\ln(n+1)+1$.

    By definition, $H_{n+1}=H_n+\dfrac{1}{n+1}$. By the
    inductive hypothesis,
    $$H_{n+1} \le \ln n+1+\frac{1}{n+1}.$$
    It remains to show $\ln n+\dfrac{1}{n+1}\le\ln(n+1)$, i.e.
    $$\ln(n+1)-\ln n \ge \frac{1}{n+1}.$$
    Using the inequality $\ln x \ge 1-\dfrac1x$ for $x>0$, take
    $x=\dfrac{n+1}{n}$:
    $$\ln\left(\frac{n+1}{n}\right) \ge 1-\frac{n}{n+1}
                = \frac{1}{n+1}.$$
    Since $\ln\left(\dfrac{n+1}{n}\right)=\ln(n+1)-\ln n$, this
    gives
    $$\ln(n+1)-\ln n \ge \frac{1}{n+1}.$$
    Combining:
    $$H_{n+1} \le \ln n+1+\frac{1}{n+1} \le \ln(n+1)+1.$$
    So the statement holds for $n+1$.

    **Conclusion.** By the Principle of Mathematical
    Induction, $H_n \le \ln n+1$ for all $n\ge1$.

    :::
:::
