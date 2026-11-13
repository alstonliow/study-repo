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

## Probability (`math/probability`)

<!-- TODO: 1058note chapter 11 has no probability section. Add symbols during migration of chapter 9. -->
