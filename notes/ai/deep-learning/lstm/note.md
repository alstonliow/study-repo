---
title: "Long Short-Term Memory"
sources: [cs231n-12]
requires: [ai/deep-learning/recurrent-neural-networks]
status: draft
---

<!-- Added 2026-11-21 from Stanford CS231n course notes (Recurrent neural networks: LSTM formulation, does the LSTM solve the vanishing gradient problem), in our own wording; the cell-gradient proposition, its proof and the numbers (computed in Python) are our own. -->

By @thm-rnn-gradient-flow, the gradient of a vanilla RNN passes through one matrix product with $W_{hh}$ and one $\tanh$ derivative per step, and typically vanishes over long spans. The *long short-term memory* (LSTM) adds a second state, the *cell*, which is updated additively and elementwise.

::: {#def-lstm .definition name="LSTM"}

An *LSTM* with hidden size $m$ has a weight matrix $W\in\mathbb{R}^{4m\times(m+d)}$ and a bias $\mathbf{b}\in\mathbb{R}^{4m}$. At step $t$, from $\mathbf{h}_{t-1}$, $\mathbf{c}_{t-1}$ and the input $\mathbf{x}_t$, it computes

$$
\begin{pmatrix}\mathbf{a}_i\\\mathbf{a}_f\\\mathbf{a}_o\\\mathbf{a}_g\end{pmatrix}=W\begin{pmatrix}\mathbf{h}_{t-1}\\\mathbf{x}_t\end{pmatrix}+\mathbf{b},\qquad
\mathbf{i}=\sigma(\mathbf{a}_i),\ \ \mathbf{f}=\sigma(\mathbf{a}_f),\ \ \mathbf{o}=\sigma(\mathbf{a}_o),\ \ \mathbf{g}=\tanh(\mathbf{a}_g),
$$

$$
\mathbf{c}_t=\mathbf{f}\odot\mathbf{c}_{t-1}+\mathbf{i}\odot\mathbf{g},\qquad \mathbf{h}_t=\mathbf{o}\odot\tanh(\mathbf{c}_t),
$$

with each $\mathbf{a}$ in $\mathbb{R}^m$. The *input gate* $\mathbf{i}$, *forget gate* $\mathbf{f}$ and *output gate* $\mathbf{o}$ have entries in $(0,1)$; $\mathbf{g}$ is the candidate written to the cell.

:::

::: {#fig-lstm-2}

```{=latex}
\begin{center}
\begin{tikzpicture}
\draw[emph, ->] (0,2) -- (7,2);
\node[tick, left] at (0,2) {$\mathbf c_{t-1}$};
\node[tick, right] at (7,2) {$\mathbf c_t$};
\node[small vertex] (m) at (2,2) {$\odot$};
\node[small vertex] (a) at (4,2) {$+$};
\node[box] (f) at (2,0.6) {$\mathbf f$};
\node[box] (i) at (3.2,0.6) {$\mathbf i$};
\node[box] (g) at (4.8,0.6) {$\mathbf g$};
\node[box] (o) at (6,0.6) {$\mathbf o$};
\node[small vertex] (ig) at (4,1.45) {$\odot$};
\draw[map] (f) -- (m);
\draw[map] (i) -- (ig);
\draw[map] (g) -- (ig);
\draw[map] (ig) -- (a);
\node[small vertex] (oh) at (6,-0.6) {$\odot$};
\draw[map] (o) -- (oh);
\draw[map] (5.4,2) |- node[tick, pos=0.2, right] {$\tanh$} (oh);
\draw[map] (oh) -- (7,-0.6) node[tick, right] {$\mathbf h_t$};
\node[hl box] (in) at (4,-1.2) {$\mathbf h_{t-1},\ \mathbf x_t$};
\draw[faint] (in) -- (2,-0.2) (in) -- (3.2,-0.2) (in) -- (4.8,-0.2) (in) -- (6,-0.2);
\end{tikzpicture}
\end{center}
```

The LSTM cell: the gates $\mathbf f,\mathbf i,\mathbf o$ and the candidate $\mathbf g$ are computed from $\mathbf h_{t-1}$ and $\mathbf x_t$. Along the top line the cell state is only scaled by $\mathbf f$ and added to, which is why gradients survive many steps

:::

Read entrywise: the forget gate decides how much of each cell entry to keep, the input gate how much of the candidate to add, and the output gate how much of the cell to reveal as the hidden state, which is what the next step and the output layer see.

```{=latex}
\begin{algorithm}
\caption{One LSTM step}
\begin{algorithmic}
\INPUT $\mathbf{x}_t$, $\mathbf{h}_{t-1}$, $\mathbf{c}_{t-1}$, $W$, $\mathbf{b}$
\OUTPUT $\mathbf{h}_t$, $\mathbf{c}_t$
\STATE $\mathbf{a}\gets W[\mathbf{h}_{t-1};\mathbf{x}_t]+\mathbf{b}$; split $\mathbf{a}$ into four blocks of size $m$
\STATE $\mathbf{i},\mathbf{f},\mathbf{o}\gets\sigma$ of the first three blocks; $\mathbf{g}\gets\tanh$ of the fourth
\STATE $\mathbf{c}_t\gets\mathbf{f}\odot\mathbf{c}_{t-1}+\mathbf{i}\odot\mathbf{g}$
\STATE $\mathbf{h}_t\gets\mathbf{o}\odot\tanh(\mathbf{c}_t)$
\RETURN $\mathbf{h}_t,\mathbf{c}_t$
\end{algorithmic}
\end{algorithm}
```

::: {#prp-lstm-cell-gradient .proposition name="The cell path has no matrix product"}

Holding the gates fixed (the path that goes from $\mathbf{c}_{t-1}$ to $\mathbf{c}_t$ directly, not through $\mathbf{h}_{t-1}$), $\partial\mathbf{c}_t/\partial\mathbf{c}_{t-1}=\operatorname{diag}(\mathbf{f}_t)$, and along this path

$$
\frac{\partial\mathbf{c}_t}{\partial\mathbf{c}_s}=\operatorname{diag}\Bigl(\prod_{k=s+1}^{t}\mathbf{f}_k\Bigr)\qquad(s<t),
$$

an elementwise product of forget gates.

:::

::: {.proof}

1. In $\mathbf{c}_t=\mathbf{f}_t\odot\mathbf{c}_{t-1}+\mathbf{i}_t\odot\mathbf{g}_t$, with $\mathbf{f}_t,\mathbf{i}_t,\mathbf{g}_t$ held fixed, entry $j$ of $\mathbf{c}_t$ depends on $\mathbf{c}_{t-1}$ only through $f_{t,j}c_{t-1,j}$, so the Jacobian is $\operatorname{diag}(\mathbf{f}_t)$.
2. The chain rule over steps $s+1,\dots,t$ multiplies these diagonal matrices, which gives the elementwise product.

:::

::: {#fig-lstm-1}

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[->] (0,0) -- (5.61,0) node[lab,anchor=west] {steps $t-s$};
\draw[->] (0,-3.15) -- (0,0.54) node[lab,anchor=south] {$\log_{10}$ factor};
\draw[tick] (0,0.0) -- (-0.08,0.0) node[lab,anchor=east] {$0$};
\draw[tick] (0,-0.9) -- (-0.08,-0.9) node[lab,anchor=east] {$-2$};
\draw[tick] (0,-1.8) -- (-0.08,-1.8) node[lab,anchor=east] {$-4$};
\draw[tick] (0,-2.7) -- (-0.08,-2.7) node[lab,anchor=east] {$-6$};
\draw[tick] (1.1,0) -- (1.1,0.08) node[lab,anchor=south] {$10$};
\draw[tick] (2.2,0) -- (2.2,0.08) node[lab,anchor=south] {$20$};
\draw[tick] (3.3,0) -- (3.3,0.08) node[lab,anchor=south] {$30$};
\draw[tick] (4.4,0) -- (4.4,0.08) node[lab,anchor=south] {$40$};
\draw[tick] (5.5,0) -- (5.5,0.08) node[lab,anchor=south] {$50$};
\draw[faint] (0.000,-0.000) -- (0.110,-0.148) -- (0.220,-0.295) -- (0.330,-0.443) -- (0.440,-0.590) -- (0.550,-0.738) -- (0.660,-0.885) -- (0.770,-1.033) -- (0.880,-1.180) -- (0.990,-1.328) -- (1.100,-1.476) -- (1.210,-1.623) -- (1.320,-1.771) -- (1.430,-1.918) -- (1.540,-2.066) -- (1.650,-2.213) -- (1.760,-2.361) -- (1.870,-2.508) -- (1.980,-2.656) -- (2.090,-2.804) -- (2.200,-2.951) -- (2.310,-3.099);
\draw[hl] (0.000,-0.000) -- (0.110,-0.009) -- (0.220,-0.019) -- (0.330,-0.028) -- (0.440,-0.038) -- (0.550,-0.047) -- (0.660,-0.057) -- (0.770,-0.066) -- (0.880,-0.076) -- (0.990,-0.085) -- (1.100,-0.095) -- (1.210,-0.104) -- (1.320,-0.114) -- (1.430,-0.123) -- (1.540,-0.133) -- (1.650,-0.142) -- (1.760,-0.152) -- (1.870,-0.161) -- (1.980,-0.171) -- (2.090,-0.180) -- (2.200,-0.190) -- (2.310,-0.199) -- (2.420,-0.209) -- (2.530,-0.218) -- (2.640,-0.228) -- (2.750,-0.237) -- (2.860,-0.247) -- (2.970,-0.256) -- (3.080,-0.266) -- (3.190,-0.275) -- (3.300,-0.285) -- (3.410,-0.294) -- (3.520,-0.304) -- (3.630,-0.313) -- (3.740,-0.323) -- (3.850,-0.332) -- (3.960,-0.342) -- (4.070,-0.351) -- (4.180,-0.361) -- (4.290,-0.370) -- (4.400,-0.380) -- (4.510,-0.389) -- (4.620,-0.399) -- (4.730,-0.408) -- (4.840,-0.418) -- (4.950,-0.427) -- (5.060,-0.437) -- (5.170,-0.446) -- (5.280,-0.456) -- (5.390,-0.465) -- (5.500,-0.475);
\node[lab,anchor=west] at (0.99,-2.52) {vanilla RNN, factor $0.47$ per step};
\node[lab,anchor=north] at (3.96,-0.855) {LSTM cell, $f=\sigma(3)$};
\end{tikzpicture}
\end{center}
```

How much of the gradient survives $t-s$ steps: along the LSTM cell path with forget gates $\sigma(3)\approx0.953$ (highlighted, @prp-lstm-cell-gradient) against a vanilla RNN whose per-step factor is about $0.47$, as in @exm-rnn-gradient-flow (faint, shown until it falls below $10^{-7}$).

:::

So the gradient along the cell is never multiplied by $W$ and never passes a squashing derivative: it is scaled only by forget gates, which the network learns and can hold near $1$ for the entries it must remember. With $f=\sigma(3)\approx0.953$ the factor over $10$ steps is $0.62$ and over $50$ steps $0.088$, against the factor $0.104$ after just three steps in @exm-rnn-gradient-flow. Initializing the forget-gate bias to a positive value such as $1$ or $3$ starts the network in this remembering regime.

::: {#rmk-lstm-1 .remark name="What the LSTM does and does not fix"}

The LSTM does not guarantee the absence of vanishing gradients: the forget gates can be small, and the other paths (through $\mathbf{h}_{t-1}$ and the gates) behave like a vanilla RNN. It does provide a path along which information and gradients can survive over many steps, as the identity path of a residual connection (@def-residual-connection) does across layers. Exploding gradients are still handled by clipping (@def-gradient-clipping). The *gated recurrent unit* (GRU) is a simpler variant with two gates and no separate cell; in practice both work comparably.

:::
