<!-- Solutions marked status="draft" were written by Claude with the FIT1058
     sample solutions as a reference; not copied. Owner to review, then remove status. -->

::: {.solution for="prob-predicate-11"}
Write $\text{Date}(d,m,y)$ as $D(d,m,y)$. $(d_1,m_1,y_1)$ comes
chronologically before $(d_2,m_2,y_2)$ exactly when
$$y_1<y_2, \quad\text{or}\quad y_1=y_2 \wedge m_1<m_2, \quad\text{or}\quad y_1=y_2\wedge m_1=m_2\wedge d_1<d_2.$$

So the answer is
$$D(d_1,m_1,y_1)\wedge D(d_2,m_2,y_2)\wedge\Big((y_1<y_2)\vee\big((y_1=y_2)\wedge(m_1<m_2)\big)\vee\big((y_1=y_2)\wedge(m_1=m_2)\wedge(d_1<d_2)\big)\Big)$$
:::
