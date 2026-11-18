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

::: {.problem #prob-mit1801n-3c-q1 origin="external" source="mit1801n-3c-q1"}
Find the area under the graph of $y=1/\sqrt{x-2}$ for $3\le x\le6$
:::

::: {.problem #prob-mit1801n-3c-q2 origin="external" source="mit1801n-3c-q2"}
Calculate

a) $\displaystyle\int_0^2\sqrt{3x+5}\,dx$

*Note (these notes):* Only part (a) was assigned.
:::

::: {.problem #prob-mit1801n-3c-q3 origin="external" source="mit1801n-3c-q3"}
Calculate

a) $\displaystyle\int_1^2\frac{x\,dx}{x^2+1}$

*Note (these notes):* Only part (a) was assigned.
:::

::: {.problem #prob-mit1801n-3c-q5 origin="external" source="mit1801n-3c-q5"}
Find the area

a) under one arch of $\sin x$.

*Note (these notes):* Only part (a) was assigned.
:::

::: {.problem #prob-mit1801n-3d-q1 origin="external" source="mit1801n-3d-q1"}
a) Prove that $\displaystyle\int_0^x\frac{dt}{\sqrt{t^2+a^2}}=\ln\big(x+\sqrt{x^2+a^2}\big)-\ln a$, $a>0$, $x>0$.

b) For what $c$ is $\displaystyle\int_c^x\frac{dt}{\sqrt{t^2+a^2}}=\ln\big(x+\sqrt{x^2+a^2}\big)$?
:::

::: {.problem #prob-mit1801n-3d-q4 origin="external" source="mit1801n-3d-q4"}
Find a function whose derivative is $\sin(x^3)$ and whose value at 0 is

b) 2  c) find one whose value at 1 is $-1$

*Note (these notes):* Parts (b) and (c) were assigned.
:::

::: {.problem #prob-mit1801n-3d-q5 origin="external" source="mit1801n-3d-q5"}
Evaluate $\displaystyle\lim_{\Delta x\to0}\frac1{\Delta x}\int_1^{1+\Delta x}\frac{t}{\sqrt{1+t^4}}\,dt$ two ways:

a) by interpreting the integral as the area under a curve

b) by relation the limit to $F'(1)$, where $F(x)=\displaystyle\int_0^x\frac{t}{\sqrt{1+t^4}}\,dt$
:::

::: {.problem #prob-mit1801n-3d-q8 origin="external" source="mit1801n-3d-q8"}
Let $f(x)$ be continuous. Find $f(\pi/2)$ if:

a) $\displaystyle\int_0^xf(t)\,dt=2x(\sin x+1)$

*Note (these notes):* Only part (a) was assigned.
:::

::: {.problem #prob-mit1801n-3e-q1 origin="external" source="mit1801n-3e-q1"}
Prove directly from the definition $L(x)=\displaystyle\int_1^x\frac{dt}t$ that $L(\tfrac1a)=-L(a)$, by making a change of variables in the definite integral.
:::

::: {.problem #prob-mit1801n-3e-q2 origin="external" source="mit1801n-3e-q2"}
The function defined by $E(x)=\dfrac1{\sqrt{2\pi}}\displaystyle\int_0^xe^{-u^2/2}du$ is used in probability and statistics and has the same importance as sine and cosine functions have to trigonometry.

a) Express $E(x)$ in terms of the function of example 5 of Notes FT, $F(x)=\displaystyle\int_0^xe^{-t^2}dt$, by making a change of variable. It is known that $\displaystyle\lim_{x\to\infty}F(x)=\sqrt\pi/2$. What is $\displaystyle\lim_{x\to\infty}E(x)$?

c) Express $\dfrac1{\sqrt{2\pi}}\displaystyle\int_a^be^{-u^2/2}du$ in terms of the function $E$ and the constants $a$ and $b$, where $a<b$.

*Note (these notes):* Parts (a) and (c) were assigned.
:::

::: {.problem #prob-mit1801n-3e-q3 origin="external" source="mit1801n-3e-q3"}
Evaluate by making a substitution and changing both the variable and the limits of integration.

a) $\displaystyle\int_1^e\frac{\sqrt{\ln x}}{x}\,dx$ ($u=\ln x$)

*Note (these notes):* Only part (a) was assigned.
:::

::: {.problem #prob-mit1801n-3e-q6 origin="external" source="mit1801n-3e-q6"}
By comparing the given integral with an integral that is easier to evaluate, establish each of the following estimations:

b) $\displaystyle\int_0^\pi\sin^2x\,dx<2$  c) $\displaystyle\int_{10}^{20}\sqrt{x^2+1}\,dx>150$

*Note (these notes):* Parts (b) and (c) were assigned.
:::
