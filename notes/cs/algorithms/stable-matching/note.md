---
title: "Stable Matching"
sources: [cs70-4]
requires: [math/discrete/proof/induction]
status: draft
---

<!-- Added 2026-11-17 from CS70 Note 4 (cs70-4), in our own wording; proofs written out in steps. -->

## The problem

::: {#def-stable-matching .definition name="Stable matching"}

An *instance* consists of $n$ jobs, $n$ candidates, and for each job a strict ranking of all candidates and for each candidate a strict ranking of all jobs (its *preference list*). A *matching* is a set of $n$ pairs (job, candidate) in which every job and every candidate occurs exactly once.

In a matching $M$, a job $J$ and a candidate $C$ that are not paired with each other form a *rogue couple* if $J$ prefers $C$ to its partner in $M$ and $C$ prefers $J$ to her partner in $M$. A matching is *stable* if it has no rogue couple.

:::

::: {#fig-stable-matching-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=0.85cm]
\foreach \j/\y in {1/2,2/1,3/0} \node[vertex] (j\j) at (0,\y) {$\j$};
\foreach \c/\y in {a/2,b/1,c/0} \node[vertex] (c\c) at (3,\y) {$\c$};
\node[lab] at (0,2.8) {jobs};
\node[lab] at (3,2.8) {candidates};
\draw[emph] (j1)--(cc) (j2)--(cb) (j3)--(ca);
\draw[hl, dashed] (j1)--(cb);
\end{tikzpicture}
\end{center}
```

The matching $\{(1,c),(2,b),(3,a)\}$ for the lists of @exm-propose-and-reject-run is not stable: job $1$ prefers $b$ to $c$, and $b$ prefers $1$ to $2$, so $(1,b)$ is a rogue couple (dashed).

:::

::: {#rmk-stable-matching-existence}

It is not obvious that a stable matching always exists. Repeatedly pairing up a rogue couple removes that couple but may create new ones, so this procedure need not stop. For the *roommates problem*, where $2n$ people of one type are paired with each other, there are instances with no stable matching at all (@exm-roommates-no-stable). So an existence proof must use the fact that there are two different types. The proof below is an algorithm.

:::

## The propose-and-reject algorithm

::: {#def-propose-and-reject .definition name="Propose-and-reject (Gale–Shapley) algorithm"}

The algorithm runs in days. Each job keeps a list of the candidates who have not rejected it, in its order of preference.

1. *Morning:* each job with a non-empty list makes an offer to the first candidate on its list.

2. *Afternoon:* each candidate who received offers keeps the one she likes best "on a string" and rejects all the others.

3. *Evening:* each rejected job crosses the candidate who rejected it off its list.

The algorithm stops on the first day with no rejection; then each candidate accepts the offer she holds.

:::

::: {#lem-propose-and-reject-halts .lemma name="The algorithm halts"}

The algorithm stops after at most $n^2+1$ days.

:::

::: {.proof}

1. On every day except the last, some offer is rejected, so some job crosses at least one candidate off its list.

2. Nothing is ever added to a list, and the $n$ lists hold $n^2$ entries at the start.

3. So there are at most $n^2$ days with a rejection, and the algorithm stops by day $n^2+1$.

:::

::: {#lem-improvement .lemma name="Improvement lemma"}

If job $J$ makes an offer to candidate $C$ on day $k$, then at the end of every day $i\ge k$, $C$ holds an offer from a job she likes at least as much as $J$.

:::

::: {.proof}

We use induction on $i\ge k$ (@sec-math-discrete-proof-induction).

1. *Base case $i=k$.* On day $k$, $C$ receives at least the offer of $J$. She keeps the best offer she receives, so at the end of day $k$ she holds $J$ or a job she likes more.

2. *Inductive step.* Suppose that at the end of day $i$, $C$ holds an offer from $J'$, and she likes $J'$ at least as much as $J$ ($J'$ may be $J$).

3. $C$ did not reject $J'$, so $C$ is still first on the list of $J'$, and $J'$ makes its offer to $C$ again on day $i+1$.

4. So at the end of day $i+1$, $C$ holds $J'$ or a job she likes more than $J'$. In both cases she likes it at least as much as $J$.

:::

The same proof can be phrased with the least counterexample: if day $i>k$ were the first day on which $C$ held nothing as good as $J$, the job she held on day $i-1$ would make its offer to her again on day $i$, a contradiction. This uses @def-well-ordering-property; compare @thm-well-ordering-mathematical-induction.

::: {#lem-propose-and-reject-matching .lemma name="The output is a matching"}

When the algorithm stops, every job is held by exactly one candidate, so the held offers form a matching.

:::

::: {.proof}

1. Each candidate holds at most one offer, and each job makes at most one offer per day, so on the last day the held offers come from distinct jobs.

2. Suppose, for contradiction, that some job $J$ is not held on the last day. If its list were non-empty, $J$ made an offer that day and was not rejected (there were no rejections), so it would be held. Hence $J$ has crossed off all $n$ candidates: each of them rejected $J$.

3. Each candidate received an offer from $J$ on some day, so by @lem-improvement every one of the $n$ candidates holds an offer on the last day.

4. By step 1 these are offers from $n$ distinct jobs, none of them $J$. Together with $J$ that makes $n+1$ jobs, a contradiction.

5. So all $n$ jobs are held, by distinct candidates (step 1), and every candidate holds exactly one of them.

:::

::: {#thm-propose-and-reject-stable .theorem name="The output is stable"}

The matching produced by the propose-and-reject algorithm is stable. In particular, every instance has a stable matching.

:::

::: {.proof}

1. Let $(J,C)$ be a pair of the output, and let $C^*$ be a candidate whom $J$ prefers to $C$. Every rogue couple has this form, so it suffices to show that $(J,C^*)$ is not one.

2. $J$ makes offers in the order of its list, so it made an offer to $C^*$ before its offer to $C$, and $C^*$ rejected it.

3. By @lem-improvement, at the end $C^*$ holds a job she likes at least as much as $J$. That job is not $J$, which is held by $C$, and preferences are strict, so $C^*$ prefers her partner to $J$.

4. So $(J,C^*)$ is not a rogue couple, and the matching is stable. Existence follows from @lem-propose-and-reject-halts and @lem-propose-and-reject-matching.

:::

## Who is better off

::: {#def-optimal-partner .definition name="Optimal and pessimal partners"}

For a job $J$, its *optimal candidate* is the candidate highest on its list among all candidates paired with $J$ in some stable matching; its *pessimal candidate* is the lowest such candidate. A stable matching is *job-optimal* if every job is paired with its optimal candidate, and *job-pessimal* if every job is paired with its pessimal candidate. Optimal and pessimal jobs of a candidate, and *candidate-optimal* and *candidate-pessimal* matchings, are defined in the same way.

:::

By @thm-propose-and-reject-stable, stable matchings exist, so every job and every candidate has an optimal and a pessimal partner. That all jobs reach their optimal candidates *at the same time* is not obvious; the next theorem shows it.

::: {#thm-job-optimal .theorem name="The proposers get their best stable partners"}

The matching produced by the propose-and-reject algorithm is job-optimal.

:::

::: {.proof}

1. First suppose that no job is ever rejected by its optimal candidate. A job $J$ makes offers down its list and ends with the first candidate who never rejects it; its optimal candidate never rejects it, so $J$ ends with its optimal candidate or someone it likes more. The output is stable (@thm-propose-and-reject-stable), so the partner of $J$ is no better than its optimal candidate. Hence $J$ ends with exactly its optimal candidate.

2. So suppose, for contradiction, that some job is rejected by its optimal candidate on some day. By @def-well-ordering-property there is a first such day $k$. On day $k$, let $C^*$ be the optimal candidate of $J$, and suppose she rejects $J$ for an offer from $J^*$.

3. By the definition of the optimal candidate, there is a stable matching $T$ with $(J,C^*)\in T$. Let $C'$ be the partner of $J^*$ in $T$; $C'\ne C^*$, since $C^*$ is paired with $J$.

4. $C^*$ prefers $J^*$ to $J$, because she rejected $J$ in favour of $J^*$.

5. $J^*$ makes its offer to $C^*$ on day $k$, so every candidate above $C^*$ on its list rejected $J^*$ before day $k$. Since $k$ is the first day on which a job is rejected by its optimal candidate, none of them is the optimal candidate of $J^*$. So $J^*$ likes $C^*$ at least as much as its optimal candidate.

6. $C'$ is a partner of $J^*$ in a stable matching, so $J^*$ likes its optimal candidate at least as much as $C'$. With step 5 and $C'\ne C^*$, $J^*$ prefers $C^*$ to $C'$.

7. By steps 4 and 6, $(J^*,C^*)$ is a rogue couple in $T$, which contradicts the stability of $T$.

:::

::: {#thm-job-optimal-candidate-pessimal .theorem name="Job-optimal is candidate-pessimal"}

A job-optimal stable matching is candidate-pessimal.

:::

::: {.proof}

1. Let $T$ be job-optimal, and let $(J,C)\in T$. We show that $C$ likes her partner in every stable matching at least as much as $J$, so $J$ is her pessimal job.

2. Suppose, for contradiction, that $S$ is a stable matching in which $C$ is paired with a job $J^*$ she likes less than $J$. Let $C'$ be the partner of $J$ in $S$; $C'\ne C$, since $C$ is paired with $J^*\ne J$.

3. $C$ prefers $J$ to $J^*$, by assumption.

4. $C$ is the optimal candidate of $J$ and $C'$ is a partner of $J$ in the stable matching $S$, so $J$ likes $C$ at least as much as $C'$, and strictly more because $C'\ne C$.

5. So $(J,C)$ is a rogue couple in $S$, which contradicts the stability of $S$.

:::

::: {#rmk-stable-matching-proposers}

The proofs only use which side makes the offers: the algorithm is optimal for the proposing side and pessimal for the other. Running it with the candidates proposing gives the candidate-optimal (and job-pessimal) matching. The US National Resident Matching Program has matched medical graduates to hospitals with this algorithm since the early 1950s, at first with the hospitals proposing; in the 1990s the roles were reversed. Gale and Shapley analysed the algorithm in 1962, and Shapley and Roth received the 2012 Nobel Prize in Economic Sciences for work built on it.

:::
