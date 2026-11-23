::: {.problem #prob-mit18335ps-3-q2 origin="external" source="mit18335ps-3-q2"}
**Schur fine**

In class, we will show that any square $m\times m$ matrix $A$ can be factorized as $A=QTQ^*$ (the Schur factorization), where $Q$ is unitary and $T$ is an upper-triangular matrix (with the same eigenvalues as $A$, since the two matrices are similar).

(a) $A$ is called "normal" if $AA^*=A^*A$. Show that this implies $TT^*=T^*T$. From this, show that $T$ must be diagonal. Hence, any normal matrix (e.g. unitary or Hermitian matrices) must be unitarily diagonalizable. Hint: consider the diagonal entries of $TT^*$ and $T^*T$, starting from the (1,1) entries and proceeding diagonally downwards by induction.

(b) Given the Schur factorization of an arbitary $A$ (not necessarily normal), describe an algorithm to find the eigenvalues and eigenvectors of $A$, assuming for simplicity that all the eigenvalues are distinct. The flop count should be asymptotically $Km^3+O(m^2)$; give the constant $K$.
:::
