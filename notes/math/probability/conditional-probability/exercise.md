<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-probability-1-10 origin="external" source="fit1058-cn-9.10-q10"}
Suppose events $A,B,C$ are independent. Must $A$ also be independent of
$B\cap C$? Justify with a proof or a counterexample.
:::

::: {.problem #prob-probability-1-11 origin="external" source="fit1058-cn-9.10-q11"}
Recall the network reliability problems in §9.7. All links behave
independently with survival probability $p$. Consider the network

```{=latex}
\begin{center}
    \begin{tikzpicture}[scale=0.9,every node/.style={circle,fill,inner sep=1.5pt}]
        \node[label=left:$S$] (S) at (0,0) {};
        \node[label=above:$M$] (M) at (2,1) {};
        \node[label=below:$N$] (N) at (2,-1) {};
        \node[label=right:$T$] (T) at (4,0) {};
        \draw (S)--(M)--(T)--(N)--(S);
        \begin{scope}[xshift=6.5cm]
            \node[label=left:$S$] (S2) at (0,0) {};
            \node[label=above:$M$] (M2) at (2,1) {};
            \node[label=below:$N$] (N2) at (2,-1) {};
            \node[label=right:$T$] (T2) at (4,0) {};
            \draw (S2)--(M2)--(T2)--(N2)--(S2);
            \draw (M2)--(N2);
        \end{scope}
    \end{tikzpicture}
    \end{center}
```

(a) (Left network.) Give an expression in $p$ for the probability that
    there is a path of surviving links from $S$ to $T$.

(b) Compare your answer to (a) with Exercise 4.8(b). Discuss the
    relationship.

(c) (Right network: add a link between $M$ and $N$.) Give an expression
    in $p$ for the probability that there is a path of surviving links
    from $S$ to $T$.

(d) Compare your answer to (c) with Exercise 4.8(c). Discuss the
    relationship.
:::

::: {.problem #prob-probability-1-13 origin="external" source="fit1058-cn-9.10-q13"}
What is the probability that a Scrabble letter is a vowel, given that it is
in the first half of the alphabet?
:::

::: {.problem #prob-probability-1-14 origin="external" source="fit1058-cn-9.10-q14"}
Prove that, for any two events $A$ and $B$, $\Pr(A\mid B)=\Pr(B\mid A)$ if and
only if the events have the same probability.
:::

::: {.problem #prob-probability-1-15 origin="external" source="fit1058-cn-9.10-q15"}
Consider again the four-node, five-link network from Exercise 11, with
$p=\frac12$.

1.  What is the probability that there is a path from $S$ to $T$?

2.  What is the probability that there is a path from $M$ to $N$?
:::
