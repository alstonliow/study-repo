<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs188hw-5-q2" status="draft"}
Values were checked by value iteration in Python.

1. **$V^*(A)=6.25$, $V^*(B)=12.5$, $V^*(C)=25$, $V^*(D)=50$.** A move succeeds with probability $\frac12$; failure ends in a $0$ exit. So each value is half the value of the better neighbour: $V^*(D)=\max\bigl(\frac12\cdot100,\frac12V^*(C)\bigr)=50$, then $V^*(C)=\frac12\max(V^*(B),V^*(D))=25$, $V^*(B)=\frac12\max(V^*(A),25)=12.5$, $V^*(A)=\frac12\max(1,12.5)=6.25$. The optimal policy goes Right everywhere.
2. **Yes, $r=51$.** Each step from $A,\dots,D$ earns $r$. If $r$ is large it pays to stay in the middle row as long as possible, moving back and forth; then every middle value $V$ satisfies $V=r+\frac12V$, so $V=2r$. At $D$, Left is worth $r+\frac12V^*(C)$ and Right $r+\frac12\cdot100$, so Left is strictly better exactly when $V^*(C)>100$. With $r=50$ all middle values are $100$ and Left and Right tie at $D$; with $r=51$ they are $102$, and Left ($102$) beats Right ($101$). For $r\le49$, $V^*(C)<100$ and Right is better. (If the Exit step also earns $r$, all values shift but the threshold is the same: tie at $r=50$, Left only from $r=51$.)
3. **$(B,\text{Left})=1$, $(B,\text{Right})=100$, $(C,\text{Left})=0$, $(C,\text{Right})=100$.** Q-learning (@def-q-learning) on replayed data converges to the optimal Q-values of the MDP the data describes, here deterministic: $Q(\text{X1},\text{Exit})=1$, $Q(A,\text{Left})=1$, $Q(B,\text{Left})=\max_aQ(A,a)=1$ (the untried $Q(A,\text{Right})$ stays $0$); along the other episode every Q-value becomes $100$. $(C,\text{Left})$ never occurs in the data, so it keeps its initial value $0$.
4. **False.** With features $f(s)$ that ignore the action, $Q(s,a)=\mathbf w\cdot f(s)$ is the same for every action in a state (@def-q-function-approximation). But the optimal Q-values differ between actions, for instance $Q^*(D,\text{Right})=50$ and $Q^*(D,\text{Left})=\frac12V^*(C)=12.5$ in part 1, so no such weights represent them.
:::
