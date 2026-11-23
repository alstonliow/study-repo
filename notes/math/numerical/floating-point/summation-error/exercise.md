::: {.problem #prob-mit18335ps-1-q4 origin="external" source="mit18335ps-1-q4"}
**Addition, another way**

Here you will analyze $f(x)=\sum_{i=1}^n x_i$, but you will compute $\tilde f(x)$ in a different way from the naive sum considered in class. In particular, compute $\tilde f(x)$ by a recursive divide-and-conquer approach, recursively dividing the set of values to be summed in two halves and then summing the halves:
$$\tilde f(x)=\begin{cases}0&\text{if }n=0\\ x_1&\text{if }n=1\\ \tilde f(x_{1:\lfloor n/2\rfloor})\oplus\tilde f(x_{\lfloor n/2\rfloor+1:n})&\text{if }n>1\end{cases},$$
where $\lfloor y\rfloor$ denotes the greatest integer $\le y$ (i.e. $y$ rounded down). In exact arithmetic, this computes $f(x)$ exactly, but in floating-point arithmetic this will have very different error characteristics than the simple loop-based summation in class.

(a) For simplicity, assume $n$ is a power of 2 (so that the set of numbers to add divides evenly in two at each stage of the recursion). Prove that $|\tilde f(x)-f(x)|\le\epsilon_{\text{machine}}\log_2(n)\sum_{i=1}^n|x_i|+O(\epsilon_{\text{machine}}^2)$. That is, show that the worst-case error bound grows logarithmically rather than linearly with $n$!

(b) Pete R. Stunt, a Microsoft employee, complains, "While doing this kind of recursion may have nice error characteristics in theory, it is ridiculous in the real world because it will be insanely slow—I'm proud of my efficient software and can't afford to have a function-call overhead for every number I want to add!" Explain to Pete how to implement a slight variation of this algorithm with the same logarithmic error bounds (possibly with a worse constant factor) but roughly the same performance as a simple loop.

(c) In the pset 1 Julia notebook, there is a function "div2sum" that computes $\tilde f(x)=$ div2sum(x) in single precision by the above algorithm. Modify it to not be horrendously slow via your suggestion in (b), and then plot its errors for random inputs as a function of $n$ with the help of the example code in the Julia notebook (but with a larger range of lengths $n$). Are your results consistent with your error bounds above?
:::
