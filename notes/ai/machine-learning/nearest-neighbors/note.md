---
title: "Nearest Neighbour Classifiers"
sources: [cs231n-1, cs231na-1]
requires: [ai/machine-learning/regularization-and-model-selection]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Image classification: data-driven approach, k-nearest neighbour, validation) and Assignment 1 (k-NN), in our own wording; the example was computed with NumPy; the invariance proposition and its proof are our own. -->

The simplest data-driven classifier keeps the whole training set and labels a new input like the training inputs closest to it. It has no parameters to fit; its behaviour is set by a distance and by the number $k$ of neighbours, both chosen on validation data (@def-cross-validation).

::: {#def-lp-distance .definition name="L1 and L2 distances"}

For inputs flattened to vectors $\mathbf{x},\mathbf{x}'\in\mathbb{R}^D$ (an image of $h\times w$ pixels with $3$ colour channels gives $D=3hw$), the *$L_1$ distance* and the *$L_2$ distance* are

$$
d_1(\mathbf{x},\mathbf{x}')=\sum_{i=1}^{D}\lvert x_i-x'_i\rvert,\qquad d_2(\mathbf{x},\mathbf{x}')=\Bigl(\sum_{i=1}^{D}(x_i-x'_i)^2\Bigr)^{1/2}.
$$

:::

::: {#fig-nearest-neighbors-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[faint] (-1.4,0) -- (1.4,0) (0,-1.4) -- (0,1.4);
\draw[emph] (1,0) -- (0,1) -- (-1,0) -- (0,-1) -- cycle;
\draw[hl] (0,0) circle (1);
\draw[emph, dashed] (-1,-1) rectangle (1,1);
\node[tick] at (0.35,0.35) {$\ell_1$};
\node[tick, text=accent] at (0.95,0.62) {$\ell_2$};
\node[tick] at (1.25,1.15) {$\ell_\infty$};
\end{tikzpicture}
\end{center}
```

Unit balls of the $\ell_1$ (diamond), $\ell_2$ (circle) and $\ell_\infty$ (square) distances. Which points count as nearest depends on the distance chosen

:::

::: {#def-k-nearest-neighbors .definition name="k-nearest neighbour classifier"}

Given training data $(\mathbf{x}_1,y_1),\dots,(\mathbf{x}_N,y_N)$ with labels in $\{0,\dots,K-1\}$, a distance $d$ and an integer $k\ge1$, the *$k$-nearest neighbour classifier* predicts for an input $\mathbf{x}$ the label that occurs most often among the $k$ training points nearest to $\mathbf{x}$ under $d$. Ties between distances or between label counts are broken by a fixed rule, for example the smaller index or the smaller label. For $k=1$ it is the *nearest neighbour classifier*.

:::

::: {#fig-nearest-neighbors-3}

```{=latex}
\begin{center}
\begin{tikzpicture}
\node[hollow dot] at (0.94,0.31) {};
\node[hollow dot] at (1.58,0.46) {};
\node[hollow dot] at (0.27,1.20) {};
\node[hollow dot] at (3.67,2.40) {};
\node[hollow dot] at (3.06,0.67) {};
\node[hollow dot] at (2.15,0.83) {};
\node[hollow dot] at (0.69,0.32) {};
\node[hollow dot] at (0.86,2.78) {};
\node[hollow dot] at (3.32,2.42) {};
\node[dot] at (3.20,0.58) {};
\node[dot] at (1.24,1.88) {};
\node[dot] at (2.93,2.56) {};
\node[dot] at (3.52,0.26) {};
\node[dot] at (2.42,2.02) {};
\node[dot] at (2.02,0.53) {};
\node[dot] at (1.89,0.27) {};
\node[dot] at (3.74,2.60) {};
\node[dot] at (2.19,0.90) {};
\draw[hl] (2.0,1.5) circle (0.74);
\node[lab] at (2.0,1.5) {$\times$};
\end{tikzpicture}
\end{center}
```

$3$-nearest neighbours: the circle around the query $\times$ holds its three nearest training points, 2 filled and 1 hollow, so the majority vote predicts the filled class

:::

```{=latex}
\begin{algorithm}
\caption{$k$-nearest neighbour prediction}
\begin{algorithmic}
\INPUT training pairs $(\mathbf{x}_i,y_i)_{i=1}^N$, distance $d$, $k$, query $\mathbf{x}$
\OUTPUT predicted label
\FOR{$i=1$ \TO $N$}
    \STATE $d_i\gets d(\mathbf{x},\mathbf{x}_i)$
\ENDFOR
\STATE $S\gets$ indices of the $k$ smallest $d_i$
\FOR{each label $c$}
    \STATE $n_c\gets\lvert\{i\in S: y_i=c\}\rvert$
\ENDFOR
\RETURN the label $c$ with the largest $n_c$ (smallest such $c$ on a tie)
\end{algorithmic}
\end{algorithm}
```

::: {#exm-knn-seven-points .example name="Seven points, two values of k"}

Take class $0$ at $(0,0),(1,0),(0,1)$ and class $1$ at $(2,2),(3,2),(2,3),(1.2,1.4)$, and the query $\mathbf{x}=(1,1)$. The $L_2$ distances are $1.414,\ 1,\ 1,\ 1.414,\ 2.236,\ 2.236,\ 0.447$. The nearest point is $(1.2,1.4)$, so the $1$-NN prediction is $1$. The three nearest are $(1.2,1.4)$, $(1,0)$ and $(0,1)$, with labels $1,0,0$, so the $3$-NN prediction is $0$. The $L_1$ distances $2,1,1,2,3,3,0.6$ give the same neighbours here.

:::

::: {#fig-nearest-neighbors-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[->] (-0.4,0) -- (3.6,0) node[lab,anchor=west] {$x_1$};
\draw[->] (0,-0.4) -- (0,3.5) node[lab,anchor=south] {$x_2$};
\draw[faint, dashed] (1,1) circle (0.447);
\draw[hl, dashed] (1,1) circle (1.0);
\node[hollow dot] at (0,0) {};
\node[hollow dot] at (1,0) {};
\node[hollow dot] at (0,1) {};
\node[hl dot] at (2,2) {};
\node[hl dot] at (3,2) {};
\node[hl dot] at (2,3) {};
\node[hl dot] at (1.2,1.4) {};
\node[lab] at (1,1) {$\times$};
\node[lab,anchor=west] at (1.72,0.3) {$k=3$};
\node[lab,anchor=south east] at (0.72,1.38) {$k=1$};
\end{tikzpicture}
\end{center}
```

@exm-knn-seven-points: class $0$ hollow, class $1$ filled, query $\times$ at $(1,1)$. The small circle holds the nearest neighbour (class $1$); the large one the three nearest, two of class $0$, so the $3$-NN vote is $0$.

:::

::: {#prp-knn-cost .proposition name="Cost of nearest neighbour classification"}

Training stores the $N$ training vectors and costs no computation beyond the copy. Predicting one input costs $O(ND)$ time for the distances plus $O(N)$ to select the $k$ smallest. On the training set itself, $1$-NN with distinct training inputs has zero training error.

:::

::: {.proof}

1. Each of the $N$ distances in @def-lp-distance sums $D$ terms, so computing them costs $O(ND)$.
2. The $k$ smallest of $N$ numbers can be found in $O(N)$ time by linear-time selection, and counting their labels costs $O(k)\subseteq O(N)$.
3. For a training input $\mathbf{x}_i$, its distance to itself is $0$ and its distance to every other (distinct) training input is positive, so its nearest neighbour is itself and the prediction is $y_i$.

:::

The cost is the wrong way round for practice: training is free, while every prediction scans all the training data. Approximate nearest neighbour methods (trees, hashing, graph indices) trade some accuracy for faster queries.

::: {#prp-knn-invariance .proposition name="Which transformations leave k-NN unchanged"}

Apply the same map $T$ to all training and test inputs. The $k$-NN predictions do not change if every distance is multiplied by one positive constant $c$, that is, if $d(T\mathbf{x},T\mathbf{x}')=c\,d(\mathbf{x},\mathbf{x}')$ for all $\mathbf{x},\mathbf{x}'$. In particular:

1. Subtracting a fixed vector from all inputs (for example the mean image, or the per-pixel mean image) changes neither $d_1$ nor $d_2$.
2. Dividing all coordinates by one constant $\sigma>0$ scales $d_1$ and $d_2$ by $1/\sigma$.
3. An orthogonal map $T$ (a rotation of the coordinate axes) preserves $d_2$ but not, in general, $d_1$.

Dividing coordinate $i$ by its own $\sigma_i$ can change both.

:::

::: {.proof}

1. Predictions depend only on the order of the distances from the query to the training points. Multiplying all of them by $c>0$ keeps the order, including ties, so the neighbours and the vote are the same.
2. A shift $\mathbf{x}\mapsto\mathbf{x}-\boldsymbol\mu$ leaves every difference $\mathbf{x}-\mathbf{x}'$ unchanged, and both distances depend only on that difference; here $c=1$.
3. Scaling by $1/\sigma$ multiplies every difference, and so every $L_1$ and $L_2$ distance, by $1/\sigma$.
4. For orthogonal $Q$, $\lVert Q\mathbf{v}\rVert_2=\lVert\mathbf{v}\rVert_2$, so $c=1$ for $d_2$. For $d_1$, let $Q$ be the rotation of the plane by $45^\circ$. The difference $(1,0)$ becomes $(1,1)/\sqrt2$, so its $L_1$ norm goes from $1$ to $\sqrt2$; the difference $(1,-1)$ becomes $(\sqrt2,0)$, so its $L_1$ norm goes from $2$ to $\sqrt2$. The ratios $\sqrt2$ and $1/\sqrt2$ differ, so no single $c$ works, and the order of distances can change.
5. With per-coordinate scales, take $\sigma_1=1$, $\sigma_2=10$, a query $(0,0)$ and training points $(1,0)$ and $(0,2)$. Before scaling $(1,0)$ is nearer; after, the points are $(1,0)$ and $(0,0.2)$ and $(0,0.2)$ is nearer.

:::

::: {#rmk-nearest-neighbors-1 .remark name="Why pixel distances fail on images"}

On raw pixels, $d_1$ and $d_2$ measure colour and background more than content: an image shifted by one pixel, or darkened, can be far from the original, while two images of different objects on the same background can be close. Nearest neighbours on pixels therefore reach only about 35–40% accuracy on CIFAR-10 (ten classes). The same classifier on learnt features (@sec-ai-deep-learning-transfer-learning) works far better, which is the motivation for learning representations.

:::

::: {#rmk-nearest-neighbors-2 .remark name="Choosing k and the distance"}

$k$ and the distance are hyperparameters: pick them by validation or cross validation (@def-cross-validation), never on the test set. Small $k$ gives ragged decision boundaries and fits label noise; larger $k$ smooths the boundaries. With large models a single validation split is usually preferred to $k$-fold cross validation, which costs $k$ trainings per candidate.

:::
