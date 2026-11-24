::: {.problem #prob-mit1803ps-13-q1 origin="external" source="mit1803ps-13-q1"}
[Second order linear equations] Saloon doors can swing through the door frame. A good door damper will slow a swinging door down so that either it comes to rest without swinging through, or, if you shove the door hard toward the frame, it swings through and comes to rest from the other side. This is a characteristic of "overdamping."

This problem will study the saloon door effect, using the Mathlet Damped Vibration. Open the applet, which is about solutions of the second order homogeneous equation $m\ddot x + b\dot x + kx = 0$. The initial conditions are set using the box at left. In it the horizontal direction gives $x(0)$ and the vertical direction gives $\dot x(0)$. The right graphing window displays the corresponding solution. You can set the mass $m$, the damping constant $b$, and the spring constant $k$, using sliders at lower left. You can invoke a window showing the roots of the characteristic polynomial by clicking the [Roots] button.

Move the cursor around in the initial conditions box and observe the behavior of the left end of the graph in the right window. Verify for yourself that the slope of the solution at $t = 0$ increases when the horizontal coordinate increases, and that the value increases when the vertical coordinate increases. These coordinates can also be controlled using the sliders along the edge of the initial conditions box. The evolution can be animated using the [»] key, and the time slider lets you adjust the value of $t$ at will. The pair $(x(t), \dot x(t))$ traces out a curve in the left window. Clicking [Relate diagrams] creates a line segment illustrating a relationship between the two windows.

Fix the constants at $m = 0.50$, $b = 1.5$, and $k = 0.625$. (You'll have to content yourself with $k = 0.62$ on the applet, but use $k = 0.625 = 5/8$ in your calculations.)

(a) What is the characteristic polynomial? Verify that the displayed roots are correct.

(b) What is the general solution? Express it in terms of the initial conditions $x(0) = x_0$, $\dot x(0) = \dot x_0$.

(c) For what initial conditions $(x_0, \dot x_0)$ is the solution "exponential"—that is, of the form $ce^{rt}$ (rather than a sum of such terms)?

(d) Suppose the initial position is fixed at $x(0) = x_0$. Take $x_0 = 0.25$ to illustrate this on the mathlet. Use the mathlet to investigate what values of $\dot x_0$ lead to solutions which become zero for some postive value of $t$. This is asking: how hard to I have to push this saloon door in order to make it swing through its closed position and return from the other side?

Now resolve this question analytically; give the precise range of values of $\dot x_0$ for which the corresponding solution is zero for some positive value of $t$. Your answer will come out in terms of $x_0$. Does it match up with your observation using the applet?

*Note (these notes):* The Java Mathlets this problem uses no longer run in most browsers; the solution answers the analytic parts and describes what the applet would show.
:::

::: {.problem #prob-mit1803ps-13-q2 origin="external" source="mit1803ps-13-q2"}
[Complex roots] This problem will continue to use the same applet.

(a) Keep $m = 0.50$ and $k = .625$, but decrease the damping constant. At what value do the roots become equal? Verify this algebraically. For this value of $b$, what is the general solution of the differential equation $m\ddot x + b\dot x + kx = 0$?

(b) Now push $b$ even lower, to $b = 0.25$. Pick a nonzero initial condition $(x_0, \dot x_0)$, invoke Relate diagrams, and animate the solution. Verify that the readout of the roots is correct, and give the general solution of the equation.

(c) With these values of $m$, $b$, and $k$, set the initial conditions to $x(0) = 1$, $\dot x(0) = 0$. Using the cross-hairs, measure the successive distances between the first five zeros of the solution. What does the theory predict they will be? Does the door oscillate faster, slower, or just the same as it comes to rest? What is the pseudo-period of this solution?

Now make the same measurements for your choice of different initial conditions. What do you observe? What does the theory say about the distance between successive zeros of the general solution?

*Note (these notes):* The Java Mathlets this problem uses no longer run in most browsers; the solution answers the analytic parts and describes what the applet would show.
:::
