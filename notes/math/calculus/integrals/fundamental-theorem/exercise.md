::: {.problem #prob-mit1801f06-5-q1 origin="external" source="mit1801f06-5-q1"}
a) Suppose that at the beginning of day 0, some time last summer, the temperature in Boston was $y(0)=65^\circ$ Fahrenheit and that over a 50-day period, the temperature increased according to the rule $y'(t)=y(t)/100$, with time $t$ measured in days. Find the formula for $y$, and draw a graph of temperature on days 3 and 4, $3\le t\le5$, and label with the correct day and shade in the regions whose areas represent the average temperature each of the two days.$^2$

b) The number of cooling degree days is the sum for each day of the difference between the average temperature for that day and $65^\circ$. The number is used to estimate the demand for electricity for air conditioning. Draw a second graph of $y$ for the whole 50 days and shade in the region whose area represents the total number of degree days. Write a formula for this total area as the difference between $65\cdot50$ and a definite integral. Evaluate the definite integral using the fundamental theorem of calculus. (Alternatively, write the whole quantity as an integral expressing the area between curves as in Lecture 21, and 7.2.)

c) (extra credit) Compute the definite integral in part (b) directly by evaluating a lower Riemann sum and taking a limit. Follow the procedure in Problem 5, PS4, but with different scale factors. This rather elaborate calculation shows how much time and effort we save every time we use the fundamental theorem and the change of variable formula in integrals.

$^2$ The continuous average of a function is
$$\frac1{b-a}\int_a^bf(x)\,dx$$
In this case $b-a=1$, so the average is the same as integral. For more, see Notes, AV, and Lecture 23.
:::

::: {.problem #prob-mit1801f06-5-q2 origin="external" source="mit1801f06-5-q2"}
Consider the function $f(x)=\int_0^x\cos(t^2)\,dt$. There is no expression for $f(x)$ in terms of standard elementary functions. It is known as a Fresnel integral, along with the corresponding sine integral.

a) Draw a rough sketch of $\cos(t^2)$, showing the first positive and negative zeros. What does the curve look like at $t=0$? Is the function even or odd?

b) List the critical points of $f(x)$ in the entire range $-\infty<x<\infty$. Which critical points are local maxima and which ones are local minima?

c) Sketch the graph of $f$ on the interval $-2\le x\le2$, with labels for the critical points and inflection points. (The drawing should be qualitatively correct, but just estimate the values of $f$ at the labelled points.)

d) Estimate $f(0.1)$ to six decimal places.

e) Fresnel integrals are sometimes expressed using different scaling of the variables.

i) Let $g(x)=\int_0^x\cos((\pi/2)u^2)\,du$. Make a change of variables to show that $f(x)=c_1g(c_2x)$ for some constants $c_1$ and $c_2$. Why did we choose the factor $\pi/2$?

ii) Let $h(x)=\int_0^x\frac{\cos v}{\sqrt v}\,dv$. (This integral is called improper because $1/\sqrt v$ is infinite$^3$ at $v=0$.) Make a different change of variable to show that $f(x)=ch(x^2)$ for some constant $c$ (assume that $x>0$).

iii) Let $k(x)=\sqrt x\int_0^1\cos(xt^2)\,dt$, $x>0$. Use the change of variable $z=xt^2$ and part (ii) to find the relationship between the functions $k$ and $f$. Hint: Which quantities are variable and which are constant? (Not assigned: you can also work out this relationship using a change of variables like the one in part (i).)

$^3$ Although the integrand is infinite, the area under the curve is finite. The function $h$ is continuous, $h(0)=0$, but its graph has infinite slope at $x=0$.
:::
