::: {.problem #prob-mit18335ps-3-q3 origin="external" source="mit18335ps-3-q3"}
**Caches and backsubstitution**

In this problem, you will consider the impact of caches (again in the ideal-cache model from class) on the problem of backsubstitution: solving $Rx=b$ for $x$, where $R$ is an $m\times m$ upper-triangular matrix (such as might be obtained by Gaussian elimination). The simple algorithm you probably learned in previous linear-algebra classes (and reviewed in the book, lecture 17) is (processing the rows from bottom to top):

$x_m=b_m/r_{mm}$\
for $j=m-1$ down to $1$\
$\quad x_j=(b_j-\sum_{k=j+1}^m r_{jk}x_k)/r_{jj}$

Suppose that $X$ and $B$ are $m\times n$ matrices, and we want to solve $RX=B$ for $X$—this is equivalent to solving $Rx=b$ for $n$ different right-hand sides $b$ (the $n$ columns of $B$). One way to solve the $RX=B$ for $X$ is to apply the standard backsubstitution algorithm, above, to each of the $n$ columns in sequence.

(a) Give the asymptotic cache complexity $Q(m,n;Z)$ (in asymptotic $\Theta$ notation, ignoring constant factors) of this algorithm for solving $RX=B$.

(b) Suppose $m=n$. Propose an algorithm for solving $RX=B$ that achieves a better asymptotic cache complexity (by cache-aware/blocking or cache-oblivious algorithms, your choice). Can you gain the factor of $1/\sqrt Z$ savings that we showed is possible for square-matrix multiplication?
:::
