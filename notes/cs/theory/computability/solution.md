<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-cs70hw-9-q1" status="draft"}
Neither exists; both would solve the halting problem (@thm-halting-undecidable), by reduction (@def-reduction).

(a) Given a program $F$ and an input $x$, build $F'$: on input $z$, run $F(x)$, then output $0$. Then $F'(x)=0$ if and only if $F$ halts on $x$, so "$P(F',x,0)$" decides the halting problem.

(b) Given $F$ and $x$, build $F'$: on any input, run $F(x)$ and halt. Let $G$ be a program that halts at once on every input. $F'$ halts on every input if $F$ halts on $x$, and on no input otherwise. So $P(F',G)$ is true exactly when $F$ halts on $x$: again the halting problem.
:::

::: {.solution for="prob-cs70hw-9-q2" status="draft"}
(a) Yes. For $L=1,2,3,\dots$, list all strings of length $L$ over the $15$ symbols, keep the valid formulas, and evaluate each one; stop at the first that evaluates to $n$. Evaluating a formula of $+$, $\times$ and powers of natural numbers always terminates. The search stops at the latest at $L$ equal to the number of digits of $n$, since the decimal numeral of $n$ is itself a formula. Searching by increasing length makes the first formula found a shortest one.

(b) Yes. For $T=1,2,3,\dots$: for every program text of length $\ell<T$, run it for at most $T-\ell$ steps, and check whether it has halted having printed $n$. Stop at the first $T$ for which some program succeeds, and output it.

1. Running a program for a bounded number of steps always terminates, so each round is finite.

2. Some program prints $n$ (for example `print(n)` with $n$ written in it), say with cost $c$; so the search stops by round $T=c$.

3. A program with cost length $+$ time $\le T$ is found in round $T$, and none is found earlier only if all costs exceed the earlier rounds. So the program found has minimum cost. The difference from the halting problem is that a program running longer than $T$ steps already costs more than $T$, so we never need to know whether it halts.
:::

::: {.solution for="prob-cs70hw-9-q3" status="draft"}
(a) There are finitely many texts of under $280$ characters, so only finitely many integers can be defined by them, and a smallest undefinable positive integer exists. But the quoted phrase defines it in under $280$ characters. This is the Berry paradox: "definable" is self-referential, like the liar's sentence (@sec-cs-theory-computability).

(b) There are $2^0+2^1+\dots+2^{n-1}=2^n-1$ bit strings of length less than $n$, so fewer than $2^n-1$ programs of fewer than $n$ bits. Each program returns at most one string, and there are $2^n$ strings of length $n$. So some string of length $n$ is returned by no program shorter than $n$ bits.

(c) $P(n)$: for each of the $2^n$ strings $x$ of length $n$ in alphabetical order, compute $K(x)$; keep the first string with the largest value, and output it.

(d)

1. By (b), the string $x_n$ output by $P(n)$ has $K(x_n)\ge n$.

2. The program "run $P$ on $n$" consists of the $m$ bits of $P$ and the input $n$, about $\log_2n$ bits, plus a constant $c$ for gluing them together. It returns $x_n$, so $K(x_n)\le m+\log_2n+c$.

3. For large $n$, $m+\log_2n+c<n$, contradicting step 1. So $P$ cannot exist, and since $P$ is easily built from $K$, neither can $K$.
:::
