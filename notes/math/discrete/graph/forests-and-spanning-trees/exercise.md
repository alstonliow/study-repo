<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-graph-2-07 origin="external" source="fit1058-cn-12.7-q7"}
How many spanning trees does the following graph have?

```{=latex}
\begin{center}
    \begin{tikzpicture}[every node/.style={circle,fill,inner sep=1.8pt}]
        \node[label=left:$a$] (a) at (0,1.4) {};
        \node[label=above:$b$] (b) at (1.4,1.4) {};
        \node[label=left:$c$] (c) at (0,0) {};
        \node[label=below:$d$] (d) at (1.4,0) {};
        \node[label=below:$e$] (e) at (2.6,0.7) {};
        \node[label=right:$f$] (f) at (3.8,0.7) {};
        \draw (a)--(b)--(d)--(c)--(a);
        \draw (b)--(e)--(d);
        \draw (e)--(f);
    \end{tikzpicture}
    \end{center}
```
:::

::: {.problem #prob-graph-2-08 origin="external" source="fit1058-cn-12.7-q8"}
Apply Kruskal’s Greedy Algorithm to find a minimum weight spanning tree in the
following weighted graph.

```{=latex}
\begin{center}
    \begin{tikzpicture}[every node/.style={circle,fill,inner sep=1.8pt},
                        lab/.style={fill=none,draw=none,inner sep=1pt,font=\small}]
        \node[label=below:$a$] (a) at (0,0) {};
        \node[label=below:$c$] (c) at (2,0) {};
        \node[label=below:$e$] (e) at (4,0) {};
        \node[label=above:$b$] (b) at (1,1.7) {};
        \node[label=above:$d$] (d) at (3,1.7) {};
        \node[label=above:$f$] (f) at (5,1.7) {};
        \draw (b)--node[lab,above]{1}(d);
        \draw (d)--node[lab,above]{6}(f);
        \draw (a)--node[lab,left]{9}(b);
        \draw (b)--node[lab,left]{3}(c);
        \draw (c)--node[lab,left]{2}(d);
        \draw (d)--node[lab,right]{4}(e);
        \draw (e)--node[lab,right]{7}(f);
        \draw (a)--node[lab,below]{8}(c);
        \draw (c)--node[lab,below]{5}(e);
    \end{tikzpicture}
    \end{center}
```
:::
