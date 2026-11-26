::: {.problem #prob-mit18433-6-q1 origin="external" source="mit18433-6-q1"}
Deduce König's theorem about the maximum size of a matching in a bipartite graph from the min-max relation for the maximum independent set common to two matroids.
:::

::: {.problem #prob-mit18433ps-5-q5 origin="external" source="mit18433ps-5-q5"}
We are given the following two graphs $G_1$ and $G_2$ with edge set $E=\{a,b,c,d,e,f,g,h,i\}$.

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (TL) at (0,1.4) {};
\node[small vertex] (TM) at (1.4,1.4) {};
\node[small vertex] (TR) at (2.8,1.4) {};
\node[small vertex] (BL) at (0,0) {};
\node[small vertex] (BM) at (1.4,0) {};
\node[small vertex] (BR) at (2.8,0) {};
\draw (TL) -- node[lab, fill=white] {$a$} (TM);
\draw (TM) -- node[lab, fill=white] {$b$} (TR);
\draw (TL) -- node[lab, fill=white] {$c$} (BL);
\draw (BL) -- node[lab, fill=white] {$d$} (BM);
\draw (TL) -- node[lab, fill=white] {$e$} (BM);
\draw (TR) -- node[lab, fill=white] {$f$} (BR);
\draw (TR) -- node[lab, fill=white] {$g$} (BM);
\draw (TM) -- node[lab, fill=white] {$h$} (BM);
\draw (BM) -- node[lab, fill=white] {$i$} (BR);
\node[small vertex] (P1) at (5,2.2) {};
\node[small vertex] (P2) at (6.2,2.2) {};
\node[small vertex] (P3) at (7.2,1.1) {};
\node[small vertex] (P4) at (5,1.1) {};
\node[small vertex] (P5) at (5,0) {};
\node[small vertex] (P6) at (6.2,0) {};
\draw (P2) -- node[lab, fill=white] {$a$} (P3);
\draw (P3) -- node[lab, fill=white] {$b$} (P6);
\draw (P1) -- node[lab, fill=white] {$c$} (P2);
\draw (P1) -- node[lab, fill=white] {$d$} (P4);
\draw (P5) -- node[lab, fill=white] {$e$} (P6);
\draw (P2) -- node[lab, fill=white] {$f$} (P6);
\draw (P4) -- node[lab, fill=white] {$g$} (P6);
\draw (P4) -- node[lab, fill=white] {$h$} (P5);
\draw (P4) -- node[lab, fill=white] {$i$} (P2);
\node[lab] at (1.4,-0.7) {$G_1$};
\node[lab] at (6.1,-0.7) {$G_2$};
\end{tikzpicture}
\end{center}
```

Observe that $S=\{a,b,c,d\}$ is a forest in both $G_1$ and in $G_2$, so it is independent in $M_1=M(G_1)$ and $M_2=M(G_2)$. Construct the exchange graph corresponding to $S$, and indicate which elements are sources and sinks. Using the exchange graph, find a larger set of elements which is acyclic in both $G_1$ and in $G_2$.

*Note (these notes):* graphs redrawn from the problem set.
:::

::: {.problem #prob-mit18433ps-6-q4 origin="external" source="mit18433ps-6-q4"}
Let $A$ be an invertible $n\times n$ matrix (thus $\operatorname{rank}(A)=n$). Let $[n]=\{1,2,\cdots,n\}$ denote the indices of rows and columns of $A$. For any subset $X\subseteq[n]$ and any subset $Y\subseteq[n]$, let $A_{X,Y}$ denote the submatrix with rows indexed by $X$ and columns indexed by $Y$.

The following linear algebra/matrix theory result can be derived in several ways:

**Theorem 0.1** Let $A$ be an invertible $n\times n$ matrix. For any partition of the set of columns into $[n]=Y_1\cup Y_2$, there exists a partition of the set of rows into $[n]=X_1\cup X_2$ such that $A_{X_1,Y_1}$ and $A_{X_2,Y_2}$ are invertible.

Prove this theorem by deriving it from the minmax relation for matroid intersection. (First question to ask yourself is what would be the two matroids to use in this case; one option (which you do not have to necessarily follow) is to take $M_1=([n],\mathcal I_1)$ and $M_2=([n],\mathcal I_2)$ where $\mathcal I_1=\{I:A_{I,Y_1}\text{ has rank }|I|\}$ and $\mathcal I_2^*=\{I:A_{I,Y_2}\text{ has rank }|I|\}$ where the $*$ denotes the dual operation in exercise 1.)
:::
