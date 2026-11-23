::: {.problem #prob-mit18335ps-4-q1 origin="external" source="mit18335ps-4-q1"}
**Almost GMRES**

We use the Arnoldi method to build up an orthogonal basis $Q_n$ for $\mathcal K_n$, with $AQ_n=Q_nH_n+h_{n+1,n}q_{n+1}e_n^*=Q_{n+1}\tilde H_n$. GMRES then finds an approximate solution to $Ax=b$ by minimizing $\|Ax-b\|_2$ for all $x\in\mathcal K_n$, giving an $(n+1)\times n$ least-square problem involving the matrix $\tilde H_n$.

Suppose that we instead find an approximate solution to $Ax=b$ by finding an $x\in\mathcal K_n$ where $b-Ax$ is $\perp\mathcal K_n$. Derive a small ($n\times n$ or similar) system of equations that you can solve to find the approximate solution $x$ of this method.
:::
