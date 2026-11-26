::: {.problem #prob-mit6854ps-4-q6 origin="external" source="mit6854ps-4-q6"}
Given an undirected graph $G=(V,E)$, a set $T\subseteq V$ with $|T|$ even and a weight function $w:E\to\mathbb Q_+$, the minimum (weight) $T$-cut problem is to find $S\subseteq V$ with $|S\cap T|$ odd (thus, $|\bar S\cap T|=|T\setminus S|$ is also odd) such that $d(S):=w(S:\bar S):=\sum_{e\in(S:\bar S)}w_e$ is minimized. Here $(S:\bar S)$ denotes the set of edges of $E$ with exactly one endpoint in $S$ (since our graph is undirected, observe that $d(S)=d(\bar S)$). For $T=\{s,t\}$, the minimum $T$-cut problem reduces to the minimum $s-t$ cut problem (in an undirected graph). In this problem, you will show that the minimum $T$-cut problem can be solved efficiently.

1. Argue that the minimum $s-t$ cut problem in an undirected graph $G$ can be solved efficiently by using an algorithm for a minimum $s-t$ cut problem in a directed graph $H$.
2. A $T-T$ cut is a cut $(S:\bar S)$ with $S\cap T\ne\emptyset$ and $\bar S\cap T\ne\emptyset$. Show that the minimum weight $T-T$ cut can be obtained by solving a polynomial number of minimum $s-t$ cut problems. Can you do it with $O(|T|)$ such minimum $s-t$ cut computations?
3. Prove that for any $A,B\subseteq V$, we have
$$d(A)+d(B)\ge d(A\cap B)+d(A\cup B).$$
4. To solve the minimum $T$-cut problem, suppose we first solve the minimum $T-T$ cut problem and obtain the cut $(S:\bar S)$. If $|S\cap T|$ is odd, we are done (right?). If $|S\cap T|$ is even, use the previous inequality to argue that there exists a minimum $T$-cut $(C:\bar C)$ such that $C\subseteq S$ or $C\subseteq\bar S$. Deduce from this an efficient algorithm for solving the minimum $T$-cut problem. How many calls to your minimum $T-T$ cut algorithm are you using?
:::
