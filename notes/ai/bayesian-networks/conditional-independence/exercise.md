::: {.problem #prob-cs188hw-6-q1 origin="external" source="cs188hw-6-q1"}
**Tracing Contacts.** There is a rumor circulating that a past CS 188 head TA is submitting fake pet pics while disguising as a student. You are trying to retrace the origins of this rumor but do not know who spread the story to whom. However, you know the contacts between each pair of people and are able to create the network below.

Assume that the direction of each edge is uniformly random and that the direction of any two edges is independent.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm, y=1.1cm]
\node[vertex] (A) at (0,1) {$A$};
\node[vertex] (B) at (1.2,1) {$B$};
\node[vertex] (C) at (0.6,0) {$C$};
\node[vertex] (G) at (2.6,-0.6) {$G$};
\node[vertex] (F) at (4.6,0) {$F$};
\node[vertex] (D) at (4.0,1) {$D$};
\node[vertex] (E) at (5.2,1) {$E$};
\draw[-] (A) -- (C);
\draw[-] (B) -- (C);
\draw[-] (C) -- (G);
\draw[-] (G) -- (F);
\draw[-] (D) -- (F);
\draw[-] (E) -- (F);
\end{tikzpicture}
\end{center}
```

1. What is the probability that a member of the group ABC spread the rumor to group DEF through G? (Hint: Don't overthink this question. What must the direction of certain edges be in the graph?)
2. What is the probability that $B\perp\!\!\!\perp F$ is guaranteed via the independence relations encoded by the Bayes Net?
3. If we add an edge between nodes B and D, what is the probability that the above Bayes Net is undefined?

In another class, you recover the following chain of contacts. Continue assuming that the direction of each edge is uniformly random and that the direction of any two edges is independent.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[vertex] (a) at (0,0) {$X_1$}; \node[vertex] (b) at (1.5,0) {$X_2$}; \node[lab] (c) at (3,0) {$\cdots$}; \node[vertex] (d) at (4.5,0) {$X_n$};
\draw (a) -- (b) -- (c) -- (d);
\end{tikzpicture}
\end{center}
```

4. What is the probability that $X_1\perp\!\!\!\perp X_n$ is guaranteed for n = 3?
5. What is the probability that $X_1\perp\!\!\!\perp X_n$ for any $n\ge3$?

   $\frac{n}{4}-\frac12$ $\quad\frac{1}{2^{n-1}}$ $\quad\frac{2^{n-1}-1}{2^{n-1}}-\frac12$ $\quad\frac{1}{2^{n-2}}-\frac14$ $\quad\frac{1}{2^{n-2}}$ $\quad$ None of the above $\quad\frac{2^{n-1}-1}{2^{n-1}}$ $\quad\frac{2^{n-1}-n}{2^{n-1}}$
6. Conditioned on $X_1\perp\!\!\!\perp X_n$ guaranteed true, what is the probability of the $X_1$ – $X_2$ edge pointing left?

   $\frac12$ $\quad\frac14$ $\quad\frac{2^{n-2}-(n-1)}{2^{n-1}-n}$ $\quad\frac{2^{n-2}-1}{2^{n-1}}$ $\quad\frac{2^{n-2}-1}{2^{n-1}-n}$ $\quad$ None of the above $\quad\frac{2^{n-2}-(n-1)}{2^{n-1}}$ $\quad\frac{2^{n-2}}{2^{n-1}-n}$
:::
