::: {.problem #prob-mit6042f10-7-q3 origin="external" source="mit6042f10-7-q3"}
(a) Use integration to find upper and lower bounds that differ by at most 0.1 for the following sum. (You may need to add the first few terms explicitly and then use integrals to bound the sum of the remaining terms.)
$$\sum_{i=1}^{\infty} \frac{1}{(2i + 1)^2}$$

(b) Assume $n$ is an integer larger than 1. Which of the following inequalities, if any, hold. You may find the graph helpful.

1. $\displaystyle\sum_{i=1}^{n} \ln(i + 1) \le \int_0^n \ln(x + 2)\,dx$
2. $\displaystyle\sum_{i=1}^{n} \ln(i + 1) \le \ln 2 + \int_1^n \ln(x + 1)\,dx$

*Note (these notes):* The graph of $y=\ln(x+1)$ and $y=\ln(x+2)$ that accompanies part (b) is not reproduced.
:::

::: {.problem #prob-mit6042f10-7-q4 origin="external" source="mit6042f10-7-q4"}
There is a bug on the edge of a 1-meter rug. The bug wants to cross to the other side of the rug. It crawls at 1 cm per second. However, at the end of each second, a malicious first-grader named Mildred Anderson stretches the rug by 1 meter. Assume that her action is instantaneous and the rug stretches uniformly. Thus, here's what happens in the first few seconds:

- The bug walks 1 cm in the first second, so 99 cm remain ahead.
- Mildred stretches the rug by 1 meter, which doubles its length. So now there are 2 cm behind the bug and 198 cm ahead.
- The bug walks another 1 cm in the next second, leaving 3 cm behind and 197 cm ahead.
- Then Mildred strikes, stretching the rug from 2 meters to 3 meters. So there are now $3 \cdot (3/2) = 4.5$ cm behind the bug and $197 \cdot (3/2) = 295.5$ cm ahead.
- The bug walks another 1 cm in the third second, and so on.

Your job is to determine this poor bug's fate.

(a) During second $i$, what fraction of the rug does the bug cross?

(b) Over the first $n$ seconds, what fraction of the rug does the bug cross altogether? Express your answer in terms of the Harmonic number $H_n$.

(c) Approximately how many seconds does the bug need to cross the entire rug?
:::

::: {.problem #prob-mit6042f10-7-q6 origin="external" source="mit6042f10-7-q6"}
This problem continues the study of the asymptotics of factorials.

(a) Either prove or disprove each of the following statements.

- $n! = O((n + 1)!)$
- $n! = \Omega((n + 1)!)$
- $n! = \Theta((n + 1)!)$
- $n! = \omega((n + 1)!)$
- $n! = o((n + 1)!)$

(b) Show that $n! = \omega\left(\left(\frac{n}{3}\right)^{n+e}\right)$.

(c) Show that $n! = \Omega(2^n)$
:::
