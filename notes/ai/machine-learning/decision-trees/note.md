---
title: "Decision Trees"
sources: [cs188-23]
requires: [ai/machine-learning/generalization]
status: draft
---

<!-- Added 2026-11-19 from UC Berkeley CS188 (Fall 2025), Lecture 23 (inductive learning, consistency versus simplicity, decision trees, expressiveness, choosing an attribute by information gain, entropy, overfitting, significance of a split, pruning), in our own wording; the cycling data is our own and the entropies were computed in Python. Decision trees for lower bounds on sorting are a different use of the name (@sec-cs-data-structures-comparison-lower-bounds). -->

Linear classifiers and neural networks score inputs with weighted sums. A decision tree classifies by a sequence of questions about single attributes, which people can read and check. Learning one illustrates a theme of all learning: many hypotheses fit the training data, and the simplest one consistent with it tends to generalise best (*Ockham's razor*).

::: {#def-decision-tree-classifier .definition name="Decision tree"}

For inputs described by discrete *attributes* $A_1,\dots,A_n$, a *decision tree* is a rooted tree whose internal nodes are labelled by attributes, with one outgoing branch per value of the attribute, and whose leaves are labelled by outputs. To classify an input, start at the root, follow the branch for the input's value of the node's attribute, and output the label of the leaf reached.

:::

Decision trees can express every function of the attributes: a tree that tests all attributes along every path has one leaf per combination of values. For $n$ Boolean attributes there are $2^{2^{n}}$ Boolean functions, so the hypothesis class is enormous, much larger than that of a linear classifier (which cannot even represent exclusive or of two attributes), and a tree that fits the training data perfectly can always be found when no two examples with equal attributes have different labels. The aim is a *small* consistent tree; finding the smallest is NP-hard, so trees are grown greedily, choosing at each node the attribute that best separates the labels.

::: {#def-entropy-information-gain .definition name="Entropy, information gain"}

The *entropy* of a distribution $(p_1,\dots,p_k)$ is
$$
H(p_1,\dots,p_k)=-\sum_{i=1}^{k}p_i\log_2p_i\quad(\text{with }0\log_20=0),
$$
measured in *bits*. For a set $S$ of labelled examples, $H(S)$ is the entropy of the label frequencies in $S$. Splitting $S$ on attribute $A$ into the subsets $S_v=\{x\in S: A(x)=v\}$ leaves the *remaining entropy* $\sum_v\frac{|S_v|}{|S|}H(S_v)$, and the *information gain* of $A$ is
$$
\mathrm{IG}(S,A)=H(S)-\sum_v\frac{|S_v|}{|S|}H(S_v).
$$

:::

Entropy is the average number of yes/no questions needed to identify a label drawn from the distribution, with an optimal code: $1$ bit for a fair coin, $0$ for a certain outcome, $\log_2k$ for $k$ equally likely values. Information gain is never negative (conditioning cannot increase entropy on average) and is $0$ for an attribute independent of the label in $S$.

::: {#def-decision-tree-learning .definition name="Greedy decision tree learning"}

To learn a tree from a set $S$ of examples and a set of attributes:

1. if all examples in $S$ have the same label, or no attributes are left, return a leaf with the most frequent label of $S$ (if $S$ is empty, that of the parent's examples);
2. otherwise choose the attribute $A$ with the largest $\mathrm{IG}(S,A)$, create a node testing $A$, and for each value $v$ learn a subtree from $S_v$ and the remaining attributes.

:::

```{=latex}
\begin{algorithm}
\caption{Greedy decision tree learning}
\begin{algorithmic}
\INPUT Examples $S$, attributes $\mathcal A$, default label $d$
\OUTPUT A decision tree
\FUNCTION{Learn}{$S,\mathcal A,d$}
    \IF{$S=\emptyset$}
        \RETURN leaf $d$
    \ELSIF{all examples in $S$ have one label, or $\mathcal A=\emptyset$}
        \RETURN leaf with the most frequent label in $S$
    \ENDIF
    \STATE $A\gets\operatorname{arg\,max}_{A'\in\mathcal A}\mathrm{IG}(S,A')$
    \STATE $m\gets$ most frequent label in $S$
    \FOR{each value $v$ of $A$}
        \STATE attach \CALL{Learn}{$S_v,\mathcal A\setminus\{A\},m$} as the branch $A=v$
    \ENDFOR
    \RETURN the node testing $A$
\ENDFUNCTION
\end{algorithmic}
\end{algorithm}
```

::: {#exm-decision-tree-cycling .example name="Who cycles to work?"}

Eight commuters are described by weather (sunny or rainy) and distance (short or long). On sunny days all four cycle; on rainy days one of two short-distance commuters cycles and neither of two long-distance ones does. So $5$ of $8$ cycle and $H(S)=H(\tfrac58,\tfrac38)\approx0.954$ bits.

- Weather: the sunny subset is pure ($H=0$), the rainy subset has $1$ of $4$ cycling ($H\approx0.811$); remaining entropy $\tfrac12\cdot0+\tfrac12\cdot0.811\approx0.406$, so $\mathrm{IG}\approx0.549$.
- Distance: short has $3$ of $4$ cycling ($H\approx0.811$), long $2$ of $4$ ($H=1$); remaining entropy $\approx0.906$, so $\mathrm{IG}\approx0.049$.

The root tests weather; the sunny branch is a leaf "cycles". On the rainy branch the only attribute left, distance, has gain $0.811-\tfrac12\cdot1=0.311$, and splits it into "long: does not cycle" and "short", a leaf with one example of each label, where the most frequent label is a tie.

:::

::: {#fig-decision-trees-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm]
\node[box] (w) at (0,0) {weather?};
\node[hl box] (y) at (-1.6,-1.3) {cycles};
\node[box] (d) at (1.6,-1.3) {distance?};
\node[hl box] (n) at (0.6,-2.6) {does not cycle};
\node[box] (t) at (2.9,-2.6) {tie (1 : 1)};
\draw (w) -- node[edge label] {sunny} (y);
\draw (w) -- node[edge label] {rainy} (d);
\draw (d) -- node[edge label] {long} (n);
\draw (d) -- node[edge label] {short} (t);
\end{tikzpicture}
\end{center}
```

The tree learnt greedily in @exm-decision-tree-cycling: weather has the larger information gain ($0.549$ against $0.049$ bits) and is tested first; distance then splits the rainy examples.

:::

::: {#rmk-decision-tree-overfitting .remark name="Overfitting and pruning"}

Grown until every leaf is pure, a tree fits the training data exactly, including its noise, and overfits (@def-overfitting) badly on data with many attributes: with enough attributes, some split will separate a handful of examples by chance. Two remedies limit the tree. One stops early or limits the depth, a hyperparameter tuned on held-out data. The other grows the full tree and then *prunes* splits whose gain is not statistically significant: a $\chi^{2}$ test compares the label counts in the branches with those expected if the attribute were irrelevant (each branch receiving the parent's label proportions), and the split is removed when the deviation is plausible as chance. Both trade a worse fit to the training data for better generalisation.

:::
