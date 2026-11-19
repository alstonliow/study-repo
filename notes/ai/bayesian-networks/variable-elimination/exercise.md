::: {.problem #prob-cs188hw-7-q1 origin="external" source="cs188hw-7-q1"}
**Bayes Nets.** Consider the following Bayes Net that has four variables $E$, $S$, $M$, and $B$. The associated probabilities are also given in the following tables.

| $E$ | $P(E)$ |
|---|---|
| $+e$ | 0.4 |
| $-e$ | 0.6 |

| $M$ | $P(M)$ |
|---|---|
| $+m$ | 0.1 |
| $-m$ | 0.9 |

| $E$ | $M$ | $S$ | $P(S\mid E,M)$ |
|---|---|---|---|
| $+e$ | $+m$ | $+s$ | 1.0 |
| $+e$ | $+m$ | $-s$ | 0.0 |
| $+e$ | $-m$ | $+s$ | 0.8 |
| $+e$ | $-m$ | $-s$ | 0.2 |
| $-e$ | $+m$ | $+s$ | 0.3 |
| $-e$ | $+m$ | $-s$ | 0.7 |
| $-e$ | $-m$ | $+s$ | 0.1 |
| $-e$ | $-m$ | $-s$ | 0.9 |

| $M$ | $B$ | $P(B\mid M)$ |
|---|---|---|
| $+m$ | $+b$ | 1.0 |
| $+m$ | $-b$ | 0.0 |
| $-m$ | $+b$ | 0.1 |
| $-m$ | $-b$ | 0.9 |

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm, y=1.1cm]
\node[vertex] (E) at (0,1) {$E$};
\node[vertex] (M) at (2,1) {$M$};
\node[vertex] (S) at (1,0) {$S$};
\node[vertex] (B) at (3,0) {$B$};
\draw[->] (E) -- (S);
\draw[->] (M) -- (S);
\draw[->] (M) -- (B);
\end{tikzpicture}
\end{center}
```

*Figure 1: Bayes Net and probability tables.*

**In the following five questions, do not just answer with a numerical value. Write explicitly what probability expression you are calculating. For instance you should write $P(A)P(B)=0.2$ instead of just 0.2.**

1. Write an expression to compute the value of the joint distribution $P(-e,-s,-m,-b)$. What is its value?
2. Write an expression to compute the value of $P(+b)$. What is its value?
3. Write an expression to compute the value of $P(+m\mid+b)$. What is its value?
4. Write an expression to compute the value of $P(+m\mid+s,+b,+e)$. What is its value?
5. Write an expression to compute the value of $P(+e\mid+m)$. What is its value?

Now consider the following Bayes Net in which all variables are binary. We want to compute the query $P(B,D\mid+f)$, so we run variable elimination with the variable elimination ordering being $A,C,E,G$.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm, y=0.9cm]
\node[vertex] (A) at (0,2) {$A$};
\node[vertex] (B) at (0,1) {$B$};
\node[vertex] (C) at (0,0) {$C$};
\node[vertex] (D) at (-1,-1) {$D$};
\node[vertex] (E) at (0,-2) {$E$};
\node[vertex] (F) at (1,-3) {$F$};
\node[vertex] (G) at (2,-2) {$G$};
\draw[->] (A) -- (B);
\draw[->] (B) -- (C);
\draw[->] (C) -- (D);
\draw[->] (C) -- (E);
\draw[->] (D) -- (E);
\draw[->] (C) -- (F);
\draw[->] (E) -- (F);
\draw[->] (C) -- (G);
\draw[->] (F) -- (G);
\end{tikzpicture}
\end{center}
```

*Figure 2: Bayes Net.*

After observing evidence on $F$, we have the following factors:
$$
P(A),\ P(B\mid A),\ P(C\mid B),\ P(D\mid C),\ P(E\mid C,D),\ P(+f\mid C,E),\ P(G\mid C,+f)
$$
When we eliminate the variable $A$, we then create a new factor $f_1(B)=\sum_aP(B\mid a)\cdot P(a)$ and the remaining factors are:
$$
f_1(B),\ P(C\mid B),\ P(D\mid C),\ P(E\mid C,D),\ P(+f\mid C,E),\ P(G\mid C,+f).
$$

6. When we eliminate $C$ next, what is the new factor $f_2$ we obtain? Furthermore, list the leftover factors.
7. When we eliminate $E$ next, what is the new factor $f_3$ we obtain? Furthermore, list the leftover factors.
8. When we eliminate $G$ next, what is the new factor $f_4$ we obtain? Furthermore, list the leftover factors.
9. How can we compute $P(B,D\mid+f)$ using the factors from Q1.8? Explain in a couple of sentences.
10. Between $f_1$, $f_2$, $f_3$, and $f_4$, which is the largest factor (or equivalently whose table has the most rows)?
11. For the same query $P(B,D\mid+f)$, find a new variable elimination ordering that minimizes the size of the largest factor created. Fill in your ordering and generated factors below. Hint: The largest factor should have only 2 variables.

    | Variable Eliminated | Factor Generated |
    |---|---|

*Note (these notes):* Networks redrawn. The local file of the HW7 solutions is a web page, not the solutions, so these answers were checked only by our own computation.
:::

::: {.problem #prob-cs188d-7-q1 origin="external" source="cs188d-7-q1"}
**Variable Elimination.** Using the same Bayes Net (shown below), we want to compute $P(Y\mid+z)$. All variables have binary domains. Assume we run variable elimination to compute the answer to this query, with the following variable elimination ordering: $X,T,U,V,W$.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm, y=1.1cm]
\node[vertex] (T) at (2,2) {$T$};
\node[vertex] (U) at (0,1) {$U$};
\node[vertex] (V) at (1.4,1) {$V$};
\node[vertex] (W) at (2.6,1) {$W$};
\node[vertex] (X) at (4,1) {$X$};
\node[vertex] (Y) at (2,0) {$Y$};
\node[vertex] (Z) at (4,0) {$Z$};
\draw[->] (T) -- (U);
\draw[->] (T) -- (V);
\draw[->] (T) -- (W);
\draw[->] (T) -- (X);
\draw[->] (V) -- (Y);
\draw[->] (W) -- (Y);
\draw[->] (X) -- (Z);
\end{tikzpicture}
\end{center}
```

Complete the following description of the factors generated in this process:

After inserting evidence, we have the following factors to start out with:
$$
P(T),\ P(U\mid T),\ P(V\mid T),\ P(W\mid T),\ P(X\mid T),\ P(Y\mid V,W),\ P(+z\mid X)
$$

(a) When eliminating $X$ we generate a new factor $f_1$ as follows, which leaves us with the factors:
$$
f_1(+z\mid T)=\sum_xP(x\mid T)P(+z\mid x)\qquad P(T),\ P(U\mid T),\ P(V\mid T),\ P(W\mid T),\ P(Y\mid V,W),\ f_1(+z\mid T)
$$

(b) When eliminating $T$ we generate a new factor $f_2$ as follows, which leaves us with the factors:

(c) When eliminating $U$ we generate a new factor $f_3$ as follows, which leaves us with the factors:

(d) When eliminating $V$ we generate a new factor $f_4$ as follows, which leaves us with the factors:

(e) When eliminating $W$ we generate a new factor $f_5$ as follows, which leaves us with the factors:

(f) How would you obtain $P(Y\mid+z)$ from the factors left above:

(g) What is the size of the largest factor that gets generated during the above process?

(m) Does there exist a better elimination ordering (one which generates smaller largest factors)?

*Note (these notes):* Network redrawn from the factors listed in the statement.
:::
