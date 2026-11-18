::: {.problem #prob-mit1801f06-6-q2 origin="external" source="mit1801f06-6-q2"}
The voltage $V$ of house current is given by
$$V(t)=C\sin(120\pi t)$$
where $t$ is time, in seconds and $C$ is a constant amplitude. The square root of the average value of $V^2$ over one period of $V(t)$ (or cycle) is called the root-mean-square voltage, abbreviated RMS. This is what the voltage meter on a house records. For house current, find the RMS in terms of the constant $C$. (The peak voltage delivered to the house is $\pm C$. The units of $V^2$ are square volts; when we take the square root again after averaging, the units become volts again.)

*Note (these notes):* Problem 1 of Problem Set 7 repeats this problem word for word and is not added again.
:::

::: {.problem #prob-mit1801f06-6-q3 origin="external" source="mit1801f06-6-q3"}
a) What is the probability that $x^2<y$ if $(x,y)$ is chosen from the unit square $0\le x\le1$, $0\le y\le1$ with probability equal to the area.

b) What is the probability that $x^2<y$ if $(x,y)$ is chosen from the square $0\le x\le2$, $0\le y\le2$ with probability proportional to the area. (Probability = Part/Whole).

c) Evaluate
$$W=\int_0^\infty e^{-at}\,dt=\lim_{N\to\infty}\int_0^Ne^{-at}\,dt$$
This is known as an improper integral because it represents the area of an unbounded region. We are using the letter $W$ to signify "whole."

The probability that a radioactive particle will decay some time in the interval $0\le t\le T$ is
$$P([0,T])=\frac{\text{PART}}{\text{WHOLE}}=\frac1W\int_0^Te^{-at}\,dt$$
Note that $P([0,\infty))=1=100\%$.

d) The half-life is the time $T$ for which $P([0,T])=1/2$. Find the value of $a$ and $W$ for which the half-life is $T=1$. Suppose that a radioactive particle has a half-life of 1 second. What is the probability that it survives to time $t=1$, but decays some time during the interval $1\le t\le2$? (Give an integral formula, and use a calculator to get an approximate numerical answer.)
:::
