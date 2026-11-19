<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-cs221hw-4-q1" status="draft"}
With $\gamma=1$, $Q_i(s,a)=\sum_{s'}T(s,a,s')\big(\text{Reward}(s,a,s')+V^*_{i-1}(s')\big)$ and $V^*_i(s)=\max_a Q_i(s,a)$. End states keep value $0$; moving to $-2$ earns $10$, to $+2$ earns $50$, any other move $-5$.

**(a)** Iteration $i=1$ (all $V^*_0=0$):

1. $s=-1$: $a_1$: $0.8(10)+0.2(-5)=7$; $a_2$: $0.7(10)+0.3(-5)=5.5$. Max $7$.
2. $s=0$: $a_1$: $0.8(-5)+0.2(-5)=-5$; $a_2$: $0.7(-5)+0.3(-5)=-5$. Max $-5$.
3. $s=+1$: $a_1$: $0.8(-5)+0.2(50)=6$; $a_2$: $0.7(-5)+0.3(50)=11.5$. Max $11.5$.

So $V^*_1=(0,\ 7,\ -5,\ 11.5,\ 0)$ on $(-2,-1,0,+1,+2)$.

Iteration $i=2$:

1. $s=-1$: $a_1$: $0.8(10)+0.2(-5-5)=6$; $a_2$: $0.7(10)+0.3(-5-5)=4$. Max $6$.
2. $s=0$: $a_1$: $0.8(-5+7)+0.2(-5+11.5)=2.9$; $a_2$: $0.7(-5+7)+0.3(-5+11.5)=3.35$. Max $3.35$.
3. $s=+1$: $a_1$: $0.8(-5-5)+0.2(50)=2$; $a_2$: $0.7(-5-5)+0.3(50)=8$. Max $8$.

So $V^*_2=(0,\ 6,\ 3.35,\ 8,\ 0)$.

**(b)** Using $V^*_2$:

1. $s=-1$: $a_1$: $0.8(10)+0.2(-5+3.35)=7.67$; $a_2$: $0.7(10)+0.3(-5+3.35)=6.505$. $\pi^*(-1)=a_1$.
2. $s=0$: $a_1$: $0.8(-5+6)+0.2(-5+8)=1.4$; $a_2$: $0.7(-5+6)+0.3(-5+8)=1.6$. $\pi^*(0)=a_2$.
3. $s=+1$: $a_1$: $0.8(-5+3.35)+0.2(50)=8.68$; $a_2$: $0.7(-5+3.35)+0.3(50)=13.845$. $\pi^*(+1)=a_2$.
:::

::: {.solution for="prob-cs188hw-4-q1" status="draft"}
All numbers were checked by value iteration (@def-value-iteration) in Python. In the first grid only exiting pays, so a plan that exits from a square after $k$ moves is worth $\gamma^{k}$ times that square's reward. From $H$: Up enters $E$ at once ($-25\gamma$); Left leads along $H,G,D,A$ ($125\gamma^{3}$); Right leads to $I$ and then $F$ ($25\gamma^{2}$). ($I$ cannot reach $C$ without entering $F$.) Down from $H$ stays in place; it only wastes a step, and with $\gamma=1$ its Q-value $\gamma V^*(H)$ merely ties with the optimal one, so like the handout we compare Up, Left and Right.

1. **Left:** $125$ against $25$ and $-25$.
2. **Left and Right (tie):** $125\cdot\frac{1}{125}=1$ and $25\cdot\frac{1}{25}=1$, both above $-5$.
3. **Right:** $25\cdot\frac{1}{100}=0.25$ beats $125\cdot\frac{1}{1000}=0.125$.
4. **0.9 and 1** (exactly $p>\frac34$). With $\gamma=1$, $V(G)=125$ and $V(E)=-25$. Left is worth $Q_L=-25p+125(1-p)=125-150p$. Right is worth $Q_R=p\,V(I)-25(1-p)$ with $V(I)=\max(25,V(H))$. Where Right is optimal, $V(H)=Q_R<25$, so $V(I)=25$ and $Q_R=50p-25$; then $Q_R>Q_L$ iff $200p>150$. For $p=0.9$: $Q_R=20>-10=Q_L$; for $p=0.5$: Left gives $50$ while Right gives only $12.5$.
5. **0.5, 0.9 and 1** (exactly $p>\frac{21}{43}\approx0.488$). Now $V(D)=12.5$, $V(G)=1.25$ and $V(I)=\gamma\cdot25=2.5$, so
$$
Q_R=\tfrac1{10}\bigl(2.5p-25(1-p)\bigr)=2.75p-2.5,\qquad Q_L=\tfrac1{10}\bigl(-25p+1.25(1-p)\bigr)=0.125-2.625p,
$$
and $Q_R>Q_L$ iff $5.375p>2.625$; both beat Up ($-2.5$) for $p>0$. (If staying in place forever, worth $0$, is admitted as an option, Right is strictly best only when $Q_R>0$, that is $p>\frac{10}{11}$, leaving only $p=1$.)
6. **$V^*(A)=100$, $V^*(C)=100$, $\pi^*(A)=$ Right.** From $C$, Down enters $D$ for $+100$ (Up gives $-100$, Right $-50$, Left back to $A$). From $A$, Right reaches $C$ for $0+100$, while Down costs $-1$ at $B$ before reaching $D$ ($99$).
7. **$V(A)=25$, $V(C)=25$.** Without Left, the two best actions at $C$ are Down ($100$) and Right ($-50$), so $V(C)=\frac12\cdot100+\frac12\cdot(-50)=25$, and $A$ still goes Right: $V(A)=0+25=25$.
8. **$V(A)=99$, $\pi(A)=$ Down.** Going Right is now worth $25$, while Down to $B$ ($-1$) and then Right to $D$ ($+100$) is worth $99$.
:::
