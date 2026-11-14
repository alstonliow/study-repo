<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

<!-- Migrated from 1058note exercises/chapters (owner's solutions). -->

::: {.solution for="prob-propositional-19"}
::: {.proof}

**Part 1: Induction on $n$.**

*Base case ($n=1$).* With two inputs $x_1,x_2$, a single AND gate computes $x_1\wedge x_2$ in time $t = 1\cdot t$. So the claim holds for $n=1$.

*Inductive step.* Assume the conjunction of $2^n$ inputs can be computed in time $nt$ by a suitable combination of AND gates.

Now suppose we have $2^{n+1}=2\cdot 2^n$ inputs $x_1,\dots,x_{2^{n+1}}$. Split them into two blocks of $2^n$ inputs each:
$$(x_1\wedge\cdots\wedge x_{2^n}) \quad\text{and}\quad (x_{2^n+1}\wedge\cdots\wedge x_{2^{n+1}}).$$

By the inductive hypothesis, each block can be computed in time $nt$ (in parallel, since the two blocks use disjoint inputs). After time $nt$, we have exactly two values available, and a single additional AND gate combines them, taking a further time $t$.

Hence the total time is
$$nt + t = (n+1)t.$$

By induction, the conjunction of $2^n$ inputs can be computed in time $nt$ for all $n\geq 1$.

**Part 2: General $m$.**

*Case 1: $m=2^n$ for some $n$.* Then $\log_2 m = n$, so $\lceil\log_2 m\rceil = n$, and by Part 1 the total time is $nt = \lceil\log_2 m\rceil\, t$, as required.

*Case 2: $m$ is not a power of $2$.* Let
$$k = \lceil \log_2 m\rceil, \qquad M = 2^k.$$

Since $k\geq \log_2 m$ and $x\mapsto 2^x$ is increasing,
$$2^k \geq 2^{\log_2 m} = m, \qquad\text{i.e.}\qquad M\geq m.$$

We have $m$ real inputs $x_1,\dots,x_m$, with $m < M$. Pad the input list with $M-m$ copies of the constant [True]{.sans-serif}:
$$x_1\wedge\cdots\wedge x_m\wedge\underbrace{\mathsf{True}\wedge\cdots\wedge\mathsf{True}}_{M-m}.$$

Since $P\wedge\mathsf{True}\equiv P$ for any proposition $P$, this padded conjunction is logically equivalent to the original one:
$$x_1\wedge\cdots\wedge x_m\wedge\underbrace{\mathsf{True}\wedge\cdots\wedge\mathsf{True}}_{M-m} \;\equiv\; x_1\wedge\cdots\wedge x_m.$$

The padded expression has exactly $M=2^k$ inputs, so by Part 1 it can be computed by a suitable combination of AND gates in time
$$kt = \lceil\log_2 m\rceil\, t.$$

Since the padded expression is equivalent to $x_1\wedge\cdots\wedge x_m$, the same circuit computes $x_1\wedge\cdots\wedge x_m$ in time $\lceil\log_2 m\rceil\, t$.

Combining both cases, for every $m\geq 1$ the conjunction of $m$ arguments can be computed by a suitable combination of AND gates in time $\lceil\log_2 m\rceil\, t$.

:::
:::

::: {.solution for="prob-propositional-22"}
By Exercise 20, any affine expression (i.e. any expression built from $\oplus,\neg$, using $\neg P\equiv P\oplus\text{True}$) in $n$ variables has exactly $2^{n-1}$ satisfying assignments.

$$\begin{array}{cc|c}
x_1 & x_2 & x_1\vee x_2\\
\hline
0&0&0\\
0&1&1\\
1&0&1\\
1&1&1
\end{array}
\qquad
\begin{array}{cc|c}
x_1 & x_2 & x_1\wedge x_2\\
\hline
0&0&0\\
0&1&0\\
1&0&0\\
1&1&1
\end{array}$$

$x_1\vee x_2$ has $3$ satisfying assignments; $x_1\wedge x_2$ has $1$. Neither equals $2^{2-1}=2$, so $\wedge,\vee$ cannot be expressed correctly by $\{\oplus,\neg\}$.

Hence $\{\oplus,\neg\}$ is **not** a universal set of operations.
:::

::: {.solution for="prob-propositional-24"}
**(a)** By De Morgan’s law,
$$\neg a\vee\neg b \equiv \neg(a\wedge b) \equiv a\ \text{NAND}\ b.$$
So the circuit (two NOT gates feeding a NOR gate) is equivalent to a single **NAND gate**.

**(b)** XOR outputs true exactly when $a,b$ differ:
$$a\oplus b \equiv (a\wedge\neg b)\vee(\neg a\wedge b).$$

**(d)** We show $\vee$ can be expressed using only $\wedge,\neg$, and $\wedge$ can be expressed using only $\vee,\neg$; since $\{\wedge,\vee,\neg\}$ is universal, this shows $\{\wedge,\neg\}$ and $\{\vee,\neg\}$ are each universal.

Using double negation ($\neg\neg P\equiv P$) and De Morgan’s law:
$$a\vee b \equiv \neg\neg(a\vee b) \equiv \neg(\neg a\wedge\neg b),$$
which expresses $\vee$ using only $\wedge$ and $\neg$. Hence $\{\wedge,\neg\}$ is a universal set of operations.

$$a\wedge b \equiv \neg\neg(a\wedge b) \equiv \neg(\neg a\vee\neg b),$$
which expresses $\wedge$ using only $\vee$ and $\neg$. Hence $\{\vee,\neg\}$ is a universal set of operations.

**(f)** We show every operation in $\{\wedge,\vee,\neg\}$ can be built from NAND alone.

*NOT:*
$$\neg a \equiv \neg a\vee\neg a \equiv \neg(a\wedge a) \equiv a\ \text{NAND}\ a.$$

*OR:*
$$a\vee b \equiv \neg\neg(a\vee b) \equiv \neg(\neg a\wedge\neg b) \equiv \neg a\ \text{NAND}\ \neg b \equiv (a\ \text{NAND}\ a)\ \text{NAND}\ (b\ \text{NAND}\ b).$$

*AND:*
$$a\wedge b \equiv \neg\big(\neg(a\wedge b)\big) \equiv \neg(a\ \text{NAND}\ b) \equiv (a\ \text{NAND}\ b)\ \text{NAND}\ (a\ \text{NAND}\ b).$$

Since NAND alone can express $\wedge,\vee,\neg$, and $\{\wedge,\vee,\neg\}$ is universal, the single operation NAND is itself a **universal (functionally complete) operation**: every Boolean circuit can, in principle, be built using nothing but NAND gates.
:::

::: {.solution for="prob-propositional-18" status="draft"}
Each 2-input gate reduces the number of values still to be combined by one.
Starting from $8$ inputs and ending with $1$ output takes exactly $7$ gates,
whatever the arrangement.

- *Chain:* $((((((x_1\wedge x_2)\wedge x_3)\wedge x_4)\cdots)\wedge x_8)$.
  Each gate waits for the previous one, so it takes $7t$.

- *Balanced tree:* in the first layer, $4$ gates compute $x_1\wedge x_2$,
  $x_3\wedge x_4$, $x_5\wedge x_6$, $x_7\wedge x_8$ in parallel. The second
  layer combines these with $2$ gates, and the third with $1$ gate. That is
  still $4 + 2 + 1 = 7$ gates, but the time is $3t$.

$3t$ is optimal. After time $kt$, each available value depends on at most
$2^k$ inputs, so combining all $8 = 2^3$ inputs needs $k\ge3$.
:::

::: {.solution for="prob-propositional-23" status="draft"}
True. The single operation NAND, $P\uparrow Q = \neg(P\wedge Q)$, is
universal.

1. $\{\neg,\wedge\}$ is universal (every Boolean function has a DNF, and
   $\vee$ can be rewritten with $\neg$ and $\wedge$ by De Morgan's law).

2. Express both with NAND:
   $$\neg P = P\uparrow P,\qquad P\wedge Q = \neg(P\uparrow Q) = (P\uparrow Q)\uparrow(P\uparrow Q).$$

3. So every Boolean function can be built from NAND alone.

This is a *proof by construction* (a constructive existence proof): it proves
that such a set exists by exhibiting one, $\{\uparrow\}$. NOR,
$\neg(P\vee Q)$, also works.
:::
