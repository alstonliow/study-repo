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
    holds for all $n\ge1$.
:::

::: {.solution for="prob-proofs-11"}
The $n$-th harmonic number $H_n$ is defined by
$$H_n = 1+\frac12+\frac13+\cdots+\frac1n.$$

**Main result:** $H_n \ge \ln(n+1)$ for all $n\ge1$.

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

**Advanced afterthoughts.**

1.  The inequality $H_n\ge\ln(n+1)$ implies $H_n\ge\ln n$, since
    $\ln(n+1)\ge\ln n$. Trying to prove $H_n\ge\ln n$ *directly*
    by induction runs into a snag: in the inductive step, one would
    need
    $$\ln(n+1)-\ln n = \ln\left(1+\frac1n\right) \le \frac{1}{n+1},$$
    but $\ln(1+x)\le x$ only gives the weaker bound
    $\ln(1+\frac1n)\le\frac1n$, which is not tight enough (since
    $\frac1n > \frac{1}{n+1}$). In fact the needed inequality is
    false: $\ln(1+x)\ge\frac{x}{1+x}$ gives
    $\ln\left(1+\frac1n\right)\ge\frac{1}{n+1}$, with equality
    never attained for $n\ge1$. This illustrates that induction
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

::: {.solution for="prob-cs70-3-q2"}
<!-- TODO: solution -->
:::

::: {.solution for="prob-cs70-3-q3"}
<!-- TODO: solution -->
:::

::: {.solution for="prob-cs70-3-q4"}
<!-- TODO: solution -->
:::

::: {.solution for="prob-cs70-3-q5"}
<!-- TODO: solution -->
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-2-q2" status="draft"}
Pacman's positions are the points $(i,j)$ with $i,j\le0$. Let $d(i,j)=-i-j\ge0$, his taxicab distance to the origin. We prove by induction on $d$: *from any position with $d(i,j)=d$, every walk reaches $(0,0)$ after exactly $d$ seconds.*

1. *Base case $d=0$:* the only such position is $(0,0)$ itself.

2. *Inductive step:* let $d(i,j)=d+1\ge1$, so $(i,j)\ne(0,0)$. If $i<0$ he can step right; if $j<0$ he can step up. So he is never stuck, and every move is one of these two.

3. Each move increases $i$ or $j$ by $1$ and stays in the quadrant, so after one second he is at a position with distance $d$. By the hypothesis, from there every walk reaches $(0,0)$ after exactly $d$ more seconds: $d+1$ in all.
:::

::: {.solution for="prob-cs70hw-2-q3" status="draft"}
Give a blue marble weight $1$, a green one $4$ and a red one $13$, and let $W=13R+4G+B$ be the total weight.

1. Every move lowers $W$ by exactly $1$: move (i) changes it by $-13+3\cdot4$, move (ii) by $-2\cdot4+7$, move (iii) by $-1$.

(b) By induction on the number $m$ of moves made, the weight after $m$ moves is $W_0-m$, where $W_0$ is the starting weight: true for $m=0$, and each further move subtracts $1$ (step 1). Weights are never negative, so at most $W_0$ moves can be made, and the game ends.

(a)

2. The game ends exactly when no move is legal: no red and no blue marble, and at most one green. So the final weight is $0$ or $4$, an even number in both cases.

3. By (b), the number of moves played is $W_0-W_{\text{end}}$, which has the parity of $W_0=13R+4G+B$, that is, of $R+B$.

4. The first player makes the last move exactly when the number of moves is odd. So **the first player wins if and only if $R+B$ is odd**, and the strategy does not matter: every sequence of legal moves has the same parity of length.
:::

::: {.solution for="prob-mit6006s20-0-q4" status="draft"}
Let $P(n)$ be the claimed identity.

1. *Base case* $n=1$: both sides equal $1$.

2. *Inductive step.* Assume $P(n)$ for some $n\ge1$. Then
   $$\sum_{i=1}^{n+1}i^3=\frac{n^2(n+1)^2}4+(n+1)^3=\frac{(n+1)^2\bigl(n^2+4n+4\bigr)}4=\left[\frac{(n+1)(n+2)}2\right]^2,$$
   which is $P(n+1)$.

3. By induction, $P(n)$ holds for all $n\ge1$.
:::
