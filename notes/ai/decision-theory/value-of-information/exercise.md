::: {.problem #prob-cs188hw-8-q1 origin="external" source="cs188hw-8-q1"}
**Phase.** The EECS department decides to offer an exciting new course, CS1888, next semester. You and your friends are deciding if you want to take it or not, and decide to draw inspiration from CS188 and model this using decision networks. For all of the following parts, $A$ represents the action of taking CS1888 or not, and $U$ represents the utility function of a specific student.

1. Your friend Lexy will only take CS1888 if a specific instructor will be teaching it ($I$), and doesn't care about the course size or curriculum. However, due to uncertainty in instructor hiring practices in the university, the instructor chosen to teach is affected by the outcome of instructor collective bargaining efforts ($B$). The collective bargaining outcome will also affect the size of the course ($S$).

   Select all of the decision networks which can represent Lexy's decision.

   ```{=latex}
   \begin{center}
   \begin{tikzpicture}[x=1cm, y=1cm, scale=0.8, every node/.append style={transform shape}]
   \begin{scope}[xshift=0.0cm]
   \node[box] (A) at (2,2) {$A$};
   \node[diamond, draw=ink, fill=accentSoft, aspect=1.5] (U) at (3.4,1.5) {$U$};
   \node[vertex] (B) at (0.6,1) {$B$};
   \node[vertex] (I) at (2,0.8) {$I$};
   \node[vertex] (S) at (2,-0.4) {$S$};
   \draw[->] (A) -- (U);
   \draw[->] (B) -- (I);
   \draw[->] (I) -- (U);
   \draw[->] (B) -- (S);
   \node[lab] at (2,-1.3) {(1)};
   \end{scope}
   \begin{scope}[xshift=5.2cm]
   \node[box] (A) at (2,2) {$A$};
   \node[diamond, draw=ink, fill=accentSoft, aspect=1.5] (U) at (3.4,1.5) {$U$};
   \node[vertex] (B) at (0.6,1) {$B$};
   \node[vertex] (I) at (2,0.8) {$I$};
   \node[vertex] (S) at (2,-0.4) {$S$};
   \draw[->] (A) -- (U);
   \draw[->] (B) -- (I);
   \draw[->] (I) -- (U);
   \draw[->] (B) -- (S);
   \draw[->] (S) -- (U);
   \node[lab] at (2,-1.3) {(2)};
   \end{scope}
   \begin{scope}[xshift=10.4cm]
   \node[box] (A) at (2,2) {$A$};
   \node[diamond, draw=ink, fill=accentSoft, aspect=1.5] (U) at (3.4,1.5) {$U$};
   \node[vertex] (B) at (0.6,1) {$B$};
   \node[vertex] (I) at (2,0.8) {$I$};
   \node[vertex] (S) at (2,-0.4) {$S$};
   \draw[->] (A) -- (U);
   \draw[->] (B) -- (I);
   \draw[->] (I) -- (U);
   \draw[->] (U) -- (S);
   \draw[->] (S) -- (B);
   \node[lab] at (2,-1.3) {(3)};
   \end{scope}
   \begin{scope}[xshift=15.600000000000001cm]
   \node[vertex] (A) at (2,2) {$A$};
   \node[diamond, draw=ink, fill=accentSoft, aspect=1.5] (U) at (3.4,1.5) {$U$};
   \node[vertex] (B) at (0.6,1) {$B$};
   \node[vertex] (I) at (2,0.8) {$I$};
   \node[vertex] (S) at (2,-0.4) {$S$};
   \draw[->] (A) -- (U);
   \draw[->] (B) -- (I);
   \draw[->] (I) -- (U);
   \draw[->] (B) -- (S);
   \node[lab] at (2,-1.3) {(4)};
   \end{scope}
   \end{tikzpicture}
   \end{center}
   ```



   (1) (2) (3) (4) None of the above

Your friend Varun is also making the same decision. His decision is represented by the following decision network, where the chance nodes correspond to the following random variables:

- $O$: if classes will be online next semester
- $V$: the current virus situation
- $M$: the chancellor's message about how optimistic the university is about the virus situation
- $F$: whether Varun's friend takes CS1888
- $C$: whether Varun's friend's crush takes CS1888

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1.2cm, y=1.1cm]
\node[box] (A) at (1.6,1.2) {$A$};
\node[diamond, draw=ink, fill=accentSoft, aspect=1.5] (U) at (3,0.6) {$U$};
\node[vertex] (V) at (0,0) {$V$};
\node[vertex] (O) at (1.6,0) {$O$};
\node[vertex] (M) at (1.6,-1.3) {$M$};
\node[vertex] (F) at (3,-0.8) {$F$};
\node[vertex] (C) at (4.4,0) {$C$};
\draw[->] (A) -- (U);
\draw[->] (V) -- (O);
\draw[->] (V) -- (M);
\draw[->] (O) -- (M);
\draw[->] (O) -- (U);
\draw[->] (C) -- (F);
\draw[->] (F) -- (U);
\end{tikzpicture}
\end{center}
```

**Each variable has a binary domain.** The conditional probability tables of variables are known, but not represented here.

2. We want $P(F,O\mid c)$, where $c$ is a value that C can take on. Which of the following algorithms could be used for calculating this?

   Forward Algorithm $\quad$ Prior Sampling $\quad$ Inference by Enumeration $\quad$ Particle Filtering $\quad$ None of the above

Varun wants to reason about the VPI of observing different evidence variables. For the following two statements, select if they are always, sometimes, or never true.

3. $\mathrm{VPI}(F)\ge\mathrm{VPI}(C)$

   Always true $\quad$ Sometimes true $\quad$ Never true
4. $\mathrm{VPI}(O\mid V)+\mathrm{VPI}(V\mid O)>\mathrm{VPI}(V,O)$

   Always true $\quad$ Sometimes true $\quad$ Never true
5. Varun peeks at his friend's crush's CalCentral and sees whether she is taking CS1888 ($C=c'$). Which of the following formulas represents the highest utility he has now?
   - $\max_a\sum_f\sum_oP(f,o\mid c')U(f,o,a)$
   - $\max_a\sum_fP(f\mid c')U(f,a)$
   - $\sum_cP(c)\bigl[\max_a\sum_f\sum_oP(f,o\mid c')U(f,o,a)\bigr]$
   - $\sum_cP(c)\bigl[\max_a\sum_fP(f\mid c')U(f,a)\bigr]$

*Note (these notes):* Networks redrawn; rectangles are action nodes, diamonds utility nodes.
:::
