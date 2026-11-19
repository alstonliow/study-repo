::: {.problem #prob-eecs126hw-5-q5 origin="external" source="eecs126hw-5-q5"}
**Discrete Uniform Records.** Consider a Markov chain $(X_n,Y_n)$ that moves on $\mathbb N_0^2$ (where by $\mathbb N_0$ we mean $\mathbb N\cup\{0\}$) as follows. From $(i,j)$ the chains moves to either $(i+1,j)$ or $(i,k)$ for some $0\le k<j$, with each of these $j+1$ possibilities chosen uniformly at random. Let $T=\min\{n\ge0:Y_n=0\}$ be the first time the chain hits the $x$-axis.

(a) Find a recurrence for $E[T]$ for any initial position $(X_0,Y_0)=(i,j)$.

(b) Find the distribution of $X_T$ for any initial position $(i,j)$. Hint: Develop first step equations for the moment generating function $M_{X_T}(s)=E_{i,j}[e^{sX_T}]$. Later we will learn about characteristic functions $\phi_X(t)=E[e^{itX}]$, which are essentially the Fourier transforms of our random variables (whereas the m.g.f. is the Laplace transform). The m.g.f. and characteristic functions both have the property of carrying complete information about the distribution of a random variable. For the purposes of this class, we may think of these two transforms as equivalent.
:::

::: {.problem #prob-eecs126d-7-q1 origin="external" source="eecs126d-7-q1"}
**Recurrence and Transience of Random Walks.** "A drunk man will eventually find his way home but a drunk bird may get lost forever."

Consider the symmetric random walk $S_n=X_1+\dots+X_n$ in dimension $d$, where we start at the origin, and with uniform probability we jump to an adjacent point on the $d$-dimensional lattice $\mathbb Z^d$. That is, $X_i\overset{\text{iid}}{\sim}\text{Uniform}\{\pm e_1,\dots,\pm e_d\}$, where $\{e_1,\dots,e_d\}$ are the unit coordinate vectors in $\mathbb R^d$.

(a) Show that if $\sum_{n=0}^{\infty}P(S_n=0)=\infty$ then the random walk is recurrent. Hint: Let $N$ be the number of times the random walk visits the origin. It may help to notice that $E[N]=\infty$ is equivalent to recurrence of the random walk.

(b) Use this to show that the random walk for $d=1$ is recurrent. You may use Stirling's approximation:
$$n!\sim\sqrt{2\pi n}\Bigl(\frac ne\Bigr)^n.$$

(c) Use part (b) to show that the random walk for $d=2$ is recurrent.

(d) (Optional) Show that the random walk for $d=3$ is transient.

(e) Use part (d) to show that the random walk for any $d>3$ is also transient.
:::

::: {.problem #prob-eecs126hw-7-q1 origin="external" source="eecs126hw-7-q1"}
**Markov Chains with Countably Infinite State Space.**

(a) Consider a Markov chain with state space $\mathbb Z_{>0}$ and transition probability graph:

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (1) at (0,0) {$1$};
\node[lab] at (1.5,0) {$\cdots$};
\node[small vertex] (i) at (3,0) {$i$};
\node[small vertex] (j) at (5.4,0) {$i+1$};
\node[lab] at (6.9,0) {$\cdots$};
\draw[->] (1) to[bend left=30] node[lab,tick,above] {$\frac14$} (1.2,0.25);
\draw[->] (1.2,-0.25) to[bend left=30] node[lab,tick,below] {$\frac12$} (1);
\draw[->] (1) to[loop below] node[lab,tick,below] {$\frac34$} (1);
\draw[->] (1.8,0.25) to[bend left=30] node[lab,tick,above] {$\frac{i-1}{2(i-1)+2}$} (i);
\draw[->] (i) to[bend left=30] node[lab,tick,below] {$\frac12$} (1.8,-0.25);
\draw[->] (i) to[bend left=30] node[lab,tick,above] {$\frac{i}{2i+2}$} (j);
\draw[->] (j) to[bend left=30] node[lab,tick,below] {$\frac12$} (i);
\draw[->] (i) to[loop below] node[lab,tick,below] {$\frac{1}{2i+2}$} (i);
\draw[->] (j) to[loop below] node[lab,tick,below] {$\frac{1}{2(i+1)+2}$} (j);
\draw[->] (j) to[bend left=30] node[lab,tick,above] {$\frac{i+1}{2(i+1)+2}$} (6.6,0.25);
\draw[->] (6.6,-0.25) to[bend left=30] node[lab,tick,below] {$\frac12$} (j);
\end{tikzpicture}
\end{center}
```

Show that this Markov chain has no stationary distribution.

(b) Consider a Markov chain with state space $\mathbb Z_{>0}$ and transition probability graph:

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[small vertex] (1) at (0,0) {$1$};
\node[lab] at (1.5,0) {$\cdots$};
\node[small vertex] (i) at (3,0) {$i$};
\node[small vertex] (j) at (5.4,0) {$i+1$};
\node[lab] at (6.9,0) {$\cdots$};
\draw[->] (1) to[bend left=30] node[lab,tick,above] {$a$} (1.2,0.25);
\draw[->] (1.2,-0.25) to[bend left=30] node[lab,tick,below] {$b$} (1);
\draw[->] (1) to[loop below] node[lab,tick,below] {$1-a$} (1);
\draw[->] (1.8,0.25) to[bend left=30] node[lab,tick,above] {$a$} (i);
\draw[->] (i) to[bend left=30] node[lab,tick,below] {$b$} (1.8,-0.25);
\draw[->] (i) to[bend left=30] node[lab,tick,above] {$a$} (j);
\draw[->] (j) to[bend left=30] node[lab,tick,below] {$b$} (i);
\draw[->] (i) to[loop below] node[lab,tick,below] {$1-a-b$} (i);
\draw[->] (j) to[loop below] node[lab,tick,below] {$1-a-b$} (j);
\draw[->] (j) to[bend left=30] node[lab,tick,above] {$a$} (6.6,0.25);
\draw[->] (6.6,-0.25) to[bend left=30] node[lab,tick,below] {$b$} (j);
\end{tikzpicture}
\end{center}
```

Assume that $0<a<b$ and $0<a+b\le1$. Show that the probability distribution given by
$$\pi(i)=\Bigl(\frac ab\Bigr)^{i-1}\Bigl(1-\frac ab\Bigr),\quad\text{for }i\in\mathbb Z_{>0},$$
is a stationary distribution of this Markov chain.
:::
