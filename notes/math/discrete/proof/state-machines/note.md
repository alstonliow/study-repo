---
title: "State Machines and Invariants"
sources: [mcs-5.4]
requires: [math/discrete/proof/well-ordering-proofs]
status: draft
---

<!-- Added 2026-11-17 from MIT 6.042J, Mathematics for Computer Science (2015), Section 5.4, in our own wording; the examples are our own versions; proofs written out in steps. -->

## States and transitions

::: {#def-state-machine .definition name="State machine"}

A *state machine* consists of a set $Q$ of *states*, a *start state* $q_0\in Q$, and a binary relation $\to$ on $Q$, the *transition relation*. A *transition* is a pair $q\to r$. An *execution* is a finite or infinite sequence $q_0,q_1,q_2,\dots$ that begins at the start state with $q_i\to q_{i+1}$ for every $i$. A state is *reachable* if it occurs in some execution. A state with no outgoing transition is *final*.

:::

::: {#exm-state-machine-counter .example name="A bounded counter"}

States $\{0,1,\dots,99,\text{overflow}\}$, start state $0$, transitions $n\to n+1$ for $0\le n<99$, and $99\to\text{overflow}\to\text{overflow}$. Its only infinite execution counts up to $99$ and then stays in overflow forever.

:::

## The invariant principle

::: {#def-preserved-invariant .definition name="Preserved invariant"}

A predicate $P$ on states is a *preserved invariant* of a state machine if $P(q)$ and $q\to r$ imply $P(r)$.

:::

::: {#thm-invariant-principle .theorem name="Invariant principle"}

If $P$ is a preserved invariant and $P(q_0)$ holds for the start state, then $P$ holds for every reachable state.

:::

::: {.proof}

1. Let $q_0,q_1,\dots$ be an execution. We show $P(q_i)$ for all $i$ by induction on $i$ (@sec-math-discrete-proof-induction).

2. *Base case:* $P(q_0)$ holds by assumption.

3. *Step:* if $P(q_i)$ holds, then $q_i\to q_{i+1}$ and preservation give $P(q_{i+1})$.

4. Every reachable state occurs in some execution, so $P$ holds there.

:::

The invariant need not be the property we care about; often it is a stronger statement that is easier to carry from step to step.

::: {#exm-diagonal-robot .example name="A robot that moves diagonally"}

A robot on the integer grid starts at $(0,0)$ and at each step moves to one of $(x\pm1,y\pm1)$. It can never reach $(1,0)$.

1. Let $P(x,y)$ be "$x+y$ is even". It holds at $(0,0)$.

2. A move changes $x+y$ by $-2$, $0$ or $+2$, so it preserves the parity of $x+y$: $P$ is a preserved invariant.

3. By @thm-invariant-principle every reachable position has $x+y$ even, and $1+0$ is odd.

:::

::: {#exm-water-jugs .example name="Two water jugs"}

A $3$-litre and a $5$-litre jug, with unlimited water. A state $(a,b)$ gives the contents. The moves are: fill a jug, empty a jug, or pour one jug into the other until the first is empty or the second is full. Start at $(0,0)$.

1. *Invariant:* $a$ and $b$ are always integer combinations of $3$ and $5$, i.e. elements of $\{3s+5t:s,t\in\mathbb Z\}$. This holds at $(0,0)$, and each move replaces amounts by sums or differences of current amounts and of $0$, $3$, $5$, which stay in this set. Since $\gcd(3,5)=1$, the invariant says nothing here; for jugs of $6$ and $9$ litres it shows that every reachable amount is a multiple of $3$, so $4$ litres can never be measured.

2. With $3$ and $5$, the execution $(0,0)\to(0,5)\to(3,2)\to(0,2)\to(2,0)\to(2,5)\to(3,4)$ leaves $4$ litres in the large jug.

In general, with jugs of $a$ and $b$ litres, the reachable amounts are exactly the multiples of $\gcd(a,b)$ up to $\max(a,b)$; the invariant gives one direction (@thm-bezout).

:::

## Correctness and termination

A program, viewed as a state machine, is *partially correct* if every final state it reaches is correct, and it *terminates* if every execution is finite. Partial correctness is proved with an invariant; termination with a decreasing quantity.

::: {#def-derived-variable .definition name="Derived variable"}

A *derived variable* is a function $v:Q\to S$ from states to some set. It is *strictly decreasing* if $q\to r$ implies $v(r)<v(q)$, and *weakly decreasing* if $q\to r$ implies $v(r)\le v(q)$.

:::

::: {#thm-strictly-decreasing-terminates .theorem name="A decreasing natural number stops a machine"}

If a state machine has a strictly decreasing derived variable with values in $\mathbb N$, then every execution is finite; in fact an execution starting at $q_0$ has at most $v(q_0)$ transitions.

:::

::: {.proof}

1. Along an execution $q_0,q_1,\dots$, the values satisfy $v(q_0)>v(q_1)>\cdots$, so $v(q_i)\le v(q_0)-i$ by induction on $i$.

2. Values are natural numbers, so $v(q_0)-i\ge0$, that is, $i\le v(q_0)$ for every state $q_i$ of the execution. So it has at most $v(q_0)$ transitions.

:::

The same holds with values in any well-ordered set (@sec-math-discrete-proof-well-ordering-proofs), though without the bound on the length.

::: {#exm-fast-exponentiation-machine .example name="Fast exponentiation"}

To compute $a^b$ for $b\in\mathbb N$, use states $(x,y,z)$ with start $(a,1,b)$ and, while $z>0$, the transitions
$$(x,y,z)\to\begin{cases}(x^2,\ y,\ z/2)&z\text{ even},\\(x^2,\ xy,\ (z-1)/2)&z\text{ odd}.\end{cases}$$

1. *Invariant:* $y\,x^z=a^b$. It holds at the start ($1\cdot a^b$). If $z$ is even, $y(x^2)^{z/2}=yx^z$; if $z$ is odd, $(xy)(x^2)^{(z-1)/2}=yx^z$. So it is preserved.

2. *Partial correctness:* the machine stops when $z=0$, and then the invariant gives $y=a^b$.

3. *Termination:* $z$ is a natural number and strictly decreases when $z>0$ (it at least halves). By @thm-strictly-decreasing-terminates the machine stops; in fact after $\lfloor\log_2b\rfloor+1$ steps for $b\ge1$, since $z$ halves each time.

This is the repeated squaring of @sec-math-discrete-number-theory-modular-exponentiation, read right to left.

:::

::: {#rmk-state-machines-stable-matching .remark name="Stable matching as a state machine"}

The propose-and-reject algorithm (@def-propose-and-reject) is a state machine whose state records each job's remaining list and the offer each candidate holds. The improvement lemma is an invariant ("each candidate holds an offer at least as good as any she has rejected"), and the total length of the jobs' lists is a strictly decreasing derived variable, which is the termination proof of @lem-propose-and-reject-halts.

:::
