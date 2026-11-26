---
title: "Burnside's Lemma"
sources: []
requires: [math/discrete/counting/combinations, math/discrete/number-theory/euler-totient]
status: draft
---

<!-- Added 2026-11-26 for the CSES problems Counting Necklaces and Counting Grids, in our own wording. TODO: add a source. -->

Two colourings of the beads of a necklace are "the same" if a rotation turns one into the other. Counting colourings up to such symmetries is the job of Burnside's lemma.

::: {#def-symmetry-group .definition name="Symmetries and orbits"}

Let $X$ be a finite set (the colourings) and $G$ a finite set of permutations of $X$ that contains the identity, is closed under composition, and contains the inverse of each of its members. Two elements $x,y\in X$ are *equivalent* if $y=g(x)$ for some $g\in G$; the equivalence classes are the *orbits*. For $g\in G$ let $\operatorname{Fix}(g)=\{x\in X: g(x)=x\}$ and for $x\in X$ let $\operatorname{Stab}(x)=\{g\in G: g(x)=x\}$.

:::

::: {#thm-burnside .theorem name="Burnside's lemma"}

The number of orbits is

$$
\frac1{|G|}\sum_{g\in G}|\operatorname{Fix}(g)|.
$$

:::

::: {.proof}

1. *Double counting.* Count the pairs $(g,x)$ with $g(x)=x$ in two ways: $\sum_{g}|\operatorname{Fix}(g)|=\sum_{x}|\operatorname{Stab}(x)|$.

2. *Orbit–stabiliser.* The map $g\mapsto g(x)$ sends $G$ onto the orbit of $x$, and two elements have the same image iff they differ by an element of $\operatorname{Stab}(x)$, so each fibre has $|\operatorname{Stab}(x)|$ elements. Hence $|G|=|\operatorname{Orb}(x)|\cdot|\operatorname{Stab}(x)|$.

3. *Sum over an orbit.* For $x$ in an orbit $O$, $|\operatorname{Stab}(x)|=|G|/|O|$, so the elements of $O$ contribute $|O|\cdot|G|/|O|=|G|$ to the sum of step 1.

4. *Conclusion.* The sum of step 1 equals $|G|$ times the number of orbits.

:::

::: {#exm-burnside-lemma-1 .example name="Necklaces"}

Colour the $n$ beads of a necklace with $k$ colours, where rotations count as the same. The rotation by $i$ positions splits the beads into $\gcd(i,n)$ cycles, and a colouring is fixed iff each cycle is monochromatic, so $|\operatorname{Fix}|=k^{\gcd(i,n)}$ and the number of necklaces is

$$
\frac1n\sum_{i=0}^{n-1}k^{\gcd(i,n)}=\frac1n\sum_{d\mid n}\varphi(d)\,k^{n/d}.
$$

For $n=4$, $k=2$: $\frac14(2^4+2^1+2^2+2^1)=6$.

:::

::: {#fig-burnside-lemma-1}

```{=latex}
\begin{center}
\begin{tikzpicture}
\foreach \k in {0,1,2,3} {
  \foreach \a [count=\j from 0] in {90,0,270,180} {
    \pgfmathtruncatemacro{\m}{mod(\j-\k+4,4)}
    \ifnum\m=0 \node[hl ball] at ({2.4*\k+0.7*cos(\a)},{0.7*sin(\a)}) {};
    \else \node[ball] at ({2.4*\k+0.7*cos(\a)},{0.7*sin(\a)}) {};\fi
  }
}
\end{tikzpicture}
\end{center}
```

@exm-burnside-lemma-1: one necklace of four beads (one bead of colour 2) and its three rotations. The four pictures are one orbit, so they count as one necklace.

:::

::: {#rmk-burnside-lemma-1 .remark name="Grids under rotation"}

For an $n\times n$ grid with $k$ colours and the four rotations, the identity fixes $k^{n^2}$ colourings, the rotations by $90^\circ$ and $270^\circ$ fix $k^{\lceil n^2/4\rceil}$ each, and the rotation by $180^\circ$ fixes $k^{\lceil n^2/2\rceil}$ (count the cycles of the cell permutation). The number of distinct grids is $\bigl(k^{n^2}+2k^{\lceil n^2/4\rceil}+k^{\lceil n^2/2\rceil}\bigr)/4$. Modulo a prime the division by $|G|$ is a multiplication by a modular inverse.

:::
