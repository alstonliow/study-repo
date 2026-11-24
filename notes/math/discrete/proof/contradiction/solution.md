<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-proofs-14"}
1. Lines 3–8 are a correct proof that $\mathbb Z\subseteq\mathbb Q$.

2. Line 9 says "the superset relation", but to prove $\mathbb Z = \mathbb Q$
   we need $\mathbb Z\supseteq\mathbb Q$, i.e. $\mathbb Q\subseteq\mathbb Z$.

3. Line 10 instead sets out to prove $\mathbb Q\supseteq\mathbb Z$. That is
   the same statement as $\mathbb Z\subseteq\mathbb Q$, just written from
   the other side, so nothing new is proved.

4. Lines 11–14 are a correct argument: they show that a number outside
   $\mathbb Q$ is outside $\mathbb Z$. This is the contrapositive of
   $\mathbb Z\subseteq\mathbb Q$, which again is the statement of line 8.

5. Line 16 concludes $\mathbb Z = \mathbb Q$ from two statements that are
   really one and the same, so the conclusion does not follow. Indeed it is
   false: $\frac12\in\mathbb Q\setminus\mathbb Z$.
:::

::: {.solution for="prob-cs70-2-q2"}
<!-- TODO: solution -->
:::

<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-2-q1" status="draft"}
The numbers are distinct, so every comparison is strict.

(a) If $a_3>a_2$, then $a_1<a_2<a_3$ is a 3-chain. So $a_3<a_2$. Suppose $a_1<a_3<a_2$. If $a_4>a_3$, then $a_1<a_3<a_4$ is a 3-chain; if $a_4<a_3$, then $a_2>a_3>a_4$ is one. Both are impossible, so $a_3<a_1$.

(b) Now $a_3<a_1<a_2$. If $a_4>a_2$, then $a_1<a_2<a_4$ is a 3-chain. If $a_4<a_3$, then $a_1>a_3>a_4$ is one. So $a_3<a_4<a_2$.

(c) If $a_5>a_4$, then $a_3<a_4<a_5$ is a 3-chain; if $a_5<a_4$, then $a_2>a_4>a_5$ is one.

(d) Suppose, for contradiction, that some sequence of five distinct integers has no 3-chain. If $a_1<a_2$, parts (a)–(c) produce a 3-chain, a contradiction. If $a_1>a_2$, the sequence $-a_1,\dots,-a_5$ has $-a_1<-a_2$, so it contains a 3-chain; its negation is a 3-chain of the original sequence (increasing and decreasing swap), again a contradiction.
:::
