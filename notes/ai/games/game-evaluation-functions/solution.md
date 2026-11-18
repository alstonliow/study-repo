<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-5-q1" status="draft"}
$$V_{\text{minmax}}(s,d)=\begin{cases}
\text{Utility}(s) & \text{if } \text{IsEnd}(s),\\
\text{Eval}(s) & \text{else if } d=0,\\
\max_{a\in\text{Actions}(s)} V_{\text{minmax}}(\text{Succ}(s,a),d) & \text{else if } \text{Player}(s)=0,\\
\min_{a\in\text{Actions}(s)} V_{\text{minmax}}(\text{Succ}(s,a),d) & \text{else if } 1\le\text{Player}(s)<n,\\
\min_{a\in\text{Actions}(s)} V_{\text{minmax}}(\text{Succ}(s,a),d-1) & \text{else if } \text{Player}(s)=n.
\end{cases}$$

1. End states return their true utility; at depth $0$ the search stops and estimates with $\text{Eval}$.
2. Pac-Man (agent $0$) maximises; ghosts $1,\dots,n$ each minimise, in turn, at the same depth.
3. The depth decreases only after the last ghost (agent $n$) has moved, so one unit of depth is one move of all $n+1$ agents.
:::

::: {.solution for="prob-cs221hw-5-q3" status="draft"}
$$V_{\text{exptmax}}(s,d)=\begin{cases}
\text{Utility}(s) & \text{if } \text{IsEnd}(s),\\
\text{Eval}(s) & \text{else if } d=0,\\
\max_{a\in\text{Actions}(s)} V_{\text{exptmax}}(\text{Succ}(s,a),d) & \text{else if } \text{Player}(s)=0,\\
\frac{1}{|\text{Actions}(s)|}\sum_{a\in\text{Actions}(s)} V_{\text{exptmax}}(\text{Succ}(s,a),d) & \text{else if } 1\le\text{Player}(s)<n,\\
\frac{1}{|\text{Actions}(s)|}\sum_{a\in\text{Actions}(s)} V_{\text{exptmax}}(\text{Succ}(s,a),d-1) & \text{else if } \text{Player}(s)=n.
\end{cases}$$

1. The cases are those of the minimax recurrence (Problem 1a); only the ghosts' layers change.
2. A random ghost picks each legal action with probability $1/|\text{Actions}(s)|$, so its node takes the average of its children instead of the minimum.
3. Pac-Man still maximises, now the expected utility, and the depth still decreases after ghost $n$.
:::
