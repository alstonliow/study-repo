::: {.problem #prob-mit18s096-8-q1 origin="external" source="mit18s096-8-q1"}
A common variation on the above procedure, which often appears in machine learning, involves a function $f(x,p)\in\mathbb{R}$ that maps input "data" $x\in\mathbb{R}^n$ and "parameters" $p\in\mathbb{R}^N$ to a scalar. Let $\nabla_x f$ and $\nabla_p f$ denote the gradients with respect to $x$ and $p$.

Now, suppose we have a function $g(z):\mathbb{R}^n\mapsto\mathbb{R}$ as before, and define $h(x,p)=g(\nabla_x f|_{x,p})$. We want to compute $\nabla_p h=(\partial h/\partial p)^T$, which will involve "mixed" derivatives of $f$ with respect to both $x$ and $p$.

Show that you can compute $\nabla_p h$ by:
$$
\nabla_p h|_{x,p}=\frac{\partial}{\partial\alpha}\left(\nabla_p f\big|_{x+\alpha\nabla g|_z,\,p}\right)\Bigg|_{\alpha=0},
$$
where $z=\nabla_x f|_{x,p}$. (Crucially, this avoids ever computing an $n\times N$ mixed-derivative matrix of $f$.)

Try coming up with simple example functions $f$ and $g$, implementing the above formula by forward-over-reverse in Julia similar to above (forward mode for $\partial/\partial\alpha$ and reverse mode for the $\nabla$'s), and checking your result against a finite-difference approximation.

*Note (these notes):* \"The above procedure\" is forward-over-reverse differentiation, @prp-forward-over-reverse.
:::
