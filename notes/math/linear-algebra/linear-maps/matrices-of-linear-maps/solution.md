<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-las-1-q10" status="draft"}
(i)

1. $\alpha|_Y$ takes values in $Z$ because $\alpha(Y)\subseteq Z$, and it is linear as a restriction of a linear map.

2. $\overline\alpha$ is well defined: if $v+Y=v'+Y$, then $v-v'\in Y$, so $\alpha(v)-\alpha(v')=\alpha(v-v')\in Z$ and $\alpha(v)+Z=\alpha(v')+Z$. It is linear because the operations on quotients are computed on representatives (@def-quotient-space).

(ii) $A$ is block upper triangular,
$$A=\begin{bmatrix}B&D\\0&C\end{bmatrix},$$
with $B$ in rows $1..l$, columns $1..k$ and $C$ in rows $l+1..m$, columns $k+1..n$ ($D$ is some $l\times(n-k)$ block).

1. For $j\le k$, $\alpha(v_j)\in Z=\langle w_1,\dots,w_l\rangle$, so column $j$ of $A$ is zero below row $l$, and its top part is the $Z$-coordinates of $\alpha|_Y(v_j)$, column $j$ of $B$.

2. For $j>k$, $\alpha(v_j)=\sum_ia_{ij}w_i$, so $\overline\alpha(v_j+Y)=\sum_{i>l}a_{ij}(w_i+Z)$, since $w_i+Z=0$ for $i\le l$. So column $j-k$ of $C$ is $(a_{l+1,j},\dots,a_{m,j})^{\mathsf T}$.

(iii) If $\beta(Y),\gamma(Y)\le Z$ then $(\lambda\beta+\mu\gamma)(y)=\lambda\beta y+\mu\gamma y\in Z$, and $0\in R$; so $R$ is a subspace. By (ii), $\beta\in R$ exactly when its matrix has the $(m-l)\times k$ block in rows $l+1..m$, columns $1..k$ equal to $0$. Under the isomorphism $\mathcal L(V,W)\cong\mathcal M_{m\times n}(\mathbb F)$ (@thm-matrix-of-linear-map), $R$ corresponds to the matrices with that block zero, so
$$\dim R=mn-(m-l)k.$$
:::
