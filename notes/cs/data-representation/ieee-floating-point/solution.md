::: {.solution for="prob-cmu15213r-3-q1" status="draft"}
1. **Bias.** $\mathit{Bias}=2^{k-1}-1=2^2-1=3$.

2. **Largest denormalized number.** Exponent field $000$, largest fraction $11$: $M=0.11_2=\tfrac34$ and $E=1-\mathit{Bias}=-2$, so the value is $\tfrac34\cdot\tfrac14=\tfrac3{16}$ (bits $000\,11$).

3. **Smallest normalized number.** Exponent field $001$, fraction $00$: $M=1$, $E=1-3=-2$, value $\tfrac14$ (bits $001\,00$). It is one step $\tfrac1{16}$ above the largest denormalized number (@prp-denormal-continuity).

4. **Largest finite number.** The exponent field $111$ is reserved for infinity and NaN, so the largest finite value has exponent field $110$ ($E=6-3=3$) and fraction $11$ ($M=1.11_2=\tfrac74$): $\tfrac74\cdot8=14$ (bits $110\,11$).

5. **Smallest nonzero value.** The smallest denormalized number with fraction $01$: $\tfrac14\cdot\tfrac14=\tfrac1{16}$ (bits $000\,01$).
:::

::: {.solution for="prob-float-scale2-code" status="draft"}
```{.c}
unsigned float_scale2(unsigned uf) {
    unsigned sign = uf & 0x80000000u;
    unsigned exp = (uf >> 23) & 0xFF;
    unsigned frac = uf & 0x7FFFFF;
    if (exp == 0xFF)                       /* infinity or NaN: unchanged */
        return uf;
    if (exp == 0)                          /* denormalized: double the fraction */
        return sign | (frac << 1);         /* a carry into bit 23 makes it normalized */
    exp++;
    if (exp == 0xFF)                       /* overflow to infinity */
        return sign | 0x7F800000u;
    return sign | (exp << 23) | frac;
}
```

1. Split the pattern into sign, exponent field and fraction field (@def-ieee-floating-point).
2. Infinity times two is infinity, and NaN must be returned unchanged, so exponent field $255$ returns `uf`.
3. A denormalized value is $f\cdot2^{-126}$ with $f=0.\mathit{frac}$; doubling it doubles the fraction, a left shift by one. If the top fraction bit was $1$, the shift carries into bit 23, the lowest exponent bit, which gives exponent field $1$ and the correct normalized value $1.f'\cdot2^{-126}$: this is the smooth transition of @prp-denormal-continuity, and it needs no special case.
4. A normalized value $M\cdot2^E$ doubles by adding $1$ to $E$, that is, to the exponent field. If the field becomes $255$ the result overflows and is $\pm\infty$, whose fraction field must be zero.
:::
