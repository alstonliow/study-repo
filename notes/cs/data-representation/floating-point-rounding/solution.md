::: {.solution for="prob-cmu15213r-3-q2" status="draft"}
Recall $\mathit{Bias}=3$; normalized values are $1.f_1f_2\times2^{e-3}$ for $1\le e\le6$, denormalized values $0.f_1f_2\times2^{-2}$.

| Value | Floating Point Bits | Rounded Value |
|---|---|---|
| 9/32 | 001 00 | 1/4 |
| 8 | 110 00 | 8 |
| 9 | 110 00 | 8 |
| 1/8 | 000 10 | 1/8 |
| 19 | 111 00 | $+\infty$ |

1. $\tfrac9{32}=0.01001_2=1.001_2\times2^{-2}$. With two fraction bits, $1.00\,|\,1$: guard $0$, round $1$, sticky $0$, an exact tie, so round to even: $1.00\times2^{-2}=\tfrac14$, exponent field $-2+3=1$ (@prp-round-to-even-rule).
2. $8=1.00_2\times2^3$, exponent field $6$: exact.
3. $9=1001_2=1.001_2\times2^3$: again a tie with guard bit $0$, rounded down to $1.00\times2^3=8$. So $8$ and $9$ share a pattern.
4. $000\,10$ is denormalized: $0.10_2\times2^{-2}=\tfrac18$.
5. $19=10011_2=1.0011_2\times2^4$. Rounding gives $1.01\times2^4=20$ (round bit $1$, sticky $1$), but $E=4$ would need exponent field $7=111$, which is reserved; the largest finite value is $14$, so the result overflows to $+\infty$, pattern $111\,00$.
:::

::: {.solution for="prob-float-to-int-code" status="draft"}
```{.c}
int float_to_int(unsigned uf) {
    unsigned sign = uf >> 31;
    int exp = (int) ((uf >> 23) & 0xFF) - 127;          /* E for normalized values */
    unsigned m = (uf & 0x7FFFFF) | 0x800000;            /* 1.frac as a 24-bit integer */
    if (exp < 0)                                        /* |f| < 1, also denormals and 0 */
        return 0;
    if (exp >= 31)                                      /* too large, infinity or NaN */
        return (int) 0x80000000u;
    if (exp >= 23) m <<= exp - 23;                      /* |f| = m * 2^(exp - 23) */
    else           m >>= 23 - exp;                      /* truncation toward zero */
    return sign ? -(int) m : (int) m;
}
```

1. A normalized value is $\pm M\cdot2^E$ with $M=1.\mathit{frac}$; written as an integer, $M\cdot2^{23}$ is the fraction field with bit 23 set, so $|f|=m\cdot2^{E-23}$.
2. If $E<0$ then $|f|<1$ and the result is $0$; denormalized values and $\pm0$ have exponent field $0$, so $E=-127$ and they land here too.
3. If $E\ge31$ then $|f|\ge2^{31}$: out of range except for $-2^{31}$ itself, whose correct result is also `0x80000000`. Infinity and NaN have exponent field $255$, so $E=128$, and fall into the same case.
4. Otherwise shift $m$ left or right by $E-23$; a right shift of the magnitude drops the fraction bits, which is truncation toward zero, and then the sign is applied. For $E\le30$ the magnitude is below $2^{31}$, so negating it is safe.
:::

::: {.solution for="prob-int-to-float-code" status="draft"}
```{.c}
unsigned int_to_float(int x) {
    unsigned sign = 0, u = x, e = 0, frac, rest, half;
    int top = 31;
    if (x == 0) return 0;
    if (x < 0) { sign = 0x80000000u; u = -u; }          /* unsigned negation: safe for INT_MIN */
    while (!(u >> top)) top--;                          /* u = 1.xxx * 2^top */
    e = top + 127;
    if (top <= 23) {
        frac = (u << (23 - top)) & 0x7FFFFF;            /* exact */
    } else {
        int drop = top - 23;
        frac = (u >> drop) & 0x7FFFFF;
        rest = u & ((1u << drop) - 1);                  /* the dropped bits */
        half = 1u << (drop - 1);
        if (rest > half || (rest == half && (frac & 1))) {
            frac++;
            if (frac == 0x800000) { frac = 0; e++; }    /* carry: 1.111.. rounds to 10.000.. */
        }
    }
    return sign | (e << 23) | frac;
}
```

1. Work with the magnitude $u=|x|$ as an `unsigned`; negating in unsigned arithmetic turns $-2^{31}$ into $2^{31}$ without overflow.
2. Find the position `top` of the highest set bit: $u=1.b\cdots\times2^{\mathit{top}}$, so the exponent field is $\mathit{top}+127$ and the 23 bits after the leading $1$ form the fraction.
3. If $\mathit{top}\le23$ every bit fits: shift the bits after the leading $1$ up to the top of the fraction field.
4. Otherwise $\mathit{drop}=\mathit{top}-23$ low bits are dropped. Comparing the dropped bits with half a unit in the last place $2^{\mathit{drop}-1}$ decides the rounding: above half rounds up, below half truncates, exactly half rounds up only when the last kept bit is $1$. This is $R\wedge(S\vee G)$ of @prp-round-to-even-rule.
5. Rounding up can carry out of the fraction ($1.11\cdots1+2^{-23}=2$); then the fraction becomes $0$ and the exponent grows by one, as for `INT_MAX`, which becomes $2^{31}$.
:::
