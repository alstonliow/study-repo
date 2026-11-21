<!-- Solutions marked status="draft" were written by Claude in our own words, checked
     against the official answers; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-mit6046s15-8-q1" status="draft"}
(a) The feasible region is the pentagon with corners $(0,0)$, $(5,0)$, $(6,4)$, $(3,7)$, $(0,8)$:

```{=latex}
\begin{center}
\begin{tikzpicture}[x=0.55cm,y=0.55cm]
\draw[->] (0,0) -- (11,0) node[lab, anchor=west] {$x_1$};
\draw[->] (0,0) -- (0,10.5) node[lab, anchor=south] {$x_2$};
\fill[tintA] (0,0) -- (5,0) -- (6,4) -- (3,7) -- (0,8) -- cycle;
\draw[faint] (0,10) -- (10,0); \draw[faint] (5,0) -- (7.5,10); \draw[faint] (0,8) -- (10.5,4.5);
\foreach \p/\q in {0/0,5/0,6/4,3/7,0/8} \fill (\p,\q) circle[pt];
\draw[hl,->] (0,0) -- (5,0); \draw[hl,->] (5,0) -- (6,4);
\node[lab,tick, anchor=west] at (6.1,4.2) {$(6,4)$: $p=28$};
\node[lab,tick, anchor=north] at (5,-0.1) {$(5,0)$};
\end{tikzpicture}
\end{center}
```

(b) *Standard form:* maximise $4x_1+x_2$ subject to $x_1+x_2\le10$, $4x_1-x_2\le20$, $x_1+3x_2\le24$, $x_1,x_2\ge0$. *Slack form*, with slack variables $s_1,s_2,s_3\ge0$:
$$s_1=10-x_1-x_2,\quad s_2=20-4x_1+x_2,\quad s_3=24-x_1-3x_2,\quad p=4x_1+x_2.$$

(c) Start at the basic solution $x_1=x_2=0$, $p=0$.

1. *Pivot 1:* $x_1$ has the largest positive coefficient and enters. The bounds on $x_1$ from the three equations are $10$, $5$ and $24$, so $s_2$ leaves: $x_1=5+\frac14x_2-\frac14s_2$. Substituting, $s_1=5-\frac54x_2+\frac14s_2$, $s_3=19-\frac{13}4x_2+\frac14s_2$, $p=20+2x_2-s_2$. Solution $(x_1,x_2)=(5,0)$, $p=20$.
2. *Pivot 2:* $x_2$ enters (coefficient $2$). Its bounds are $4$ (from $s_1$) and $\frac{76}{13}$ (from $s_3$), so $s_1$ leaves: $x_2=4-\frac45s_1+\frac15s_2$. Then $x_1=6-\frac15s_1-\frac15s_2$, $s_3=6+\frac{13}5s_1-\frac25s_2$, $p=28-\frac85s_1-\frac35s_2$. Solution $(6,4)$, $p=28$.
3. All coefficients in $p$ are now negative, so $(6,4)$ is optimal with $p=28$. The path $(0,0)\to(5,0)\to(6,4)$ is marked on the diagram.

(d) The dual is: minimise $10y_1+20y_2+24y_3$ subject to $y_1+4y_2+y_3\ge4$, $y_1-y_2+3y_3\ge1$, $y_1,y_2,y_3\ge0$ (@def-dual-lp). The final coefficients of the slacks give $y=(\frac85,\frac35,0)$, which is feasible ($\frac85+\frac{12}5=4$, $\frac85-\frac35=1$) with value $16+12=28$; by weak duality (@thm-weak-duality) both are optimal, and the optimal value is $28$.
:::

::: {.solution for="prob-mit18065ps-24-q2" status="draft"}
1. A corner has two of the three variables equal to zero: $(4,0,0)$, $(0,4,0)$, $(0,0,2)$.

2. Costs: $20$, $12$, $16$. The minimum is at $(0,4,0)$ with cost $12$. A linear cost on the triangle is minimised at a corner, so this is the minimum over the whole triangle.
:::
