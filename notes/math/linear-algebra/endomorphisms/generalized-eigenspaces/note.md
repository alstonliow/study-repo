---
title: "Generalised Eigenspaces and Existence of Jordan Normal Form"
sources: [camib-la-6]
requires: [math/linear-algebra/endomorphisms/jordan-normal-form, math/discrete/number-theory/extended-euclidean-algorithm]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 6.4 (second half), in our own wording; proofs written out in steps. The course proves the generalised eigenspace decomposition and stops at nilpotent maps (deferring to IB Groups, Rings and Modules); the elementary proof of the nilpotent case here is our own addition, so that the Jordan normal form theorem is proved in full. -->

The existence of the Jordan normal form is proved in two steps: split $V$ into pieces on which $\alpha$ has a single eigenvalue, then handle one eigenvalue, which after subtracting $\lambda\iota$ means a nilpotent map.

::: {#lem-polynomial-bezout .lemma name="Bézout for polynomials" related="thm-bezout"}

If $p_1,\dots,p_k\in F[t]$ have no common factor of positive degree, there are $q_1,\dots,q_k\in F[t]$ with $q_1p_1+\dots+q_kp_k=1$.

:::

::: {.proof}

1. Let $I=\{\sum q_ip_i:q_i\in F[t]\}$. It is closed under addition and under multiplication by any polynomial, and contains each $p_i$. It is not $\{0\}$ (unless all $p_i=0$, which have $t$ as a common factor).

2. Let $g\in I$ be non-zero of least degree. Divide (@thm-polynomial-division): $p_i=s_ig+r_i$ with $r_i=0$ or $\deg r_i<\deg g$. Since $r_i=p_i-s_ig\in I$, minimality forces $r_i=0$: $g$ divides every $p_i$.

3. By hypothesis $g$ has degree $0$, a non-zero constant. Dividing a representation $g=\sum q_ip_i$ by that constant gives $1$.

:::

::: {#thm-generalized-eigenspace-decomposition .theorem name="Generalised eigenspace decomposition"}

Suppose $m_\alpha(t)=\prod_{i=1}^k(t-\lambda_i)^{c_i}$ with distinct $\lambda_i\in F$ (always true over $\mathbb C$). Let $V_i=\ker(\alpha-\lambda_i\iota)^{c_i}$, the *generalised eigenspace* of $\lambda_i$. Then
$$V=V_1\oplus\dots\oplus V_k,$$
each $V_i$ is $\alpha$-invariant, and $\alpha|_{V_i}$ has minimal polynomial $(t-\lambda_i)^{c_i}$.

:::

::: {.proof}

1. Let $p_j(t)=\prod_{i\ne j}(t-\lambda_i)^{c_i}$. These have no common factor of positive degree: by unique factorisation in $F[t]$, such a factor of $p_1$ would be divisible by some $t-\lambda_i$, and $t-\lambda_i$ does not divide $p_i$ (its roots are the $\lambda_l$ with $l\ne i$). By @lem-polynomial-bezout there are $q_j$ with $\sum_jq_jp_j=1$.

2. Let $\pi_j=q_j(\alpha)p_j(\alpha)$. Then $\sum_j\pi_j=\iota$, and $(\alpha-\lambda_j\iota)^{c_j}\pi_j=q_j(\alpha)m_\alpha(\alpha)=0$, so $\operatorname{im}\pi_j\subseteq V_j$. Hence every $v=\sum_j\pi_jv\in\sum_jV_j$.

3. Directness: suppose $\sum_jv_j=0$ with $v_j\in V_j$. For $i\ne j$, $p_i(\alpha)$ contains the factor $(\alpha-\lambda_j\iota)^{c_j}$, so $\pi_iv_j=0$. Then $v_j=\sum_i\pi_iv_j=\pi_jv_j$, and $\pi_j$ applied to $\sum_lv_l=0$ gives $v_j=\pi_jv_j=0$.

4. Each $V_i$ is invariant because $\alpha$ commutes with $(\alpha-\lambda_i\iota)^{c_i}$.

5. $(t-\lambda_i)^{c_i}$ kills $\alpha|_{V_i}$, so the minimal polynomial of $\alpha|_{V_i}$ is $(t-\lambda_i)^{d_i}$ with $d_i\le c_i$. The product $\prod_i(t-\lambda_i)^{d_i}$ kills $\alpha$ on every $V_i$, hence on $V$, so $m_\alpha$ divides it and $d_i\ge c_i$.

:::

::: {#fig-generalized-eigenspaces-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0,0) rectangle (2.10,-2.10);
\draw[hl cell] (0.0,0.0) rectangle (1.4,-1.4); \node[lab, tick] at (0.7,-0.7) {$\begin{smallmatrix}2&1\\0&2\end{smallmatrix}$};
\draw[hl cell] (1.4,-1.4) rectangle (2.10,-2.10); \node[lab, tick] at (1.75,-1.75) {$3$};
\node[lab, note, anchor=west, align=left] at (2.5,-0.5) {$V=V_2\oplus V_3$ with $V_2=\ker(A-2I)^2$, $V_3=\ker(A-3I)$:};
\node[lab, note, anchor=west, align=left] at (2.5,-1.1) {both are invariant, so in an adapted basis the matrix is block diagonal};
\node[lab, note, anchor=west, align=left] at (2.5,-1.7) {and each block has a single eigenvalue};
\end{tikzpicture}
\end{center}
```

The generalised eigenspace decomposition turns any matrix whose characteristic polynomial splits into blocks, one per eigenvalue. Inside a block $\alpha-\lambda\iota$ is nilpotent, which leads to the Jordan form.

:::

In a basis made of bases of the $V_i$, $[\alpha]$ is block diagonal with one block per eigenvalue. When all $c_i=1$ this is the diagonalisability theorem again.

::: {#def-nilpotent .definition name="Nilpotent endomorphism"}

$\beta\in\operatorname{End}(W)$ is *nilpotent* if $\beta^r=0$ for some $r\ge1$; equivalently, $m_\beta=t^c$ for some $c$.

:::

::: {#fig-generalized-eigenspaces-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell frame] (0.000,1.100) rectangle (0.550,1.650);
\draw[hl cell] (0.550,1.100) rectangle (1.100,1.650);
\node[lab] at (0.825,1.375) {$1$};
\draw[cell frame] (1.100,1.100) rectangle (1.650,1.650);
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\draw[hl cell] (1.100,0.550) rectangle (1.650,1.100);
\node[lab] at (1.375,0.825) {$1$};
\draw[cell frame] (0.000,-0.000) rectangle (0.550,0.550);
\draw[cell frame] (0.550,-0.000) rectangle (1.100,0.550);
\draw[cell frame] (1.100,-0.000) rectangle (1.650,0.550);
\node[lab, note] at (0.825,-0.350) {$N$};
\draw[cell frame] (2.200,1.100) rectangle (2.750,1.650);
\draw[cell frame] (2.750,1.100) rectangle (3.300,1.650);
\draw[hl cell] (3.300,1.100) rectangle (3.850,1.650);
\node[lab] at (3.575,1.375) {$1$};
\draw[cell frame] (2.200,0.550) rectangle (2.750,1.100);
\draw[cell frame] (2.750,0.550) rectangle (3.300,1.100);
\draw[cell frame] (3.300,0.550) rectangle (3.850,1.100);
\draw[cell frame] (2.200,-0.000) rectangle (2.750,0.550);
\draw[cell frame] (2.750,-0.000) rectangle (3.300,0.550);
\draw[cell frame] (3.300,-0.000) rectangle (3.850,0.550);
\node[lab, note] at (3.025,-0.350) {$N^2$};
\draw[cell frame] (4.400,1.100) rectangle (4.950,1.650);
\draw[cell frame] (4.950,1.100) rectangle (5.500,1.650);
\draw[cell frame] (5.500,1.100) rectangle (6.050,1.650);
\draw[cell frame] (4.400,0.550) rectangle (4.950,1.100);
\draw[cell frame] (4.950,0.550) rectangle (5.500,1.100);
\draw[cell frame] (5.500,0.550) rectangle (6.050,1.100);
\draw[cell frame] (4.400,-0.000) rectangle (4.950,0.550);
\draw[cell frame] (4.950,-0.000) rectangle (5.500,0.550);
\draw[cell frame] (5.500,-0.000) rectangle (6.050,0.550);
\node[lab, note] at (5.225,-0.350) {$N^3$$\,=0$};
\node[lab, note, anchor=west, align=left] at (6.6,0.825) {each power pushes the $1$s\\one diagonal further up};
\end{tikzpicture}
\end{center}
```

A nilpotent matrix: $N=J_3(0)$ shifts $e_3\mapsto e_2\mapsto e_1\mapsto0$. Its square shifts by two places, and its cube is zero.

:::

::: {#thm-nilpotent-jordan-form .theorem name="Jordan form of a nilpotent map"}

If $\beta\in\operatorname{End}(W)$ is nilpotent, $W$ has a basis consisting of *chains*
$$\beta^{l}w,\ \beta^{l-1}w,\ \dots,\ \beta w,\ w\qquad\text{with }\beta^{l+1}w=0,$$
and in such a basis (each chain listed in this order) $[\beta]$ is a direct sum of blocks $J_{l+1}(0)$.

:::

::: {.proof}

Induction on $\dim W$; $W=\{0\}$ is trivial.

1. If $W\ne\{0\}$, $\beta$ is not injective (otherwise $\beta^r$ would be injective, not $0$), so $\operatorname{im}\beta$ is a $\beta$-invariant subspace of smaller dimension (@thm-rank-nullity) on which $\beta$ is nilpotent. By induction it has a basis of chains: vectors $u_1,\dots,u_k\in\operatorname{im}\beta$ with lengths $l_1,\dots,l_k$, such that $\beta^iu_j$ ($0\le i<l_j$) form a basis of $\operatorname{im}\beta$ and $\beta^{l_j}u_j=0$.

2. Write $u_j=\beta w_j$. The vectors $\beta^{l_j}w_j=\beta^{l_j-1}u_j$ ($j=1,\dots,k$) are part of the basis of $\operatorname{im}\beta$, hence independent, and lie in $\ker\beta$. Extend them to a basis of $\ker\beta$ by vectors $z_1,\dots,z_m$.

3. Candidate basis: the chains $w_j,\beta w_j,\dots,\beta^{l_j}w_j$ ($j\le k$) and the one-element chains $z_1,\dots,z_m$. Their number is $\sum_j(l_j+1)+m=\dim\operatorname{im}\beta+(k+m)=\dim\operatorname{im}\beta+\dim\ker\beta=\dim W$.

4. Independence: suppose $\sum_j\sum_{i=0}^{l_j}a_{ji}\beta^iw_j+\sum_sb_sz_s=0$. Applying $\beta$ kills the $z_s$ and the top terms $\beta^{l_j+1}w_j=\beta^{l_j}u_j=0$, leaving $\sum_j\sum_{i=0}^{l_j-1}a_{ji}\beta^iu_j=0$. These are basis vectors of $\operatorname{im}\beta$, so $a_{ji}=0$ for $i<l_j$.

5. What remains is $\sum_ja_{jl_j}\beta^{l_j}w_j+\sum_sb_sz_s=0$, a combination of the basis of $\ker\beta$ from step 2, so all these coefficients vanish too. By step 3 the vectors form a basis of $W$.

6. For a chain listed as $v_1=\beta^lw,\dots,v_{l+1}=w$, we have $\beta v_1=0$ and $\beta v_i=v_{i-1}$, which are the columns of $J_{l+1}(0)$.

:::

```{=latex}
\begin{algorithm}
\caption{Jordan chains of a nilpotent map}
\begin{algorithmic}
\INPUT A nilpotent $\beta\in\operatorname{End}(W)$
\OUTPUT Vectors $w_j$ whose chains $w_j,\beta w_j,\dots,\beta^{l_j}w_j$ form a basis of $W$
\IF{$W=\{0\}$} \RETURN no chains \ENDIF
\STATE recursively find chains $u_1,\dots,u_k$ for $\beta|_{\operatorname{im}\beta}$
\STATE choose $w_j$ with $\beta w_j=u_j$ for each $j$
\STATE extend the chain ends $\beta^{l_j}w_j$ to a basis of $\ker\beta$ by $z_1,\dots,z_m$
\RETURN $w_1,\dots,w_k,z_1,\dots,z_m$ (each $z_s$ a chain of length one)
\end{algorithmic}
\end{algorithm}
```

::: {#thm-jordan-normal-form-existence .theorem name="Existence of Jordan normal form"}

If $\chi_\alpha$ splits over $F$ (in particular if $F=\mathbb C$), then $V$ has a basis in which $[\alpha]$ is in Jordan normal form. This completes the proof of @thm-jordan-normal-form.

:::

::: {.proof}

1. $m_\alpha\mid\chi_\alpha$ (@thm-cayley-hamilton), so $m_\alpha$ splits as well, and @thm-generalized-eigenspace-decomposition gives $V=\bigoplus V_i$ with $\alpha|_{V_i}-\lambda_i\iota$ nilpotent.

2. By @thm-nilpotent-jordan-form, each $V_i$ has a basis in which $\alpha|_{V_i}-\lambda_i\iota$ is a direct sum of blocks $J_m(0)$, so $\alpha|_{V_i}$ is a direct sum of blocks $J_m(0)+\lambda_iI=J_m(\lambda_i)$.

3. The union of these bases is a basis of $V$ (@prp-direct-sum-criteria), and $[\alpha]$ is block diagonal with these Jordan blocks.

:::

::: {#exm-generalized-eigenspaces .example name="Generalised eigenspaces"}

$A=\begin{bmatrix}2&1&0\\0&2&0\\0&0&3\end{bmatrix}$ has $m_A=(t-2)^2(t-3)$ (@exm-minimal-polynomial). Its generalised eigenspaces are $\ker(A-2I)^2=\langle e_1,e_2\rangle$ and $\ker(A-3I)=\langle e_3\rangle$, while the eigenspace $E(2)=\langle e_1\rangle$ is smaller. Bézout: $p_1=t-3$, $p_2=(t-2)^2$, and $-(t-1)p_1+p_2=-(t^2-4t+3)+(t^2-4t+4)=1$, so $\pi_1=-(A-I)(A-3I)$ and $\pi_2=(A-2I)^2$ are the projections onto the two generalised eigenspaces along each other.

:::

::: {#fig-generalized-eigenspaces-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (2.60,0.00) rectangle (3.35,0.45);
\node[lab, tick] at (2.98,-0.22) {$e_1$};
\draw[cell frame] (3.35,0.00) rectangle (4.10,0.45);
\draw[cell frame] (4.10,0.00) rectangle (4.85,0.45);
\node[lab, anchor=east] at (2.50,0.23) {$\ker(A-2I)$};
\draw[cell, fill=primaryLight] (2.60,-0.90) rectangle (3.35,-0.45);
\draw[cell, fill=primaryLight] (3.35,-0.90) rectangle (4.10,-0.45);
\node[lab, tick] at (3.35,-1.12) {$e_1,e_2$};
\draw[cell frame] (4.10,-0.90) rectangle (4.85,-0.45);
\node[lab, anchor=east] at (2.50,-0.68) {$\ker(A-2I)^2$};
\draw[cell, fill=primaryLight] (2.60,-1.80) rectangle (3.35,-1.35);
\draw[cell, fill=primaryLight] (3.35,-1.80) rectangle (4.10,-1.35);
\node[lab, tick] at (3.35,-2.02) {$e_1,e_2$};
\draw[cell frame] (4.10,-1.80) rectangle (4.85,-1.35);
\node[lab, anchor=east] at (2.50,-1.57) {$\ker(A-2I)^3$};
\node[lab, note, anchor=west, align=left] at (5.2,-0.7) {the kernels grow and then stop:\\$1,2,2,\dots$; the limit is the\\generalised eigenspace $V_2$};
\end{tikzpicture}
\end{center}
```

The kernels of the powers of $A-2I$ for the matrix of @exm-generalized-eigenspaces. The eigenvector $e_1$ is killed in one step; $e_2$ needs two, since $(A-2I)e_2=e_1$.

:::

::: {#fig-generalized-eigenspaces-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[regionA] (0,0) rectangle (3.4,2.0); \node[lab, above] at (1.7,2.0) {$\ker(A-2I)^2=\langle e_1,e_2\rangle$};
\draw[regionB] (0.3,0.3) rectangle (1.5,1.4); \node[lab, tick] at (0.9,1.15) {$E(2)$};
\node[lab] (e1) at (0.9,0.65) {$e_1$}; \node[lab] (e2) at (2.9,0.65) {$e_2$};
\draw[map] (e2) -- node[lab, tick, below=3pt] {$A-2I$} (e1);
\draw[regionC] (4.0,0) rectangle (5.6,2.0); \node[lab, above] at (4.8,2.0) {$\ker(A-3I)$};
\node[lab] at (4.8,1.0) {$e_3$};
\node[lab] at (3.6,1.0) {$\oplus$};
\end{tikzpicture}
\end{center}
```

$\mathbb R^3$ splits into the two generalised eigenspaces of $A$. The eigenspace $E(2)$ is only part of the first one; $e_2$ reaches it after one step of $A-2I$.

:::
