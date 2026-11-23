::: {.solution for="prob-how-many-bits-code" status="draft"}
```{.c}
int how_many_bits(int x) {
    int b16, b8, b4, b2, b1, b0;
    x = x ^ (x >> 31);               /* negative x -> ~x, which needs the same width */
    b16 = !!(x >> 16) << 4; x = x >> b16;
    b8  = !!(x >> 8) << 3;  x = x >> b8;
    b4  = !!(x >> 4) << 2;  x = x >> b4;
    b2  = !!(x >> 2) << 1;  x = x >> b2;
    b1  = !!(x >> 1);       x = x >> b1;
    b0  = x;
    return b16 + b8 + b4 + b2 + b1 + b0 + 1;
}
```

1. For $x\ge0$, the width is one more than the number of bits up to the highest $1$ (one extra for the sign bit $0$). For $x<0$, $x$ fits in $w$ bits exactly when $\mathord{\sim}x=-x-1\ge0$ fits, because the range $[-2^{w-1},2^{w-1}-1]$ is symmetric under $x\mapsto-x-1$. The arithmetic shift `x >> 31` is all ones for negative $x$ and zero otherwise, so `x ^ (x >> 31)` turns $x$ into $\mathord{\sim}x$ exactly when it is negative.
2. Now $x\ge0$; find the position of its highest $1$ by binary search. If anything is set in the top 16 bits, the answer includes those 16 positions: record $16$ and shift them down. Repeat with 8, 4, 2 and 1 bits on what is left.
3. After the halvings $x$ is $0$ or $1$; `b0` counts that last bit. The sum of the recorded amounts is the number of significant bits, and the final $+1$ is the sign bit. For $x=0$ every term is $0$ and the answer is $1$.
:::
