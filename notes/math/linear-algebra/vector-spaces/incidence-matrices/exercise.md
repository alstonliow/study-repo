::: {.problem #prob-mit1806s10-3-q4 origin="external" source="mit1806s10-3-q4"}
Kirchoff's Law says that current in = current out at every node. This network has six currents $y_1,\dots,y_6$ (the arrows show the positive direction, each $y_i$ could be positive or negative). Find the four equations $A\mathbf{y}=\mathbf{0}$ for Kirchoff's Law at the four nodes. Find three special solutions in the nullspace of $A$.

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (1) at (0,0) {$1$}; \node[small vertex] (2) at (3.2,0) {$2$};
\node[small vertex] (3) at (1.6,2.8) {$3$}; \node[small vertex] (4) at (1.6,0.95) {$4$};
\draw[->] (1) -- node[edge label] {$y_1$} (2);
\draw[->] (2) -- node[edge label] {$y_2$} (3);
\draw[->] (3) -- node[edge label] {$y_3$} (1);
\draw[->] (1) -- node[edge label] {$y_4$} (4);
\draw[->] (2) -- node[edge label] {$y_5$} (4);
\draw[->] (3) -- node[edge label] {$y_6$} (4);
\end{tikzpicture}
\end{center}
```
:::

::: {.problem #prob-mit1806s10-5-q12 origin="external" source="mit1806s10-5-q12"}
With conductances $c_1=c_2=2$ and $c_3=c_4=c_5=3$, multiply the matrices $A^{\mathsf T}CA$. Find a solution to $A^{\mathsf T}CA\mathbf{x}=\mathbf{f}=(1,0,0,-1)$. Where these potentials $\mathbf{x}$ and currents $\mathbf{y}=-CA\mathbf{x}$ on the nodes and edges of the square graph.

*Note (these notes):* The square graph, with edges numbered; $A$ is its $5\times4$ incidence matrix (@def-oriented-incidence-matrix).

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (1) at (0,2.2) {$1$}; \node[small vertex] (2) at (2.2,2.2) {$2$};
\node[small vertex] (3) at (0,0) {$3$}; \node[small vertex] (4) at (2.2,0) {$4$};
\draw[->] (1) -- node[edge label] {$1$} (2);
\draw[->] (1) -- node[edge label] {$2$} (3);
\draw[->] (2) -- node[edge label] {$3$} (3);
\draw[->] (2) -- node[edge label] {$4$} (4);
\draw[->] (3) -- node[edge label] {$5$} (4);
\end{tikzpicture}
\end{center}
```
:::

::: {.problem #prob-mit1806s10-5-q13 origin="external" source="mit1806s10-5-q13"}
Suppose $A$ is a $12\times9$ incidence matrix from a connected (but unknown) graph.

a. How many columns of $A$ are independent?

b. What condition on $\mathbf{f}$ makes it possible to solve $A^{\mathsf T}\mathbf{y}=\mathbf{f}$?

c. The diagonal entries of $A^{\mathsf T}A$ give the number of edges into each node. What is the sum of those diagonal entries?
:::

::: {.problem #prob-mit18065ps-30-q3 origin="external" source="mit18065ps-30-q3"}
For a connected graph with $M$ edges and $N$ nodes, what requirement on $M$ and $N$ comes from each of the words spanning tree ?
:::
