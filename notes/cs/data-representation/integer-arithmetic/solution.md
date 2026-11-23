::: {.solution for="prob-is-less-or-equal-code" status="draft"}
```{.c}
int is_less_or_equal(int x, int y) {
    int sx = (x >> 31) & 1, sy = (y >> 31) & 1;
    int diff = y + (~x + 1);                 /* y - x, may overflow */
    int nonneg = !((diff >> 31) & 1);
    int differ = sx ^ sy;
    return (differ & sx) | (!differ & nonneg);
}
```

1. If $x$ and $y$ have different signs, the answer is decided by the signs alone: $x\le y$ exactly when $x$ is the negative one, that is, $s_x=1$.
2. If they have the same sign, $y-x$ cannot overflow: both lie in $[0,TMax_w]$ or both in $[TMin_w,-1]$, so the difference lies in $[-TMax_w,TMax_w]$. Then $x\le y$ exactly when $y-x\ge0$, read off its sign bit. $-x$ is computed as `~x + 1` (@prp-twos-complement-negation); for $x=TMin_w$ this wraps, but in the same-sign case the wrapped sum is still the correct $y-x$ modulo $2^{32}$, which is representable.
3. `differ` selects between the two cases with Boolean operators on single bits.
:::

::: {.solution for="prob-divide-power2-code" status="draft"}
```{.c}
int divide_power2(int x, int n) {
    int bias = (x >> 31) & ((1 << n) + ~0);   /* 2^n - 1 if x < 0, else 0 */
    return (x + bias) >> n;
}
```

1. For $x\ge0$ the arithmetic shift is $\lfloor x/2^n\rfloor$, which is also the quotient rounded toward zero.
2. For $x<0$, item 4 of @thm-shift-multiply-divide: adding $2^n-1$ before shifting turns the floor into a ceiling, which is rounding toward zero for negative numbers.
3. `x >> 31` is all ones exactly when $x<0$, so ANDing it with $2^n-1$ (written `(1 << n) + ~0`, since `~0` is $-1$) gives the bias only for negative $x$. The sum $x+2^n-1$ cannot overflow for $x<0$.
:::
