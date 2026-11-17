<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 4 (source key cs70-4, in note.md). The first instance is our own; checked by a short program. -->

::: {#exm-propose-and-reject-run .example name="A run of propose-and-reject" level="easy"}
Jobs $1,2,3$ and candidates $a,b,c$, each list from most to least preferred:

| Job | List | | Candidate | List |
|---|---|---|---|---|
| $1$ | $a,b,c$ | | $a$ | $3,2,1$ |
| $2$ | $a,c,b$ | | $b$ | $1,3,2$ |
| $3$ | $b,a,c$ | | $c$ | $2,1,3$ |

| Day | Offers to $a$ | Offers to $b$ | Offers to $c$ | Rejected |
|---|---|---|---|---|
| 1 | $1,2$ | $3$ | — | $1$ by $a$ |
| 2 | $2$ | $1,3$ | — | $3$ by $b$ |
| 3 | $2,3$ | $1$ | — | $2$ by $a$ |
| 4 | $3$ | $1$ | $2$ | none |

The output is $\{(1,b),(2,c),(3,a)\}$. Candidate $a$ trades up twice, as @lem-improvement predicts. Job $2$ ends with its second choice $c$; it cannot get $a$, who prefers her partner $3$. Checking all six matchings shows this is the only stable one.
:::

::: {#exm-two-stable-matchings .example name="Two stable matchings" level="medium"}
Four jobs and four candidates:

| Job | List | | Candidate | List |
|---|---|---|---|---|
| $1$ | $A,B,C,D$ | | $A$ | $1,3,2,4$ |
| $2$ | $A,D,C,B$ | | $B$ | $4,3,2,1$ |
| $3$ | $A,C,B,D$ | | $C$ | $2,3,1,4$ |
| $4$ | $A,B,C,D$ | | $D$ | $3,4,2,1$ |

Exactly two of the $24$ matchings are stable:
$$S=\{(1,A),(2,D),(3,C),(4,B)\},\qquad T=\{(1,A),(2,C),(3,D),(4,B)\}.$$
Job $2$ ranks $A$ first, but no stable matching pairs them, so its optimal candidate is $D$, its partner in $S$. In fact $S$ is job-optimal and $T$ is candidate-optimal. With the jobs proposing, all four jobs make their offer to $A$ on day 1, $A$ keeps $1$, and on day 2 the offers $2\to D$, $3\to C$, $4\to B$ are all held, so the algorithm outputs $S$ (@thm-job-optimal). By @thm-job-optimal-candidate-pessimal, $S$ is candidate-pessimal: $C$ and $D$ each prefer their partner in $T$.
:::

::: {#exm-roommates-no-stable .example name="Roommates without a stable pairing" level="medium"}
Four people $A,B,C,D$ must be split into two pairs. The lists are $A: B,C,D$; $B: C,A,D$; $C: A,B,D$; and $D$ has any list. No pairing is stable.

1. Whoever is paired with $D$ is one of $A,B,C$, and ranks $D$ last.

2. Among $A,B,C$, each person is the first choice of exactly one other: $B$ of $A$, $C$ of $B$, $A$ of $C$. Let $x$ be the partner of $D$, and $y$ the person whose first choice is $x$.

3. $y$ is not paired with $x$, so $y$ prefers $x$ to its partner; and $x$ prefers $y$ to $D$. So $(x,y)$ is a rogue couple.

For example, in $\{(A,B),(C,D)\}$ the rogue couple is $(B,C)$, and in $\{(A,D),(B,C)\}$ it is $(A,C)$.
:::
