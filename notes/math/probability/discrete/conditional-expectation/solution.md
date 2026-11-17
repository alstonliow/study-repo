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
