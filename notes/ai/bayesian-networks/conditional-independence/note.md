---
title: "Conditional Independence in Bayesian Networks"
sources: [cs221-17, cs221-18]
requires: [ai/bayesian-networks/gibbs-sampling]
status: draft
---

<!-- Added 2026-11-18 from Stanford CS221 (lecture code, commit 3ac2452), Lecture 17 (independence from graph structure, the moralization test) and Lecture 18 (recap as blocked paths), in our own wording; proofs written out in steps. Independence of random variables is @def-independent-random-variables. -->

The graph of a Bayesian network says more than how to factor the joint distribution: it also shows which variables are independent, possibly given others.

::: {#def-conditional-independence .definition name="Conditional independence"}

Random variables $A$ and $B$ are *conditionally independent given* $C$, written $A\perp B\mid C$, if for all values $a,b,c$ with $P(C=c)>0$,

$$
P(A=a,B=b\mid C=c)=P(A=a\mid C=c)\,P(B=b\mid C=c).
$$

With no $C$ this is independence, $A\perp B$ (@def-independent-random-variables). $A$, $B$, $C$ may also be sets of variables.

:::

::: {#prp-three-node-independence .proposition name="Three basic patterns"}

1. *Chain* $A\to C\to B$ and *common cause* $A\leftarrow C\to B$: $A\perp B\mid C$, but in general not $A\perp B$.
2. *Common effect* $A\to C\leftarrow B$: $A\perp B$, but in general not $A\perp B\mid C$.

:::

::: {.proof}

1. Common cause: $P(a,b,c)=p(c)\,p(a\mid c)\,p(b\mid c)$, so $P(a,b\mid c)=p(a\mid c)\,p(b\mid c)$, and summing over $b$ (or $a$) shows these factors are $P(a\mid c)$ and $P(b\mid c)$.

2. Chain: $P(a,b,c)=p(a)\,p(c\mid a)\,p(b\mid c)$. Then $P(a,c)=p(a)p(c\mid a)$ and $P(a,b\mid c)=P(a\mid c)\,p(b\mid c)$, and summing over $a$ gives $P(b\mid c)=p(b\mid c)$.

3. Common effect: $P(a,b)=\sum_cp(a)\,p(b)\,p(c\mid a,b)=p(a)\,p(b)$, since $p(\cdot\mid a,b)$ sums to $1$.

4. The negative statements need only one example each. In the alarm network (@exm-bayesian-network-alarm), a common effect, $P(B=1\mid A=1,E=1)=0.05\ne0.513=P(B=1\mid A=1)$, so $B\not\perp E\mid A$ (explaining away). For a common cause where $A=B=C$ with $C$ a fair coin, $A$ and $B$ are equal, so not independent.

:::

::: {#def-moralization-test .definition name="Testing conditional independence by moralization"}

To decide whether $A\perp B\mid C$ follows from the graph:

1. *shade* the variables in $C$;
2. repeatedly delete leaves (variables with no children) that are not shaded and are not $A$ or $B$;
3. connect ("marry") every two parents of a common child, then drop the directions of all edges;
4. answer *yes* if every path from $A$ to $B$ in this undirected graph passes through a shaded variable.

If the answer is yes, then $A\perp B\mid C$ in every Bayesian network with this graph.

:::

```{=latex}
\begin{algorithm}
\caption{Moralization test for $A\perp B\mid C$}
\begin{algorithmic}
\INPUT DAG $G$, variables $A,B$, set $C$
\OUTPUT Whether $A\perp B\mid C$ is implied by $G$
\WHILE{some vertex $v\notin C\cup\{A,B\}$ has no children}
    \STATE delete $v$ from $G$
\ENDWHILE
\STATE add an edge between every two parents of each vertex; make all edges undirected
\STATE delete the vertices in $C$
\RETURN \textbf{true} if $A$ and $B$ are in different connected components, else \textbf{false}
\end{algorithmic}
\end{algorithm}
```

Equivalently (*d-separation*), $A\perp B\mid C$ when every path between $A$ and $B$ in the DAG is *blocked*: it passes through a chain $X\to M\to Y$ or a common cause $X\leftarrow M\to Y$ with $M\in C$, or through a common effect $X\to M\leftarrow Y$ where neither $M$ nor any descendant of $M$ is in $C$.

::: {#exm-conditional-independence-diagnosis .example name="Reading off independence"}

In the diagnosis network of @exm-bayesian-network-diagnosis ($C\to H\leftarrow A\to I$): to test $C\perp A$, nothing is shaded, so the leaves $H$ and $I$ are deleted and $C$, $A$ are disconnected: yes. To test $C\perp A\mid H$, $H$ is shaded and stays; marrying the parents of $H$ adds the edge $C\text{–}A$: no (explaining away). To test $C\perp I\mid A,H$: after marrying, every path from $C$ to $I$ goes through $A$, which is shaded: yes. Indeed the Markov blanket of $C$ is $\{H,A\}$.

:::

::: {#fig-conditional-independence-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[vertex] (C) at (0,1) {$C$};
\node[vertex] (A) at (2,1) {$A$};
\node[vertex,fill=accentLight] (H) at (1,0) {$H$};
\node[vertex] (I) at (3,0) {$I$};
\draw[->] (C) -- (H); \draw[->] (A) -- (H); \draw[->] (A) -- (I);
\draw[->] (3.7,0.5) -- node[lab,above] {moralize} (4.7,0.5);
\node[vertex] (C2) at (5.4,1) {$C$};
\node[vertex] (A2) at (7.4,1) {$A$};
\node[vertex,fill=accentLight] (H2) at (6.4,0) {$H$};
\node[vertex] (I2) at (8.4,0) {$I$};
\draw (C2) -- (H2); \draw (A2) -- (H2); \draw (A2) -- (I2); \draw[hl] (C2) -- (A2);
\end{tikzpicture}
\end{center}
```

Testing $C\perp A\mid H$ in the diagnosis network: $H$ is shaded, the parents $C$ and $A$ of $H$ are married (highlighted edge), and the path $C\text{–}A$ avoids the shaded $H$, so $C$ and $A$ are not independent given $H$.

:::

::: {#rmk-conditional-independence-1 .remark name="Markov blankets again"}

Every variable is conditionally independent of all the others given its Markov blanket (@def-markov-blanket): after moralization, its neighbours are exactly its Markov blanket. This is why Gibbs sampling needs only the Markov blanket (@prp-gibbs-markov-blanket).

:::
