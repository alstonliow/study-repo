<!-- Added 2026-11-27: the examples of Cambridge Part IB Linear Algebra (Michaelmas 2015 lecture notes), Section 4, restated in our own words with our own checks. -->

::: {#exm-bilinear-form-from-matrix .example name="Bilinear forms from rectangular matrices"}

For $A\in\operatorname{Mat}_{m,n}(F)$, $\varphi(v,w)=v^{\mathsf T}Aw$ on $F^m\times F^n$ is bilinear: it is linear in $w$ for fixed $v$ because matrix multiplication is, and linear in $v$ for fixed $w$ because $v\mapsto v^{\mathsf T}(Aw)$ is a linear functional. With $m=n$ and $A=I$ it is $\sum_iv_iw_i$, the dot product when $F=\mathbb R$. Since $\varphi(e_i,e_j)=A_{ij}$, every bilinear form on $F^m\times F^n$ is of this kind for exactly one $A$.

:::
