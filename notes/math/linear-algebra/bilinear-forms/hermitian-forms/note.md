---
title: "Hermitian Forms"
sources: [camib-la-7]
requires: [math/linear-algebra/bilinear-forms/sylvester-law-of-inertia, math/linear-algebra/eigenvalues/complex-matrices]
status: draft
---

<!-- Added 2026-11-20 from Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 7.2, in our own wording; examples ours; proofs written out in steps. -->

Over $\mathbb C$ a symmetric bilinear form cannot be positive definite: $\phi(iv,iv)=-\phi(v,v)$. The fix is to make the form conjugate-linear in one argument. Following the Cambridge course, forms here are linear in the first argument and conjugate-linear in the second (many physics texts use the opposite convention).

::: {#def-sesquilinear-form .definition name="Sesquilinear and Hermitian forms"}

Let $V,W$ be complex vector spaces. A *sesquilinear form* is a map $\phi:V\times W\to\mathbb C$ with
$$\phi(\lambda v_1+\mu v_2,w)=\lambda\phi(v_1,w)+\mu\phi(v_2,w),\qquad \phi(v,\lambda w_1+\mu w_2)=\bar\lambda\phi(v,w_1)+\bar\mu\phi(v,w_2).$$
Its matrix in bases $e_i$, $f_j$ is $A$ with $a_{ij}=\phi(e_i,f_j)$. A sesquilinear form on $V\times V$ is *Hermitian* if $\phi(u,v)=\overline{\phi(v,u)}$ for all $u,v$.

:::

::: {#fig-hermitian-forms-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[box] (a) at (0,0) {$\phi(\lambda z,w)=\lambda\,\phi(z,w)$}; \node[lab, note, below] at (0,-0.4) {linear in the first slot};
\node[hl box] (b) at (5.2,0) {$\phi(z,\lambda w)=\bar\lambda\,\phi(z,w)$}; \node[lab, note, below] at (5.2,-0.4) {conjugate-linear in the second};
\node[lab, anchor=west, align=left] at (-1.6,-1.3) {then $\phi(z,z)$ is unchanged by $z\mapsto\lambda z$ with $\lvert\lambda\rvert=1$: $\lambda\bar\lambda=1$, so a Hermitian $\phi(z,z)$ can be real};
\end{tikzpicture}
\end{center}
```

Sesquilinear means one and a half times linear. Conjugating in the second argument is what lets $\phi(z,z)$ measure a size, as $\lvert z\rvert^2=z\bar z$ does for one complex number.

:::

::: {#fig-hermitian-forms-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[hl cell] (0.0,0.0) rectangle (0.9,0.9);
\draw[cell frame] (0.9,0.0) rectangle (1.8,0.9);
\draw[cell frame] (1.8,0.0) rectangle (2.7,0.9);
\draw[cell frame] (0.0,-0.9) rectangle (0.9,0.0);
\draw[hl cell] (0.9,-0.9) rectangle (1.8,0.0);
\draw[cell frame] (1.8,-0.9) rectangle (2.7,0.0);
\draw[cell frame] (0.0,-1.8) rectangle (0.9,-0.9);
\draw[cell frame] (0.9,-1.8) rectangle (1.8,-0.9);
\draw[hl cell] (1.8,-1.8) rectangle (2.7,-0.9);
\node[lab] at (0.45,0.45) {$a$};
\node[lab] at (1.35,-0.45) {$b$};
\node[lab] at (2.25,-1.35) {$c$};
\node[lab] at (1.35,0.45) {$z$};
\node[lab] at (0.45,-0.45) {$\bar z$};
\node[lab] at (2.25,0.45) {$w$};
\node[lab] at (0.45,-1.35) {$\bar w$};
\node[lab] at (2.25,-0.45) {$u$};
\node[lab] at (1.35,-1.35) {$\bar u$};
\node[lab, right] at (3.0,0.45) {$a,b,c\in\mathbb R$};
\node[lab, right] at (3.0,-0.45) {$a_{ji}=\overline{a_{ij}}$};
\end{tikzpicture}
\end{center}
```

The matrix of a Hermitian form satisfies $A^{\mathsf H}=A$: entries mirrored in the diagonal are complex conjugates, so the diagonal is real and $\phi(\mathbf z,\mathbf z)$ is always real.

:::

In coordinates $\phi(v,w)=[v]^{\mathsf T}A\,\overline{[w]}$. The form is Hermitian exactly when its matrix satisfies $A=A^{\mathsf H}$ (@def-hermitian-unitary). For a Hermitian form, $\phi(v,v)=\overline{\phi(v,v)}$ is real, so it makes sense to ask for its sign.

::: {#prp-hermitian-form-change-of-basis .proposition name="Change of basis for a Hermitian form"}

If $P$ is the change of basis matrix from $\mathcal B$ to $\mathcal B'$, then $[\phi]_{\mathcal B'}=P^{\mathsf T}[\phi]_{\mathcal B}\bar P$.

:::

::: {.proof}

1. $[v]_{\mathcal B}=P[v]_{\mathcal B'}$, so $\phi(v,w)=(P[v]_{\mathcal B'})^{\mathsf T}A\,\overline{P[w]_{\mathcal B'}}=[v]_{\mathcal B'}^{\mathsf T}(P^{\mathsf T}A\bar P)\overline{[w]_{\mathcal B'}}$.

2. The matrix is determined by this identity, as for bilinear forms.

:::

Writing $R=\bar P$, the rule reads $A\mapsto R^{\mathsf H}AR$ (with $R^{\mathsf H}=P^{\mathsf T}$), which again is Hermitian.

::: {#prp-hermitian-polarization .proposition name="Polarization for Hermitian forms"}

A Hermitian form is determined by its values $\phi(v,v)$:
$$\phi(u,v)=\tfrac14\big(\phi(u+v,u+v)-\phi(u-v,u-v)+i\,\phi(u+iv,u+iv)-i\,\phi(u-iv,u-iv)\big).$$

:::

::: {.proof}

1. Expanding, $\phi(u+cv,u+cv)=\phi(u,u)+\bar c\,\phi(u,v)+c\,\phi(v,u)+\lvert c\rvert^2\phi(v,v)$ for $c\in\mathbb C$.

2. Take $c=1,-1,i,-i$ with weights $1,-1,i,-i$. The terms $\phi(u,u)$ and $\phi(v,v)$ have weights summing to $1-1+i-i=0$. The coefficient of $\phi(u,v)$ is $1\cdot1+(-1)(-1)+i\cdot\bar i+(-i)\cdot\overline{(-i)}=1+1+1+1=4$. The coefficient of $\phi(v,u)$ is $1+1+i\cdot i+(-i)(-i)=1+1-1-1=0$.

3. So the weighted sum is $4\phi(u,v)$.

:::

::: {#fig-hermitian-forms-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (0,0) circle[radius=1];
\draw[->, muted] (-1.15,0) -- (1.15,0); \draw[->, muted] (0,-1.15) -- (0,1.15);
\fill[primary] (1,0) circle[pt] node[anchor=west, lab, note, primary] {$+\frac14\,\phi(u+v,u+v)$};
\fill[accent] (-1,0) circle[pt] node[anchor=east, lab, note, accent] {$-\frac14\,\phi(u-v,u-v)$};
\fill[secondary] (0,1) circle[pt] node[anchor=south, lab, note, secondary] {$+\frac i4\,\phi(u+iv,u+iv)$};
\fill[muted] (0,-1) circle[pt] node[anchor=north, lab, note, muted] {$-\frac i4\,\phi(u-iv,u-iv)$};
\end{tikzpicture}
\end{center}
```

The polarization formula samples $\phi(u+cv,u+cv)$ at the four units $c=1,i,-1,-i$ and weights each value by $c$. The cross terms $\bar c\,\phi(u,v)$ add up, the other terms cancel, leaving $\phi(u,v)$.

:::

::: {#thm-sylvester-hermitian .theorem name="Sylvester's law for Hermitian forms" generalizes="thm-sylvester-law-of-inertia"}

Let $\phi$ be a Hermitian form on an $n$-dimensional complex vector space. There is a basis in which $[\phi]=\operatorname{diag}(I_p,-I_q,0)$, and $p$ and $q$ do not depend on the basis: $p$ is the largest dimension of a subspace on which $\phi$ is positive definite, and $q$ likewise for negative definite.

:::

::: {.proof}

1. If $\phi\ne0$, polarization (@prp-hermitian-polarization) gives $e_1$ with $\phi(e_1,e_1)\ne0$; this value is real, and after scaling by $\lvert\phi(e_1,e_1)\rvert^{-1/2}$ it is $\pm1$.

2. $U=\{u:\phi(u,e_1)=0\}$ is the kernel of the non-zero linear functional $u\mapsto\phi(u,e_1)$, so $\dim U=n-1$ and $V=\langle e_1\rangle\oplus U$, as in @thm-symmetric-form-diagonalizable. By induction $\phi|_U$ has a basis of the required form, and $\phi(e_j,e_1)=0=\overline{\phi(e_1,e_j)}$ for $e_j\in U$. Reorder to get $\operatorname{diag}(I_p,-I_q,0)$.

3. Uniqueness of $p$ and $q$ is the proof of @thm-sylvester-law-of-inertia word for word: a positive definite subspace meets $\langle e_{p+1},\dots,e_n\rangle$ only in $0$.

:::

::: {#fig-hermitian-forms-4}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[cell, fill=primaryLight] (0.000,2.200) rectangle (0.550,2.750);
\node[lab] at (0.275,2.475) {$1$};
\draw[cell frame] (0.550,2.200) rectangle (1.100,2.750);
\draw[cell frame] (1.100,2.200) rectangle (1.650,2.750);
\draw[cell frame] (1.650,2.200) rectangle (2.200,2.750);
\draw[cell frame] (2.200,2.200) rectangle (2.750,2.750);
\draw[cell frame] (0.000,1.650) rectangle (0.550,2.200);
\draw[cell, fill=primaryLight] (0.550,1.650) rectangle (1.100,2.200);
\node[lab] at (0.825,1.925) {$1$};
\draw[cell frame] (1.100,1.650) rectangle (1.650,2.200);
\draw[cell frame] (1.650,1.650) rectangle (2.200,2.200);
\draw[cell frame] (2.200,1.650) rectangle (2.750,2.200);
\draw[cell frame] (0.000,1.100) rectangle (0.550,1.650);
\draw[cell frame] (0.550,1.100) rectangle (1.100,1.650);
\draw[hl cell] (1.100,1.100) rectangle (1.650,1.650);
\node[lab] at (1.375,1.375) {$-1$};
\draw[cell frame] (1.650,1.100) rectangle (2.200,1.650);
\draw[cell frame] (2.200,1.100) rectangle (2.750,1.650);
\draw[cell frame] (0.000,0.550) rectangle (0.550,1.100);
\draw[cell frame] (0.550,0.550) rectangle (1.100,1.100);
\draw[cell frame] (1.100,0.550) rectangle (1.650,1.100);
\draw[cell frame] (1.650,0.550) rectangle (2.200,1.100);
\node[lab] at (1.925,0.825) {$0$};
\draw[cell frame] (2.200,0.550) rectangle (2.750,1.100);
\draw[cell frame] (0.000,0.000) rectangle (0.550,0.550);
\draw[cell frame] (0.550,0.000) rectangle (1.100,0.550);
\draw[cell frame] (1.100,0.000) rectangle (1.650,0.550);
\draw[cell frame] (1.650,0.000) rectangle (2.200,0.550);
\draw[cell frame] (2.200,0.000) rectangle (2.750,0.550);
\node[lab] at (2.475,0.275) {$0$};
\draw[decorate, decoration={brace, amplitude=3pt}] (0,2.85) -- (1.1,2.85) node[midway, above=3pt, lab, tick] {$p$};
\draw[decorate, decoration={brace, amplitude=3pt}] (1.1,2.85) -- (1.65,2.85) node[midway, above=3pt, lab, tick] {$q$};
\draw[decorate, decoration={brace, amplitude=3pt}] (1.65,2.85) -- (2.75,2.85) node[midway, above=3pt, lab, tick] {$n-p-q$};
\node[lab, note, anchor=west, align=left] at (3.2,1.4) {Hermitian forms: the same normal form;\\the diagonal entries $\phi(v_i,v_i)$ are real,\\and $p$, $q$ do not depend on the basis};
\end{tikzpicture}
\end{center}
```

The normal form of a Hermitian form on $\mathbb C^5$ with $p=2$, $q=1$: $\operatorname{diag}(1,\dots,1,-1,\dots,-1,0,\dots,0)$, exactly as for real symmetric forms.

:::

::: {#exm-hermitian-form .example name="A Hermitian form on C^2"}

Let $\phi(\mathbf z,\mathbf w)=\mathbf z^{\mathsf T}A\bar{\mathbf w}$ with $A=\begin{bmatrix}1&i\\-i&1\end{bmatrix}=A^{\mathsf H}$. Then $\phi(\mathbf z,\mathbf z)=\lvert z_1\rvert^2+iz_1\bar z_2-i\bar z_1z_2+\lvert z_2\rvert^2=\lvert z_1-i z_2\rvert^2$, since $\lvert z_1-iz_2\rvert^2=(z_1-iz_2)(\bar z_1+i\bar z_2)$. So $\phi$ is positive semi-definite of rank $1$: $p=1$, $q=0$, and $\phi(\mathbf z,\mathbf z)=0$ on the line $z_1=iz_2$. Its matrix has eigenvalues $0$ and $2$, in agreement.

:::
