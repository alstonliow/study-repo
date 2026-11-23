::: {.problem #prob-mit18335ps-1-q2 origin="external" source="mit18335ps-1-q2"}
**Funny functions**

(a) Write a function `L4(x,y)` in Julia to compute the $L_4$ norm $(|x|^4+|y|^4)^{1/4}$ of two scalars $x$ and $y$. Does your code give an accurate answer for `L4(1e-100,0.0)`? What about `L4(1e+100,0.0)`? Without using arbitrary-precision (`BigFloat`) calculations, fix your code so that it gives an answer whose relative error $\frac{|\text{computed}-\text{correct}|}{|\text{correct}|}$ is within a small multiple of `eps()` $=\varepsilon_{\text{machine}}$ (a few "ulps", or "units in the last place") of the exactly rounded answer for all double-precision $x$ and $y$. (You can test your code by comparing to `L4(big(x),big(y))`, i.e. arbitrary-precision calculation.)

(b) Write a function `cotdiff(x,y)` that computes $\cot(x)-\cot(x+y)$. Does your code give an accurate answer for `cotdiff(1.0, 1e-20)`? Without using arbitrary-precision (`BigFloat`) calculations, fix your code so that it gives an accurate `Float64` answer (within a few ulps) even when $|y|\ll|x|$ (without hurting the accuracy when $y$ and $x$ are comparable!). (Hint: one option would be to switch over to Taylor expansion when $|y|/|x|$ is sufficiently small, but a simpler solution is possible by applying some trigonometric identities.)
:::
