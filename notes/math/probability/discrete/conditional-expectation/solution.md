<!-- Solutions marked status="draft" were written by Claude in our own words, 
     no official solutions were available. Owner to review, then remove status. -->

::: {.solution for="prob-mit6042f10-12-q3" status="draft"}
(a) Each problem set takes $1\cdot\frac23+2\cdot\frac13=\frac43$ days on average, so $E[B]=3\cdot\frac43=4$ by linearity.

(b) $R+1$ is the number of rolls up to the first $1$, which is $\mathrm{Geom}(\frac16)$ with mean $6$ (@prp-standard-distributions-1-4). So $E[R]=5$.

(c) The dice are independent, so $E[U]=E[X]E[Y]=\frac72\cdot\frac72=\frac{49}4$ (@thm-expectation-of-product).

(d) By the law of total expectation (@thm-total-expectation), $E[D]=\frac12\cdot4+\frac13\cdot5+\frac16\cdot\frac{49}4=\frac{48+40+49}{24}=\frac{137}{24}\approx5.71$.
:::

::: {.solution for="prob-mit6042f10-12-q5" status="draft"}
(a) By linearity: true/false $10\cdot2\cdot\frac34=15$; the four $15$-point questions $4\cdot(7+3)=40$; the $20$-point question $15$. Total $70$.

(b) The product of two independent dice has mean $\frac72\cdot\frac72=\frac{49}4$, and the general impression has mean $0.4\cdot40+0.3\cdot50+0.3\cdot60=49$. Total $\frac{49}4+49=61.25$.

(c) By the law of total expectation (@thm-total-expectation), $\frac47\cdot70+\frac27\cdot61.25+\frac17\cdot84=40+17.5+12=69.5$.
:::

::: {.solution for="prob-mit6041f10-4-q1" status="draft"}
The six points have weights $x^2+y^2$: $(1,1)\colon2$, $(1,3)\colon10$, $(2,1)\colon5$, $(2,3)\colon13$, $(4,1)\colon17$, $(4,3)\colon25$.

(a) The weights sum to $72$, so $c=1/72$.
(b) $Y<X$ at $(2,1),(4,1),(4,3)$: $\frac{47}{72}$.
(c) $Y>X$ at $(1,3),(2,3)$: $\frac{23}{72}$.
(d) $Y=X$ only at $(1,1)$: $\frac2{72}=\frac1{36}$.
(e) $\frac{10+13+25}{72}=\frac23$.
(f) $p_X(1)=\frac{12}{72}=\frac16$, $p_X(2)=\frac{18}{72}=\frac14$, $p_X(4)=\frac{42}{72}=\frac7{12}$; $p_Y(1)=\frac{24}{72}=\frac13$, $p_Y(3)=\frac23$.
(g) $E[X]=\frac16+\frac12+\frac73=3$, $E[Y]=\frac13+2=\frac73$, and $E[XY]=\frac1{72}\sum xy\,(x^2+y^2)=\frac{488}{72}=\frac{61}9$.
(h) $E[X^2]=\frac16+1+\frac{28}3=\frac{21}2$, so $\mathrm{Var}(X)=\frac32$; $E[Y^2]=\frac13+6=\frac{19}3$, so $\mathrm{Var}(Y)=\frac89$. With $\mathrm{Cov}(X,Y)=\frac{61}9-7=-\frac29$,
$$\mathrm{Var}(X+Y)=\tfrac32+\tfrac89-\tfrac49=\tfrac{35}{18}.$$
(i) $A$ consists of $(1,1),(2,1),(4,1),(4,3)$ with total weight $49$. Given $A$, $X$ is $1,2,4$ with probabilities $\frac2{49},\frac5{49},\frac{42}{49}$. So $E[X\mid A]=\frac{2+10+168}{49}=\frac{180}{49}$, $E[X^2\mid A]=\frac{2+20+672}{49}=\frac{694}{49}$, and
$$\mathrm{Var}(X\mid A)=\frac{694}{49}-\Bigl(\frac{180}{49}\Bigr)^2=\frac{1606}{2401}\approx0.669.$$
:::
