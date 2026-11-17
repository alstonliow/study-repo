<!-- Adapted (own wording) from UC Berkeley CS 70, Fall 2020, Note 21 (source key cs70-21, in note.md); checked numerically. -->

::: {#exm-web-chain-invariant .example name="A five-page web" level="medium"}
Five pages $A,B,C,D,E$ link as follows: $A\to B,D$; $B\to C$; $C\to A$; $D\to A,B,E$; $E\to B,C$. A surfer follows a uniformly random link, so the transition matrix (rows and columns in the order $A,\dots,E$) is
$$P=\begin{pmatrix}0&\frac12&0&\frac12&0\\0&0&1&0&0\\1&0&0&0&0\\\frac13&\frac13&0&0&\frac13\\0&\frac12&\frac12&0&0\end{pmatrix}.$$
The chain is irreducible: $A\to D\to E\to C\to A$ and $A\to B\to C$ form walks through all pages and back to $A$.

Set $\pi(A)=1$ and drop the balance equation for $A$. The others are
$$\pi(B)=\tfrac12\pi(A)+\tfrac13\pi(D)+\tfrac12\pi(E),\quad \pi(C)=\pi(B)+\tfrac12\pi(E),\quad \pi(D)=\tfrac12\pi(A),\quad \pi(E)=\tfrac13\pi(D).$$
Solve from the right: $\pi(D)=\frac12$, $\pi(E)=\frac16$, $\pi(B)=\frac12+\frac16+\frac1{12}=\frac34$, $\pi(C)=\frac34+\frac1{12}=\frac56$. These sum to $\frac{39}{12}$; multiply by $\frac{12}{39}$:
$$\pi=\tfrac1{39}(12,\,9,\,10,\,6,\,2).$$
Check the dropped equation: $\pi(A)=\pi(C)+\frac13\pi(D)=\frac{10+2}{39}$. The pages rank $A,C,B,D,E$.
:::
