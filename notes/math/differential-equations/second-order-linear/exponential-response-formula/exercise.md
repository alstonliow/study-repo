::: {.problem #prob-mit1803ps-14-q1 origin="external" source="mit1803ps-14-q1"}
[Superposition; exponential response formula] Find the general real solution of:

(a) $\dot x + 2x = e^{3t}\cos(4t)$. (You could do this using an integrating factor, but it's easier to write the equation as the real part of a complex-valued equation with exponential right hand side, and use the ERF.)

(b) $\ddot x + \dot x + 2x = \cos t$. (Express the sinusoidal solution of this equation in two ways: as $a\cos t + b\sin t$, and as $A\cos(t - \phi)$.)

Now open the Mathlet Forced Damped Vibrations. As in Damped Vibrations, the initial conditions are set by the box at left. There is now a forcing term, $A\cos(\omega t)$, and the values of $A$ and $\omega$ are adjustable by sliders, as are the values of the mass, damping constant, and spring constant. The force in this system is applied directly to the mass (rather than being mediated by the spring or the dashpot).

Set $m = 1.00$, $b = 1.00$, and $k = 2.00$.

(c) Start by setting $A = 0.00$, so you are looking at the homogeneous case. Set the initial condition to $x(0) = 0$ and $\dot x(0) = 1$, select the Solution curve only, and measure the pseudoperiod. (Notice that a slider above the graphing window lets you adjust the vertical scale.) How well does your measurement agree with what you found in (b)?

(d) Now set $A = 1.00$ and $\omega = 1.00$. Select the green Steady State curve. Measure its amplitude and the value at $t = 0$. You computed this solution in (b). Compare the computed amplitude and value at $t = 0$ with what you measured. Also compute $\dot x_p(0)$.

(e) Finally, select initial condition $x(0) = 0$, $\dot x(0) = 0$: so-called rest initial conditions. (Clicking on a hashmark gives the exact value.) If you select Steady State, Transient, and Solution, you can see all three: $x = x_p + x_h$. Please compute $x_h$.

*Note (these notes):* The Java Mathlets this problem uses no longer run in most browsers; the solution answers the analytic parts and describes what the applet would show.
:::
