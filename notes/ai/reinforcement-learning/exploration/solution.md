<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs188hw-5-q1" status="draft"}
1. With probability $\varepsilon$ the agent acts uniformly at random among the four actions, otherwise it takes the best action $N$ (@def-epsilon-greedy). So
$$
p(N\mid s)=1-\varepsilon+\frac{\varepsilon}{4}=1-\frac{3\varepsilon}{4},\qquad p(E\mid s)=p(S\mid s)=p(W\mid s)=\frac{\varepsilon}{4}.
$$
(If the random choice is made only among the three other actions, the answers are $1-\varepsilon$ and $\varepsilon/3$.)
2. **$R-\sqrt{N}$, $R+\sqrt{1/(N+1)}$, $\sqrt{1/(N+1)}$ and $\exp(R-N)$.** A modified reward encourages new actions when it is larger for rarely taken pairs, that is, decreasing in $N(s,a)$; all four are. $R+\sqrt N$ rewards repetition, and $-\sqrt{1/(N+1)}$ is most negative ($-1$) for untried pairs and rises towards $0$, so both discourage exploring.
3. **Only $R+\sqrt{1/(N+1)}$.** As learning goes on, every pair is tried more and more often (the bonus sees to that), and this reward tends to $R(s,a,s')$, so the learnt Q-values tend to those of the original problem, as with an exploration function (@def-exploration-function). The others do not tend to $R$: $R-\sqrt N$ and $R+\sqrt N$ drift without bound, $\pm\sqrt{1/(N+1)}$ and $\exp(R-N)$ tend to $0$ and forget $R$ altogether.
:::
