<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-camib-las-1-q3" status="draft"}
Finite-dimensional spaces are isomorphic exactly when their dimensions agree (@thm-isomorphic-iff-same-dimension).

(a) Isomorphic: $(x_1,\dots,x_4)\mapsto(x_1,x_2,x_3,x_4,-x_1-x_2-x_3-x_4)$ is linear and injective, and its inverse is "forget the last coordinate".

(b) Not isomorphic: $1,t,\dots,t^5$ is a basis of $W$, so $\dim W=6\ne5$.

(c) Isomorphic: $f\mapsto g$, $g(x)=f\big(\frac{x+1}2\big)$, with inverse $g\mapsto f$, $f(y)=g(2y-1)$. Both are linear and preserve continuity.

(d) Isomorphic: $I(f)(x)=\int_0^xf$. By the fundamental theorem of calculus $I(f)$ is continuously differentiable with $I(f)'=f$, and $I(f)(0)=0$, so $I:V\to W$. Differentiation $D:W\to V$ satisfies $DI(f)=f$ and $ID(g)(x)=g(x)-g(0)=g(x)$. So $I$ is a linear bijection.

(e) Isomorphic: $(a,b)\mapsto a\cos t+b\sin t$. It is linear, lands in $W$, and is injective since $x(0)=a$, $\dot x(0)=b$. It is surjective: if $x\in W$, let $y=x-x(0)\cos t-\dot x(0)\sin t$, a solution with $y(0)=\dot y(0)=0$. Then $E=y^2+\dot y^2$ has $\dot E=2\dot y(y+\ddot y)=0$, so $E\equiv E(0)=0$ and $y=0$.

(f) Not isomorphic: $1,t,t^2,\dots$ are linearly independent in $C[0,1]$ (a polynomial vanishing on $[0,1]$ has infinitely many roots, so is $0$), so $C[0,1]$ is infinite-dimensional.

(g) Not isomorphic.

1. For $a\in\mathbb R$ let $v_a=(1,a,a^2,\dots)\in\mathbb R^{\mathbb N}$. Any finitely many $v_{a_1},\dots,v_{a_k}$ with distinct $a_i$ are independent: in a relation $\sum c_iv_{a_i}=0$ the first $k$ coordinates give $\sum_ic_ia_i^j=0$ for $0\le j<k$, a Vandermonde system with non-zero determinant, so all $c_i=0$. So $\mathbb R^{\mathbb N}$ has an uncountable independent set.

2. Suppose $\phi:\mathbb R^{\mathbb N}\to P$ is an isomorphism. Then the $\phi(v_a)$, $a\in\mathbb R$, are independent. Each lies in some $P_n=\{p:\deg p\le n\}$, and $\mathbb R$ is uncountable while there are countably many $n$, so some $P_n$ contains infinitely many of them, in particular $n+2$ independent vectors. But $\dim P_n=n+1$, a contradiction.
:::
