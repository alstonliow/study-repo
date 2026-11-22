---
title: "The Recursion Theorem for Turing Machines"
sources: [mit18404j-11]
requires: [cs/theory/computability, cs/theory/reducibility]
status: draft
---

<!-- Added 2026-11-22 from MIT 18.404J (Fall 2020), Lecture 11, in our own wording; proofs written out in steps. The informal program version is @thm-recursion-theorem; this note states and proves it for Turing machines. -->

A machine can obtain its own description and compute with it. This makes self-reference a routine programming tool.

::: {#lem-q-computable .lemma name="Printing a description"}

There is a computable function $q:\Sigma^*\to\Sigma^*$ such that, for every string $w$, $q(w)$ is the description $\langle P_w\rangle$ of a TM $P_w$ that ignores its input, prints $w$ on its tape and halts.

:::

::: {.proof}

1. On input $w$, write out the instructions of a machine that writes the symbols of $w$ one at a time and then halts.

:::

::: {#def-self-machine .definition name="The self-printing machine SELF"}

Let $\mathrm{SELF}$ be the TM made of two parts run one after the other:

1. $A=P_{\langle B\rangle}$, which prints the description of $B$;
2. $B$, which, with a description $\langle X\rangle$ on its tape, computes $q(\langle X\rangle)=\langle P_{\langle X\rangle}\rangle$, combines it with $\langle X\rangle$ into the description of the machine "$P_{\langle X\rangle}$, then $X$", and prints that.

When $B$ runs after $A$, the tape holds $\langle B\rangle$, so $B$ prints the description of "$P_{\langle B\rangle}$, then $B$", which is $\langle A B\rangle=\langle\mathrm{SELF}\rangle$.

:::

The trick avoids circularity: $A$ is defined from $B$, and $B$ is defined without reference to $A$, finding $A$ by applying $q$ to what $A$ printed.

::: {#fig-recursion-theorem-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA, draw=none] (-1.6,-0.85) rectangle (5.2,0.85);
\node[box] at (0,0) {$A=P_{\langle B\rangle}$\\ prints $\langle B\rangle$};
\node[hl box] at (3.4,0) {$B$\\ computes $q(\langle B\rangle)=\langle A\rangle$};
\node[lab, note] at (1.8,1.15) {SELF};
\draw[map] (5.4,0) -- (6.4,0);
\node[lab] at (7.4,0) {$\langle A\rangle\langle B\rangle$};
\node[lab, note] at (7.4,-0.5) {$=\langle\mathrm{SELF}\rangle$};
\end{tikzpicture}
\end{center}
```

The two halves of $\mathrm{SELF}$ (@def-self-machine). $A$ supplies $B$'s text; $B$ reconstructs $A$ from that text, then prints both.

:::

::: {#thm-recursion-theorem-tm .theorem name="Recursion theorem" generalizes="thm-recursion-theorem"}

Let $T$ be a TM that computes a function $t:\Sigma^*\times\Sigma^*\to\Sigma^*$. There is a TM $R$ that computes $r:\Sigma^*\to\Sigma^*$ with

$$
r(w)=t(\langle R\rangle,w)\qquad\text{for every } w.
$$

:::

::: {.proof}

1. Build $R$ from three parts $A$, $B$, $T$. $A=P_{\langle BT\rangle}$ writes $\langle BT\rangle$ after the input $w$.

2. $B$ reads $\langle BT\rangle$, computes $q(\langle BT\rangle)=\langle A\rangle$, and combines them into $\langle ABT\rangle=\langle R\rangle$, leaving $\langle R\rangle,w$ on the tape.

3. Control passes to $T$, which computes $t(\langle R\rangle,w)$.

:::

In practice: a TM description may include the step "obtain own description $\langle R\rangle$".

::: {#cor-atm-via-recursion .corollary name="A second proof that $A_{\mathsf{TM}}$ is undecidable"}

:::

::: {.proof}

1. Suppose $H$ decides $A_{\mathsf{TM}}$. Let $R$ be the TM: on input $w$, obtain $\langle R\rangle$ by @thm-recursion-theorem-tm, run $H$ on $\langle R,w\rangle$, and do the opposite of what $H$ says.

2. $R$ accepts $w$ iff $H$ says that $R$ does not accept $w$. So $H$ answers wrongly on $\langle R,w\rangle$, a contradiction.

:::

::: {#thm-min-tm-unrecognizable .theorem name="Minimal machines cannot be listed"}

Call $M$ *minimal* if no TM with a shorter description recognizes $L(M)$. Then $MIN_{\mathsf{TM}}=\{\langle M\rangle: M \text{ is minimal}\}$ is not Turing-recognizable.

:::

::: {.proof}

1. $MIN_{\mathsf{TM}}$ is infinite: there are infinitely many recognizable languages, each with a minimal machine.

2. Suppose an enumerator $E$ enumerates it (@thm-enumerator-recognizable). Let $C$ be the TM: on input $w$, obtain $\langle C\rangle$, run $E$ until it prints some $\langle D\rangle$ longer than $\langle C\rangle$ (this happens, as the list is infinite), and then simulate $D$ on $w$.

3. Then $L(C)=L(D)$ while $\langle C\rangle$ is shorter than $\langle D\rangle$, so $D$ is not minimal, although $E$ printed it. This contradiction shows that no such $E$ exists.

:::

::: {#thm-fixed-point .theorem name="Fixed-point theorem"}

For every computable function $f$ on TM descriptions there is a TM $F$ such that $f(\langle F\rangle)$ describes a TM equivalent to $F$.

:::

::: {.proof}

1. Let $F$ be: on input $w$, obtain $\langle F\rangle$, compute $G$ with $\langle G\rangle=f(\langle F\rangle)$, and simulate $G$ on $w$.

2. $F$ and $G$ accept the same strings, as required.

:::

::: {#fig-recursion-theorem-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (r) at (0,0) {$R$ on input $w$};
\node[box] (s) at (3.6,0) {obtain $\langle R\rangle$};
\node[box] (h) at (7.4,0) {ask $H$ about $\langle R,w\rangle$};
\node[hl box] (o) at (7.4,-1.5) {do the opposite};
\draw[map] (r) -- (s); \draw[map] (s) -- (h); \draw[map] (h) -- (o);
\draw[map, dashed] (o.west) -| node[lab, note, pos=0.25, below] {so $H$ is wrong about $R$} (r.south);
\end{tikzpicture}
\end{center}
```

The self-referential machine of @cor-atm-via-recursion; the diagonal argument of @thm-atm-undecidable becomes a direct program.

:::
