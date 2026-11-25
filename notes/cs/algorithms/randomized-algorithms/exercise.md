::: {.problem #prob-mit6046s15-4-q2 origin="external" source="mit6046s15-4-q2"}
**Quicksort Analysis**

In this problem, we will analyze the time complexity of QUICKSORT in terms of error probabilities, rather than in terms of expectation. Suppose the array to be sorted is $A[1..n]$, and write $x_i$ for the element that starts in array location $A[i]$ (before QUICKSORT is called). Assume that all the $x_i$ values are distinct.

In solving this problem, it will be useful to recall a claim from lecture. Here it is, slightly restated:

*Claim:* Let $c>1$ be a real constant, and let $\alpha$ be a positive integer. Then, with probability at least $1-\frac1{n^\alpha}$, $3(\alpha+c)\lg n$ tosses of a fair coin produce at least $c\lg n$ heads.

Note: High probability bounds, and this Claim, will be covered in Tuesday's lecture.

(a) Consider a particular element $x_i$. Consider a recursive call of QUICKSORT on subarray $A[p..p+m-1]$ of size $m\ge2$ which includes element $x_i$. Prove that, with probability at least $\frac12$, either this call to QUICKSORT chooses $x_i$ as the pivot element, or the next recursive call to QUICKSORT containing $x_i$ involves a subarray of size at most $\frac34m$.

(b) Consider a particular element $x_i$. Prove that, with probability at least $1-\frac1{n^2}$, the total number of times the algorithm compares $x_i$ with pivots is at most $d\lg n$, for a particular constant $d$. Give a value for $d$ explicitly.

(c) Now consider all of the elements $x_1,x_2,\dots,x_n$. Apply your result from part (b) to prove that, with probability at least $1-\frac1n$, the total number of comparisons made by QUICKSORT on the given array input is at most $d'n\lg n$, for a particular constant $d'$. Give a value for $d'$ explicitly. *Hint:* The Union Bound may be useful for your analysis.

(d) Generalize your results above to obtain a bound on the number of comparisons made by QUICKSORT that holds with probability $1-\frac1{n^\alpha}$, for any positive integer $\alpha$, rather than just probability $1-\frac1n$ (i.e., $\alpha=1$).
:::
