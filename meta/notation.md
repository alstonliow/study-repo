---
title: Notation
version: 0.1
status: draft
---

# Notation v0.1

Standard symbols for all notes (`meta/SPEC.md` §7). Transcribed from the
1058note notation summary (chapter 11). Symbols and descriptions are unchanged;
only the format changed:

- 1058note macros are expanded to plain LaTeX: `\N` → `\mathbb{N}` (likewise
  `\Z`, `\Q`, `\R`, `\C`), `\dom` → `\operatorname{dom}`,
  `\lcmop` → `\operatorname{lcm}`.
- Vertical bars inside table cells are written `\lvert … \rvert` / `\vert` so the
  Markdown tables do not break. They render the same.
- Chapter numbers are replaced by taxonomy branches (`meta/taxonomy.md`).

Notation differences between sources are recorded in the `sources/` mappings,
not here.

## Sets (`math/discrete/sets`)

| Symbol | Meaning |
|---|---|
| $\in,\ \notin$ | membership |
| $\emptyset,\ \{\}$ | empty set |
| $\{x : P(x)\}$ | set-builder |
| $[a,b],\ (a,b),\ [a,b),\ (a,b]$ | intervals |
| $\mathbb{N},\mathbb{Z},\mathbb{Z}^+,\mathbb{Z}^-,\mathbb{Q},\mathbb{R},\mathbb{R}^+,\mathbb{R}^-,\mathbb{C}$ | standard number sets |
| $\lvert A\rvert$ | cardinality |
| $\Sigma,\ \Sigma^n,\ \Sigma^*$ | alphabet, strings of length $n$, all strings |
| $\subseteq,\ \subsetneq,\ \supseteq$ | subset, proper subset, superset |
| $\mathcal P(A)$ | power set |
| $\binom{n}{k}$ | binomial coefficient |
| $A-B$ (or $A\setminus B$), $\overline{A}$ | set difference, complement |
| $\cup,\ \cap$ | union, intersection |
| $\triangle$ | symmetric difference |
| $\times,\ A^n$ | Cartesian product, $n$-fold power |

## Functions and relations (`math/discrete/functions`, `math/discrete/relations`)

| Symbol | Meaning |
|---|---|
| $f:A\to B,\ f(x)$ | function declaration, value |
| $\operatorname{dom}(f)$ | domain |
| $i_A$ | identity function |
| $\chi_A$ | indicator/characteristic function |
| $c_a$ | constant function |
| $\lfloor x\rfloor,\ \lceil x\rceil$ | floor, ceiling |
| $f\vert_X$ | restriction |
| $f^{-1}$ | inverse function (or preimage, context-dependent) |
| $g\circ f$ | composition |
| $f^{(n)}$ | iterated composition |
| $e_k,\ d_k$ | encryption/decryption (cryptosystem) |
| $R \subseteq A\times B,\ xRy$ | binary relation, infix notation |
| $R(x),\ R^{-1}(y)$ | image set, inverse-image set (relation) |
| $R\circ S$ | relation composition |
| $R^{(n)},\ R^+$ | iterated relation, transitive closure |
| $[x]_R$ | equivalence class |
| $[a_{ij}]$ | matrix |
| $\wedge,\vee$ (matrices) | meet, join (zero-one matrices) |
| $\odot$ | Boolean matrix product |
| $\preceq$ | partial order |
| $\vee,\wedge$ (posets) | join (LUB), meet (GLB) |

## Propositional logic (`math/discrete/logic/propositional`)

| Symbol | Meaning |
|---|---|
| $T,\ F$ | truth values |
| $\neg$ | negation |
| $\wedge,\ \vee$ | conjunction, disjunction |
| $\implies,\ \iff$ | implication, biconditional |
| $\oplus$ | exclusive-or |
| $\mid$ | Sheffer stroke (NAND) |
| $\equiv$ (or $=$) | logical equivalence |
| $w,\ \mathcal M(f)$ | a model (truth assignment); the set of models of $f$ |
| $\mathcal I(f,w)$ | interpretation: truth value of $f$ in model $w$ |
| $\text{KB}\models f,\ \text{KB}\vdash f$ | entailment (semantic), derivation (syntactic) |

## Predicate logic (`math/discrete/logic/predicate`)

| Symbol | Meaning |
|---|---|
| $P(x)$ | predicate applied to a term |
| $\exists x,\ \exists x\in A$ | existential quantifier, restricted |
| $\forall x,\ \forall x\in A$ | universal quantifier, restricted |
| $\operatorname{dom}(f)$ | (as in functions – domain of a variable/predicate argument) |

## Sequences and series (`math/discrete/sequences`)

| Symbol | Meaning |
|---|---|
| $(a_n),\ f_n,\ (n^2:n\in\mathbb{N})$ | sequence, $n$-th term, formula notation |
| $a,d$ | arithmetic sequence: first term, common difference |
| $a,r$ | geometric sequence: first term, common ratio |
| $\varphi,\psi$ | golden ratio and its conjugate (Fibonacci/Binet) |
| $O,\ \Omega,\ \Theta$ | big-O, big-Omega, big-Theta |
| $P,\ NP$ | complexity classes |
| $\sum,\ \prod$ | summation, product notation |
| $A_n$ | partial sum, Abel summation |
| $\lim_{n\to\infty}a_n,\ \varepsilon,N$ | sequence limit, $\varepsilon$-$N$ definition |
| $H_n$ | harmonic number |
| $\gamma$ | Euler's constant |
| $G(x)$ | generating function |

## Number theory (`math/discrete/number-theory`)

| Symbol | Meaning |
|---|---|
| $d\mid n,\ d\nmid n$ | $d$ divides $n$ / does not divide $n$ |
| $d\mathbb{Z}$ | set of multiples of $d$ |
| $n\bmod d$ | remainder of $n$ on division by $d$ |
| $\lfloor n/d\rfloor$ | quotient of $n$ on division by $d$ |
| $\gcd(a,b),\ \operatorname{lcm}(a,b)$ | greatest common divisor, least common multiple |
| $\mathrm{CD}(x,y)$ | set of common divisors of $x,y$ |
| $m\mathbb{Z}+n\mathbb{Z}$ | integer linear combinations $\{xm+yn : x,y\in\mathbb{Z}\}$ |
| $(a,x,y),\ (b,z,w)$ | EEA triples, $a=xm+yn,\ b=zm+wn$ |
| $a\equiv b\pmod n$ | congruence mod $n$: $n\mid(a-b)$ |
| $[a],\ a+n\mathbb{Z}$ | residue class of $a$ mod $n$ |
| $\mathbb{Z}_n$ | $\{0,\dots,n-1\}$ with arithmetic mod $n$ |
| $\mathbb{Z}_n^*$ | elements of $\mathbb{Z}_n$ with a multiplicative inverse |
| $x^{-1}$ (mod $n$) | multiplicative inverse of $x$ in $\mathbb{Z}_n$ |
| $\varphi(n)$ | Euler totient function, $\lvert\mathbb{Z}_n^*\rvert$ |
| $\mathrm{ds}(n),\ \mathrm{ads}(n)$ | digital sum, alternating digital sum |
| $\log_a y$ (mod $n$) | discrete logarithm: $x$ with $a^x\equiv y\pmod n$ |
| $p,q$ | primes (generic; RSA's two secret primes in examples) |
| $e,d$ | RSA public/private exponents |
| $x_A,x_B,y_A,y_B$ | Diffie–Hellman private/public numbers |
| $k_{AB},\ k_{BA}$ | Diffie–Hellman shared key |

## Counting and combinatorics (`math/discrete/counting`)

| Symbol | Meaning |
|---|---|
| $\lceil x\rceil,\ \lfloor x\rfloor$ | ceiling, floor (pigeonhole bounds) |
| $R(3,3)$ | Ramsey number |
| $\bigcup,\bigcap$ (inclusion-exclusion) | union/intersection over index sets, @sec-math-discrete-counting-inclusion-exclusion |
| $D_n$ | derangement count |
| $(n)_r,\ {}_nP_r,\ P(n,r)$ | falling factorial, permutations |
| $\binom{n}{r},\ {}_nC_r$ | binomial coefficient, combinations |
| $\binom{r+n-1}{r}$ | unordered selection with replacement (stars and bars) |
| $S(n,k)$ | Stirling number of the second kind |

## Proof and general notation (`math/discrete/proof`, throughout)

| Symbol | Meaning |
|---|---|
| $\blacksquare$ | end of proof |
| $\mid$ (number theory) | divides ($a\mid b$) |
| $\Rightarrow$ (proof steps) | logical consequence within a proof |

## Linear algebra (`math/linear-algebra`)

<!-- Added 2026-11-18 with MIT 18.06. -->

| Symbol | Meaning |
|---|---|
| $\mathbf{x},\ \mathbf{b},\ \mathbf{0}$ | column vectors (bold lowercase); $x_i$ is a component |
| $A,\ I,\ E_{ij},\ P,\ Q$ | matrices (capital); identity, elimination, permutation or projection, orthogonal |
| $a_{ij}$ | entry in row $i$, column $j$ |
| $A^{\mathsf T},\ A^{-1},\ A^{+}$ | transpose, inverse, pseudoinverse |
| $A^{\mathsf H}=\bar{A}^{\mathsf T}$ | conjugate transpose (complex matrices) |
| $\mathbf{v}\cdot\mathbf{w}=\mathbf{v}^{\mathsf T}\mathbf{w}$ | dot product |
| $\lVert\mathbf{v}\rVert$ | length (Euclidean norm) |
| $\mathbb{R}^n,\ \mathbb{C}^n$ | real and complex column vectors with $n$ components |
| $C(A),\ N(A),\ C(A^{\mathsf T}),\ N(A^{\mathsf T})$ | column space, nullspace, row space, left nullspace |
| $\operatorname{rank}A=r$ | rank (number of pivots) |
| $\dim V,\ V^{\perp}$ | dimension, orthogonal complement |
| $\det A=\lvert A\rvert$ | determinant |
| $C_{ij}$ | cofactor |
| $\lambda,\ \mathbf{x}$ | eigenvalue, eigenvector ($A\mathbf{x}=\lambda\mathbf{x}$) |
| $\Lambda,\ S$ | diagonal eigenvalue matrix, eigenvector matrix ($A=S\Lambda S^{-1}$) |
| $\sigma_i,\ \Sigma,\ U,\ V$ | singular values and the SVD $A=U\Sigma V^{\mathsf T}$ |
| $\operatorname{tr}A$ | trace |

### Abstract linear algebra (`math/linear-algebra`, Cambridge IB branches)

<!-- Added 2026-11-20 with Cambridge IB Linear Algebra. Vectors in abstract spaces are plain letters, not bold. -->

| Symbol | Meaning |
|---|---|
| $F$ | field of scalars |
| $u,v,w$; $\langle S\rangle$ | vectors of an abstract space; span of a set |
| $U\le V$, $V/U$, $U\oplus W$ | subspace, quotient space, direct sum |
| $\alpha,\beta$; $\iota$ | linear maps; the identity map |
| $\mathcal L(U,V)$, $\operatorname{End}(V)$ | linear maps $U\to V$; endomorphisms of $V$ |
| $[\alpha]_{\mathcal B,\mathcal C}$, $[v]_{\mathcal B}$ | matrix of $\alpha$ from basis $\mathcal B$ to basis $\mathcal C$; coordinates of $v$ |
| $r(\alpha)$, $n(\alpha)$ | rank and nullity |
| $V^*$, $\varepsilon_i$, $U^0$ | dual space, dual basis, annihilator |
| $\alpha'$ | dual map $\theta\mapsto\theta\circ\alpha$ |
| $\alpha^*$ | adjoint (inner product spaces) |
| $\chi_\alpha$, $m_\alpha$ | characteristic polynomial $\det(t\iota-\alpha)$, minimal polynomial |
| $E(\lambda)$; $a_\lambda$, $g_\lambda$, $c_\lambda$ | eigenspace; algebraic and geometric multiplicity, multiplicity in $m_\alpha$ |
| $J_m(\lambda)$ | Jordan block |
| $\varepsilon(\sigma)$ | sign of a permutation |
| $\langle u,v\rangle$, $\lVert v\rVert$ | inner product (linear in the first argument), norm |
| $O(V)$, $U(V)$ | orthogonal and unitary groups |

## Calculus (`math/calculus`)

<!-- Added 2026-11-18 with MIT 18.01. -->

| Symbol | Meaning |
|---|---|
| $\lim_{x\to a}f(x),\ \lim_{x\to a^\pm}f(x)$ | limit, one-sided limits |
| $f'(x),\ \frac{dy}{dx},\ Df$ | derivative |
| $f'',\ f^{(n)},\ \frac{d^ny}{dx^n}$ | higher derivatives |
| $\Delta x,\ \Delta f,\ dx,\ dy$ | increments, differentials |
| $\int f(x)\,dx,\ \int_a^bf(x)\,dx$ | indefinite and definite integral |
| $F(x)\big\vert_a^b$ | $F(b)-F(a)$ |
| $e,\ \ln x$ | base of the natural logarithm, natural logarithm |
| $\sin^{-1},\ \cos^{-1},\ \tan^{-1}$ | inverse trigonometric functions |
| $\sinh,\ \cosh$ | hyperbolic functions |
| $(r,\theta)$ | polar coordinates |

### Multivariable calculus (`math/calculus/multivariable`)

<!-- Added 2026-11-18 with MIT 18.02. -->

| Symbol | Meaning |
|---|---|
| $\mathbf{A},\ \mathbf{F},\ \mathbf{r}$ | vectors and vector fields (bold); $\mathbf{r}=\langle x,y,z\rangle$ is the position vector |
| $\langle a_1,a_2,a_3\rangle=a_1\mathbf{i}+a_2\mathbf{j}+a_3\mathbf{k}$ | components; $\mathbf{i},\mathbf{j},\mathbf{k}$ are the unit coordinate vectors |
| $\lvert\mathbf{A}\rvert,\ \operatorname{dir}\mathbf{A}$ | length (same as $\lVert\mathbf{A}\rVert$), direction $\mathbf{A}/\lvert\mathbf{A}\rvert$ |
| $\overrightarrow{PQ}$ | vector from $P$ to $Q$ |
| $\mathbf{A}\times\mathbf{B}$ | cross product |
| $\hat{\mathbf{u}},\ \hat{\mathbf{T}},\ \hat{\mathbf{n}}$ | unit vector, unit tangent, unit normal |
| $f_x,\ \frac{\partial f}{\partial x},\ f_{xy}$ | partial derivatives |
| $\left(\frac{\partial f}{\partial x}\right)_{y}$ | partial derivative with $y$ held fixed |
| $\nabla f,\ \frac{df}{ds}\big\vert_{\hat{\mathbf{u}}}$ | gradient, directional derivative |
| $\frac{\partial(u,v)}{\partial(x,y)}$ | Jacobian determinant |
| $dA,\ dV,\ dS,\ ds$ | area, volume, surface area and arclength elements |
| $(r,\theta,z),\ (\rho,\phi,\theta)$ | cylindrical and spherical coordinates ($\phi$ measured down from the $z$-axis) |
| $\int_C\mathbf{F}\cdot d\mathbf{r}=\int_CM\,dx+N\,dy$, $\oint_C$ | line integral (work), around a closed curve |
| $\iint_S\mathbf{F}\cdot\hat{\mathbf{n}}\,dS=\iint_S\mathbf{F}\cdot d\mathbf{S}$ | flux through a surface |
| $\operatorname{div}\mathbf{F}=\nabla\cdot\mathbf{F},\ \operatorname{curl}\mathbf{F}=\nabla\times\mathbf{F}$ | divergence, curl |
| $\nabla^2u$ | Laplacian $u_{xx}+u_{yy}+u_{zz}$ |

## Probability (`math/probability`)

<!-- TODO: 1058note chapter 11 has no probability section. Add symbols during migration of chapter 9. -->

### Convex optimization (`math/optimization`)

<!-- Added 2026-11-21 with Stanford EE364A (CVX101). Vectors are plain lowercase letters, as in Boyd and Vandenberghe; matrices are capitals. -->

| Symbol | Meaning |
|---|---|
| $x,y,z\in\mathbb{R}^n$; $x_i$ | vectors (plain lowercase); components |
| $\mathbf 1$, $e_i$ | the all-ones vector; the $i$-th unit vector |
| $x\preceq y$, $x\prec y$ | componentwise inequality ($x_i\le y_i$, $x_i<y_i$) for vectors |
| $\mathbb S^n$, $\mathbb S^n_+$, $\mathbb S^n_{++}$ | symmetric, positive semidefinite, positive definite $n\times n$ matrices |
| $X\succeq0$, $X\succ0$ | $X\in\mathbb S^n_+$, $X\in\mathbb S^n_{++}$ |
| $x\preceq_K y$, $x\prec_K y$ | generalized inequality: $y-x\in K$, $y-x\in\operatorname{int}K$ |
| $K^*$, $\lVert\cdot\rVert_*$ | dual cone, dual norm |
| $\operatorname{dom}f$ | domain of $f$; $f$ is $+\infty$ outside it (extended-value extension) |
| $\operatorname{epi}f$, $f^*$ | epigraph, conjugate function |
| $\operatorname{conv}C$, $\operatorname{int}C$, $\operatorname{relint}C$ | convex hull, interior, relative interior |
| $\nabla f(x)$, $\nabla^2 f(x)$ | gradient, Hessian |
| $p^\star$, $d^\star$, $x^\star$, $(\lambda^\star,\nu^\star)$ | optimal values of the primal and dual problems; optimal points |
| $L(x,\lambda,\nu)$, $g(\lambda,\nu)$ | Lagrangian, Lagrange dual function |
| $\Delta x_{\rm nt}$, $\lambda(x)$ | Newton step, Newton decrement |

## Algorithms (`cs/algorithms`, `cs/data-structures`, `cs/graph-algorithms`, `cs/dynamic-programming`)

| Symbol | Meaning |
|---|---|
| $n$, $\lvert V\rvert$, $\lvert E\rvert$ | input size; numbers of vertices and edges |
| $w$ | word size of the word-RAM (in graphs: the weight function $w(u,v)$) |
| $\log$ | base $2$ unless another base is written; bases matter only inside exponents |
| $\operatorname{Adj}^+(u)$, $\operatorname{Adj}^-(u)$ | out- and in-neighbours of $u$; $\operatorname{Adj}(u)=\operatorname{Adj}^+(u)$ |
| $\deg^+(u)$, $\deg^-(u)$ | out- and in-degree |
| $\delta(s,v)$ | distance: least weight (or length) of a walk from $s$ to $v$; $\pm\infty$ allowed |
| $\delta_k(s,v)$ | least weight of a walk from $s$ to $v$ with at most $k$ edges |
| $d(v)$ | an algorithm's current estimate of $\delta(s,v)$ |
| $P(v)$ | parent pointer of $v$ in a search or shortest-path tree |
| `operation(args)` | an operation of an interface (sequence, set, priority queue), in code font |
