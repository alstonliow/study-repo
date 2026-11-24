::: {.problem #prob-mit1803ps-10-q1 origin="external" source="mit1803ps-10-q1"}
[Autonomous Equations] This problem will use the Mathlet Phase Lines. Open the applet and understand its use and conventions. Click on [Phase Line] to see a representation of the phase line. Note the color coding: a green dot represents a stable or attracting equilibrium; a red dot represents an unstable or repelling equilibrium; and a blue dot represents a "semi-stable" equilibrium.

The Kenyan government has a game preserve that, in the absence of hunting, supports an oryx population that follows the logistic equation with a stable population of one kilo-oryx (one thousand animals). Kenya wishes to investigate the effect of various hunting rates $a$ on the oryx population.

(a) This situation is well modeled by the top menu item in Phase Lines. Explain why this is a good model. The rest of this problem will use this equation.

(b) It appears that there is a pair of equilibria for some values of $a$, only one for at least one other value of $a$, and none for still other values of $a$. Calculate which values of $a$ behave in which way. For each $a$ find the critical values of $y$ and in each case say whether the critical points involved are stable, unstable, or semi-stable.

(c) The Kenyan government hopes to allow 187.5 oryx to be killed in an average year. Determine the resulting stable population. If this strategy is adopted, what is the critical oryx population below which the population will crash (if the same harvest rate continues to be allowed)?

(d) For this value of $a$, there are five different behaviors possible for the oryx population. (Two solutions exhibit the "same behavior" if one is a time-translate of the other). Sketch one solution of each of the five types. Your sketch should make it clear what the behavior of the solution is as $t$ gets small and as $t$ gets large. Match each one up with a portion of the phase line.

(e) Invoke the Bifurcation Diagram for this autonomous equation. Move $a$ along its slider to see the variety of behaviors of the phase line of as $a$ varies. The green and red curve in the newly displayed bifurcation plane represents the equilibrium points for those equations for various values of $a$. Give an equation for that curve.

*Note (these notes):* The Java Mathlets this problem uses no longer run in most browsers; the solution answers the analytic parts and describes what the applet would show.
:::

::: {.problem #prob-mit1803ps-11-q1 origin="external" source="mit1803ps-11-q1"}
[Linear vs Nonlinear] Still working with the equation $\dot y = (1 - y)y - a$ with $a = \frac3{16}$, let $y_0$ be the stable critical point. Write $u = y - y_0$ for the population excess over equilibrium (so $u < 0$ if the population is less than the equilibrium value).

(a) Rewrite the differential equation as a differential equation for $u$. Check that the new equation is again autonomous and that $u = 0$ is a critical point for it.

(b) For small $u$ we can neglect higher powers of $u$ (such as $u^2$). This process is "linearization near equilibrium." What is the linearized equation near $u = 0$? What is the general solution of this linear autonomous equation?

(c) At least in this case, when solutions of the original autonomous equation get near equilibrium, they are well modeled by solutions of the linearization. Give an approximation of $y$ near equilibrium. Use it to answer this question: if $y(10) - y_0 = b$, estimate $y(11)$ and $y(12)$.

(d) Suppose that the linear equation $\dot x + p(t)x = q(t)$ is autonomous. What can you say about $p(t)$ and $q(t)$?
:::
