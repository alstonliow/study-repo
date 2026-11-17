<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-probability-2-04 origin="external" source="fit1058-cn-10.12-q4"}
You need a die but don’t have one. Your friend suggests tossing five fair
coins, counting the Heads (in $\{0,\dots,5\}$) and adding one to get a number
in $\{1,\dots,6\}$. Discuss this suggestion. Can you think of any other way
in which a set of fair coins (possibly more than six) can be used to simulate
the throw of a fair die?
:::

::: {.problem #prob-probability-2-07 origin="external" source="fit1058-cn-10.12-q7"}
Suppose $X\sim\mathrm{Bin}(16,0.5)$.

(a) Your friend claims that, because $p=\frac12$, half the trials must
    be successes and half failures. What is the probability that this
    actually happens?

(b) What is the probability that $X$ is at least two standard
    deviations away from the mean?

(c) What is the probability that $X$ is at least three standard
    deviations away from the mean?

(d) How do these exact probabilities compare with the bounds given by
    Chebyshev’s Theorem?
:::

::: {.problem #prob-cs70hw-11-q3 origin="external" source="cs70hw-11-q3"}
**Testing Model Planes.** Amin is testing model airplanes. He starts with $n$ model planes which each independently have probability $p$ of flying successfully each time they are flown, where $0 < p < 1$. Each day, he flies every single plane and keeps the ones that fly successfully (i.e. don't crash), throwing away all other models. He repeats this process for many days, where each "day" consists of Amin flying any remaining model planes and throwing away any that crash. Let $X_i$ be the random variable representing how many model planes remain after $i$ days. Note that $X_0 = n$. Justify your answers for each part.

(a) What is the distribution of $X_1$? That is, what is $P[X_1 = k]$?

(b) What is the distribution of $X_2$? That is, what is $P[X_2 = k]$? Name the distribution of $X_2$ and what its parameters are.

(c) Repeat the previous part for $X_t$ for arbitrary $t \ge 1$.

(d) What is the probability that at least one model plane still remains (has not crashed yet) after $t$ days? Do not have any summations in your answer.

(e) Considering only the first day of flights, is the event $A_1$ that the first and second model planes crash independent from the event $B_1$ that the second and third model planes crash? Recall that two events $A$ and $B$ are independent if $P[A \cap B] = P[A]P[B]$. Prove your answer using this definition.

(f) Considering only the first day of flights, let $A_2$ be the event that the first model plane crashes and exactly two model planes crash in total. Let $B_2$ be the event that the second plane crashes on the first day. What must $n$ be equal to in terms of $p$ such that $A_2$ is independent from $B_2$? Prove your answer using the definition of independence stated in the previous part.

(g) Are the random variables $X_i$ and $X_j$, where $i < j$, independent? Recall that two random variables $X$ and $Y$ are independent if $P[X = k_1 \cap Y = k_2] = P[X = k_1]P[Y = k_2]$ for all $k_1$ and $k_2$. Prove your answer using this definition.
:::
