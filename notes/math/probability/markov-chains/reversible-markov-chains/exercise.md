::: {.problem #prob-eecs126hw-4-q2 origin="external" source="eecs126hw-4-q2"}
**Finite Random Walk.**

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (0) at (0,0) {$0$};
\node[small vertex] (1) at (1.6,0) {$1$};
\node[small vertex] (2) at (3.2,0) {$2$};
\node[lab] at (5.0,0) {$\cdots$};
\node[small vertex] (a) at (7.0,0) {$k-2$};
\node[small vertex] (b) at (8.6,0) {$k-1$};
\draw[->] (0) to[loop left] node[lab,tick,left] {$1-p$} (0);
\draw[->] (b) to[loop right] node[lab,tick,right] {$p$} (b);
\draw[->] (0) to[bend left=30] node[lab,tick,above] {$p$} (1);
\draw[->] (1) to[bend left=30] node[lab,tick,below] {$1-p$} (0);
\draw[->] (1) to[bend left=30] node[lab,tick,above] {$p$} (2);
\draw[->] (2) to[bend left=30] node[lab,tick,below] {$1-p$} (1);
\draw[->] (a) to[bend left=30] node[lab,tick,above] {$p$} (b);
\draw[->] (b) to[bend left=30] node[lab,tick,below] {$1-p$} (a);
\draw[->] (2) to[bend left=30] node[lab,tick,above] {$p$} (4.5,0.25);
\draw[->] (5.5,-0.25) to[bend left=30] node[lab,tick,below] {$1-p$} (2);
\draw[->] (5.5,0.25) to[bend left=30] node[lab,tick,above] {$p$} (a);
\draw[->] (a) to[bend left=30] node[lab,tick,below] {$1-p$} (4.5,-0.25);
\end{tikzpicture}
\end{center}
```

Assume $0<p<1$. Find the stationary distribution. Hint: Let $q=1-p$ and $\rho=\frac pq$, but be careful when $\rho=1$.
:::
