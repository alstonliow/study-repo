::: {.solution for="prob-bit-xor-code" status="draft"}
```{.c}
int bit_xor(int x, int y) {
    /* x ^ y = (x | y) & ~(x & y), and x | y = ~(~x & ~y) */
    return ~(~x & ~y) & ~(x & y);
}
```

1. A bit of $x\oplus y$ is $1$ when at least one input bit is $1$ but not both: $(x\vee y)\wedge\neg(x\wedge y)$.
2. `|` is not allowed, so rewrite $x\vee y$ by De Morgan as $\neg(\neg x\wedge\neg y)$. Everything is bitwise, so the identity holds in each of the 32 positions at once.
:::

::: {.solution for="prob-conditional-code" status="draft"}
```{.c}
int conditional(int x, int y, int z) {
    int mask = !x + ~0;        /* x != 0: 0 + (-1) = all ones; x == 0: 1 + (-1) = 0 */
    return (mask & y) | (~mask & z);
}
```

1. `!x` is $1$ when $x=0$ and $0$ otherwise, and `~0` is $-1$ (@prp-twos-complement-facts). Their sum is $0$ when $x=0$ and $-1$, the all-ones pattern, when $x\ne0$: a mask $m$ that is all ones exactly when $x$ is true.
2. `(m & y) | (~m & z)` keeps all bits of $y$ and none of $z$ when $m$ is all ones, and the reverse when $m$ is zero.
:::
