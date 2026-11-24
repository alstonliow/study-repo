<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-propositional-03"}
1. Apply the first law to $\neg P$ and $\neg Q$:
   $$\neg(\neg P\vee\neg Q) = \neg\neg P\wedge\neg\neg Q = P\wedge Q.$$

2. Negate both sides:
   $$\neg\neg(\neg P\vee\neg Q) = \neg(P\wedge Q),$$
   that is, $\neg P\vee\neg Q = \neg(P\wedge Q)$.
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-1-q2" status="draft"}
List the rows $PQR$ from TTT to FFF.

(a) True. The left side is true exactly when $P$ is false and $Q\land R$ is false, i.e. in the rows FTF, FFT, FFF; the right side is true when $P$ is false and at least one of $Q,R$ is false, the same three rows. (By De Morgan, $\lnot(P\lor(Q\land R))\equiv\lnot P\land\lnot(Q\land R)\equiv\lnot P\land(\lnot Q\lor\lnot R)$.)

| $P\,Q\,R$ | TTT | TTF | TFT | TFF | FTT | FTF | FFT | FFF |
|---|---|---|---|---|---|---|---|---|
| (a) left | F | F | F | F | F | T | T | T |
| (a) right | F | F | F | F | F | T | T | T |
| (b) left | F | F | F | T | T | T | T | T |
| (b) right | F | T | T | T | T | T | T | T |

(b) False. In the row $P=Q=\text{T}$, $R=\text{F}$: $Q\lor R$ is true, so the left side is $\lnot(\text{T})=\text{F}$, while $\lnot R$ is true, so the right side is T. (The correct law is $\lnot(P\land(Q\lor R))\equiv\lnot P\lor(\lnot Q\land\lnot R)$.)
:::
