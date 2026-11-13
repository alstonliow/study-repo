<!-- Migrated from 1058note exercises/chapters (CN end-of-chapter exercises). -->

::: {.problem #prob-propositional-04 origin="external" source="fit1058-cn-4.21-q4"}
Prove the two Distributive Laws ((4.2) and (4.3) in §4.14).
:::

::: {.problem #prob-propositional-05 origin="external" source="fit1058-cn-4.21-q5"}
Do you need parentheses in $a\wedge b\vee c$? Investigate
$a\wedge(b\vee c)$ and $(a\wedge b)\vee c$. Are they logically equivalent? If
not, does either imply the other?
:::

::: {.problem #prob-propositional-07 origin="external" source="fit1058-cn-4.21-q7"}
Simplify as much as possible using Boolean algebra:
$$(\neg X\wedge\neg Y)\vee(\neg X\wedge Y)\vee(X\wedge Y).$$
:::

::: {.problem #prob-propositional-08 origin="external" source="fit1058-cn-4.21-q8"}
This question is about using Boolean algebra to describe the
algebra of switching.

An electrical switch is represented diagrammatically as follows.

The state of a switch can be represented by a Boolean variable,
with the states Off and On being represented by *False* and
*True* respectively. Let $x$ be a Boolean variable
representing the state of a switch. Then $x = \textit{True}$
represents the switch being On, so that electrical current can pass
through it; $x = \textit{False}$ represents the switch being Off,
so that there is no electrical current through the switch.

We can put switches together to make more complicated circuits.
Those circuits can then be described by Boolean expressions in the
variables that represent the switches. In the following circuits,
$v,w,x,y,z$ are Boolean variables representing the indicated
switches.

(a) For each of the two switching circuits below, write a
    Boolean expression in $x$ and $y$ for the proposition that
    current flows between the two ends of the circuit. (The
    ends are shown as $A$ and $B$ in the diagram. In effect,
    the diagrams only show part of a complete circuit. The
    rest of the circuit would contain a power supply, such as
    a battery, and an electrical device that operates when the
    current flows, such as a light or an appliance.)

    ```{=latex}
\begin{center}
            \begin{circuitikz}[scale=1]
                \draw (0,0) node[left]{$A$} to[switch, l=$x$] (2,0)
                    to[switch, l=$y$] (4,0) node[right]{$B$};
            \end{circuitikz}
```

    ```{=latex}
\begin{circuitikz}[scale=1]
                \draw (0,0) node[left]{$A$} -- (0.6,0);
                \draw (0.6,0.6) to[switch, l=$x$] (2.6,0.6);
                \draw (0.6,-0.6) to[switch, l_=$y$] (2.6,-0.6);
                \draw (0.6,0) -- (0.6,0.6);
                \draw (0.6,0) -- (0.6,-0.6);
                \draw (2.6,0.6) -- (3.2,0.6) -- (3.2,0);
                \draw (2.6,-0.6) -- (3.2,-0.6) -- (3.2,0);
                \draw (3.2,0) -- (3.8,0) node[right]{$B$};
            \end{circuitikz}
            \end{center}
```

(b) For each of the next two circuits, again construct a
    Boolean expression to represent the proposition that
    current flows between the two ends of the circuit. Compare
    the two expressions you construct. What can you say about
    the relationship between them?

    ```{=latex}
\begin{center}
            \begin{circuitikz}[scale=1]
                \draw (0,0) node[left]{$A$} -- (0.6,0);
                \draw (0.6,0.5) to[switch, l=$v$] (2,0.5);
                \draw (0.6,-0.5) to[switch, l_=$w$] (2,-0.5);
                \draw (0.6,0) -- (0.6,0.5);
                \draw (0.6,0) -- (0.6,-0.5);
                \draw (2,0.5) -- (2.4,0);
                \draw (2,-0.5) -- (2.4,0);
                \draw (2.4,0.5) to[switch, l=$y$] (3.8,0.5);
                \draw (2.4,-0.5) to[switch, l_=$z$] (3.8,-0.5);
                \draw (2.4,0) -- (2.4,0.5);
                \draw (2.4,0) -- (2.4,-0.5);
                \draw (3.8,0.5) -- (4.2,0);
                \draw (3.8,-0.5) -- (4.2,0);
                \draw (4.2,0) -- (4.8,0) node[right]{$B$};
            \end{circuitikz}
            \end{center}
```

(c) Similarly, construct Boolean expressions for the next
    two circuits. Compare the two expressions you construct.
    What can you say about the relationship between them?

    ```{=latex}
\begin{center}
            \begin{circuitikz}[scale=1]
                \coordinate (A) at (0,0);
                \coordinate (N1) at (1.6,0.9);
                \coordinate (N2) at (1.6,-0.9);
                \coordinate (B) at (4.4,0);
                \draw (A) node[left]{$A$} -- (0.4,0.9) to[switch, l=$v$] (N1);
                \draw (A) -- (0.4,-0.9) to[switch, l_=$w$] (N2);
                \draw (N1) to[switch, l=$y$] (3.6,0.9) -- (B);
                \draw (N2) to[switch, l_=$z$] (3.6,-0.9) -- (B);
                \draw (N1) to[switch, l=$x$] (N2);
                \draw (B) -- (4.8,0) node[right]{$B$};
            \end{circuitikz}
            \end{center}
```

(d) For each of our circuit pairs in (a)–(c), discuss how
    they are related to each other, and what this means for
    how the Boolean expressions derived from them are related
    to each other.
:::

::: {.problem #prob-propositional-13 origin="external" source="fit1058-cn-4.21-q13"}
We saw two distributive laws for $\vee$ and $\wedge$, versus only one for $+$
and $\times$ on numbers. Investigate the situation for $\oplus$ and $\wedge$.
Do you have two distributive laws, one (which one?), or none? Explain.
:::
