<!-- Adapted (own wording) from UC Berkeley EECS 70, Fall 2020, Note 13, §3.7 "The Monty Hall Problem". TODO: source (CS70 is not yet a registered resource, SPEC §17.12). -->

::: {#exm-monty-hall .example name="The Monty Hall problem" level="medium"}
A prize is behind one of three doors and the other two hide nothing. You pick
a door. The host knows where the prize is and opens one of the other two
doors, always one without the prize. You may then keep your door or switch to
the remaining closed one. Should you switch?

**Intuition misleads.** With two closed doors left, it is tempting to give
each probability $\frac12$. But your first pick is right with probability
$\frac13$, and opening an empty door does not change that. So the other
closed door must hold the prize with probability $\frac23$.

**Sample space.** To check this, write an outcome as a triple $(i,j,k)$: the
prize is behind door $i$, you pick door $j$, and the host opens door $k$. The
host never opens the prize door or your door, so only $12$ triples are
possible. Assume:

- the prize is equally likely to be behind each door;
- you pick each door with probability $\frac13$;
- when you have picked the prize door, the host opens either of the other two
  with probability $\frac12$.

**Probabilities of the outcomes.** Multiply along the choices
(@prp-multiplication-rule).

- If $i\neq j$, the host has only one door to open, so
  $\Pr(i,j,k)=\frac13\cdot\frac13\cdot1=\frac19$. There are $6$ such outcomes.
- If $i=j$, the host has two doors to choose from, so
  $\Pr(i,j,k)=\frac13\cdot\frac13\cdot\frac12=\frac1{18}$. There are $6$ such
  outcomes.

As a check, $6\cdot\frac19+6\cdot\frac1{18}=1$.

**Switching.** Switching wins exactly when your first pick was wrong, that is
when $i\neq j$. Then the host opens the other empty door and you switch to the
prize. So
$$
\Pr(\text{win by switching}) = 6\cdot\tfrac19 = \tfrac23,
\qquad
\Pr(\text{win by keeping}) = 6\cdot\tfrac1{18} = \tfrac13 .
$$
You should switch.

**Lesson.** Work systematically. Name the sample space, give each outcome its
probability, describe the event as a set of outcomes, and add up.
:::
